#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFile>
#include <QFileDialog>
#include <QMessageBox>
#include <QTextStream>
#include <QtDebug>
#include <QTime>
#define PRIME 7
const int T_S = 819;
long long probe;
QString file_name;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

struct input{
    QString id, name, surname, address, country, email;
};
class HashTableEntry {
   public:
      long long k;
      struct input *v;
      HashTableEntry(long long k, struct input *v) {
         this->k= k;
         this->v = v;
      }
};
class HashMapTable {
   public:
      HashTableEntry *t[819];
      QString showData[819];
   public:
      HashMapTable() {
         for (int i = 0; i< T_S; i++) {
            t[i] = NULL;
         }
      }
      int HashFunc(long long k) {
         return k % T_S;
      }
      int clusterFunc(long long k, int c){
          return (HashFunc(k) + c)%T_S;
      }
      void Insert(long long k, struct input *v, int choice, int c) {
          int h;
          if(choice==0)
              h = HashFunc(k);
          else if(choice==1)
              h = HashFunc(k);
          else if(choice==2)
              h = clusterFunc(k, c);

         while (t[h] != NULL && t[h]->k != k) {
             if(choice==0)
                h = HashFunc(h + 1);
             else if(choice==1)
                 h = HashFunc(h + c);
             else if(choice==2)
                 h = clusterFunc(h + 1, c);
            probe++;
         }

         if (t[h] != NULL)
            delete t[h];
         t[h] = new HashTableEntry(k, v);
         QString enter;
         enter = QString::number(h) + "        " + t[h]->v->id + "        " + t[h]->v->email + "\n";
         showData[h]=enter;

      }
      ~HashMapTable() {
         for (int i = 0; i < T_S; i++) {
            if (t[i] != NULL)
               delete t[i];
         }
      }
};
class doubleHashMapTable {
   public:
      HashTableEntry **t;
      QString showData[819];
   public:
      doubleHashMapTable() {
         t = new HashTableEntry * [T_S];
         for (int i = 0; i< T_S; i++) {
            t[i] = NULL;
         }
      }
      int HashFunc(long long k) {
         return k % T_S;
      }
      int doubleHashFunc(long long k){
          return (PRIME - (k % PRIME));
      }

      void Insert(long long k, struct input *v) {
         int h = HashFunc(k);

         if (t[h] != NULL) {
             int h2 = doubleHashFunc(k);
             int i = 1;
             while(1){
                 int newIndex = (h + i * h2) % T_S;

                 if (t[newIndex] == NULL) {
                     delete t[newIndex];
                     t[newIndex] = new HashTableEntry(k, v);
                     QString enter;
                     enter = QString::number(h) + "        " + t[h]->v->id + "        " + t[h]->v->email + "\n";
                     showData[h]=enter;
                     break;
                 }
                 i++;
             }
             probe++;
         }
         else{
             delete t[h];
             t[h] = new HashTableEntry(k, v);
             QString enter;
             enter = QString::number(h) + "        " + t[h]->v->id + "        " + t[h]->v->email + "\n";
             showData[h]=enter;
         }
      }
      ~doubleHashMapTable() {
         for (int i = 0; i < T_S; i++) {
            if (t[i] != NULL)
               delete t[i];
            delete[] t;
         }
      }
};
void MainWindow::on_pushButton_clicked()
{
    file_name = QFileDialog::getOpenFileName(this, "select files", "C:/");


    QFile filename(file_name);
    if(!filename.open(QFile::ReadOnly | QFile::Text)){
        QMessageBox::warning(this, "title", "file not open");
    }

    QTextStream in(&filename);
    QString text = in.readAll();
    ui->plainTextEdit_2->setPlainText(text);
    filename.close();
}

void delay()
{
    QTime dieTime= QTime::currentTime().addSecs(1000);
    while (QTime::currentTime() < dieTime)
        QCoreApplication::processEvents(QEventLoop::AllEvents, 100);
}

void MainWindow::on_pushButton_2_clicked()
{
    int choice = ui->comboBox->currentIndex();

    if(choice==0) {
        int c = ui->spinBox->value();
        HashMapTable hash;
        long long k;
        int i=0;
        probe = 0;
        QString data = ui->plainTextEdit_2->toPlainText();
        QStringList newdata = data.split("\n");
        QString var;
        QStringList newvar;

        foreach (var, newdata) {
            struct input v;
            newvar = var.split(",");
            if(!(newvar.size()<6)){
                v.id = newvar[0];
                v.name = newvar[1];
                v.surname = newvar[2];
                v.address = newvar[3];
                v.country = newvar[4];
                v.email = newvar[5];
                k = (v.id).toDouble();
                hash.Insert(k, &v, choice, c);
                i++;
            }
        }
        ui->lineEdit_9->setText(QString::number(i));
        QStringList temp;
        for(int i=0;i<819;i++){
            if(!hash.showData[i].isEmpty())
                temp.append(hash.showData[i]);
        }
        QString show = temp.join("\n");
        ui->plainTextEdit->setPlainText(show);
        double avgprobe = (float)probe/i;
        double totalprobe = probe;
        ui->lineEdit_7->setText(QString::number(avgprobe));
        ui->lineEdit_8->setText(QString::number(totalprobe));
        delay();
    }
    else if(choice==1){
        int c = ui->spinBox_2->value();
        HashMapTable hash;
        long long k;
        int i=0;
        probe = 0;
        QString data = ui->plainTextEdit_2->toPlainText();
        QStringList newdata = data.split("\n");
        QString var;
        QStringList newvar;
        foreach (var, newdata) {
            struct input v;
            newvar = var.split(",");
            if(!(newvar.size()<6)){
                v.id = newvar[0];
                v.name = newvar[1];
                v.surname = newvar[2];
                v.address = newvar[3];
                v.country = newvar[4];
                v.email = newvar[5];
                k = (v.id).toDouble();
                hash.Insert(k, &v, choice, c);
                i++;
            }
        }
        ui->lineEdit_9->setText(QString::number(i));
        QStringList temp;
        for(int i=0;i<819;i++){
            if(!hash.showData[i].isEmpty())
                temp.append(hash.showData[i]);
        }
        QString show = temp.join("\n");
        ui->plainTextEdit->setPlainText(show);
        double avgprobe = (float)probe/i;
        double totalprobe = probe;
        ui->lineEdit_7->setText(QString::number(avgprobe));
        ui->lineEdit_8->setText(QString::number(totalprobe));
        delay();
    }
    else if(choice==2){
        int c = ui->spinBox->value();
        HashMapTable hash;
        long long k;
        int i=0;
        probe = 0;
        QString data = ui->plainTextEdit_2->toPlainText();
        QStringList newdata = data.split("\n");
        QString var;
        QStringList newvar;
        foreach (var, newdata) {
            struct input v;
            newvar = var.split(",");
            if(!(newvar.size()<6)){
                v.id = newvar[0];
                v.name = newvar[1];
                v.surname = newvar[2];
                v.address = newvar[3];
                v.country = newvar[4];
                v.email = newvar[5];
                k = (v.id).toDouble();
                hash.Insert(k, &v, choice, c);
                i++;
            }
        }
        ui->lineEdit_9->setText(QString::number(i));
        QStringList temp;
        for(int i=0;i<819;i++){
            if(!hash.showData[i].isEmpty())
                temp.append(hash.showData[i]);
        }
        QString show = temp.join("\n");
        ui->plainTextEdit->setPlainText(show);
        double avgprobe = (float)probe/i;
        double totalprobe = probe;
        ui->lineEdit_7->setText(QString::number(avgprobe));
        ui->lineEdit_8->setText(QString::number(totalprobe));
        delay();
    }
    else if(choice==3){
        doubleHashMapTable hash;
        long long k;
        int i=0;
        probe = 0;
        QString data = ui->plainTextEdit_2->toPlainText();
        QStringList newdata = data.split("\n");
        QString var;
        QStringList newvar;
        foreach (var, newdata) {
            struct input v;
            newvar = var.split(",");
            if(!(newvar.size()<6)){
                v.id = newvar[0];
                v.name = newvar[1];
                v.surname = newvar[2];
                v.address = newvar[3];
                v.country = newvar[4];
                v.email = newvar[5];
                k = (v.id).toDouble();
                hash.Insert(k, &v);
                i++;
            }
        }
        ui->lineEdit_9->setText(QString::number(i));
        QStringList temp;
        for(int i=0;i<819;i++){
            if(!hash.showData[i].isEmpty())
                temp.append(hash.showData[i]);
        }
        QString show = temp.join("\n");
        ui->plainTextEdit->setPlainText(show);
        double avgprobe = (float)probe/i;
        double totalprobe = probe;
        ui->lineEdit_7->setText(QString::number(avgprobe));
        ui->lineEdit_8->setText(QString::number(totalprobe));
        delay();
    }
}

void MainWindow::on_pushButton_3_clicked()
{
    QString add = ui->lineEdit->text()+","+ui->lineEdit_2->text()+","+ui->lineEdit_3->text()+","+ui->lineEdit_4->text()+","+ui->lineEdit_5->text()+","+ui->lineEdit_6->text()+"\n";
    QString data = ui->plainTextEdit_2->toPlainText()+add;
    ui->plainTextEdit_2->setPlainText(data);
}
