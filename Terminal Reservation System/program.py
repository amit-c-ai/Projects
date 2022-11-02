import threading
import os
import sqlite3 as sl

con = sl.connect('my-test.db')

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS USER(
            busId INTEGER NOT NULL PRIMARY KEY,
            pickupLocation TEXT,
            destination TEXT,
            gender TEXT,
            driverName TEXT,
            seatsAvailable INTEGER,
            pickupTime TEXT
        );
    """)

def readFile():
    print('Child process ( id=', os.getpid(), ")    function to read data from file")
    print("----------------------------------------")
    file1 = open('data.txt', 'r')
    Lines = file1.readlines()

    count = 0
    data = []
    for line in Lines:
        count += 1
        if(count>2):
            x = line.split(" ")
            x = tuple(x)
            data.append(x)

    return data

def writeFile(data):
    file = open('newfile.txt', 'w')
    file.write("Bus #. SQU Location Destination Student's Gender Driver's Name available seats Pick-Up\n")
    file.write("-------- ----------------- -------------- --------------------- ----------------- ------------------ -----------------\n")

    for row in data:
        count=0
        for i in row:
            count = count+1
            if(count!=7):
                file.write(str(i)+" ")
            else:
                file.write(str(i))


def maintainDb():
    print("Child process ( id=", os.getpid(), ")    function to maintain database")
    print("----------------------------------------")
    sql = 'INSERT INTO USER (busId, pickupLocation, destination, gender, driverName, seatsAvailable, pickupTime) values (?, ?, ?, ?, ?, ?, ?)'
    data = readFile()

    with con:
        con.executemany(sql, data)

def show(gender):
    print("Child process (id=", os.getpid(), ") function to show data")
    print("----------------------------------------")
    with con:
        if(gender == "all"):
            data = con.execute("SELECT * FROM USER")
        else:
            data = con.execute("SELECT * FROM USER WHERE gender=?", (gender,))
        for row in data:
            print(row)

def reserve(id, n):
    with con:
        data = con.execute("SELECT seatsAvailable FROM USER WHERE busId=?",(id,))
        data = list(data)[0][0]

        if(data>=n):
            con.execute("UPDATE USER SET seatsAvailable=? WHERE busId=?;", (data-n, id,))
            print("Your seats reserved successfully! Seats remaining: {}".format(data-n))
        else:
            print("Error: Number of seats you want to reserve is greater than the available number of seats.")

    with con:
        data = con.execute("SELECT * FROM USER")
        Data = []
        for row in data:
            Data.append(list(data))
        p = threading.Thread(target=writeFile, args=Data)
        p.start()
        p.join()
    

if __name__ == '__main__':
    print("Parent process ( id=", os.getppid(), ")   calling maintainDb function")
    print("----------------------------------------")
    maintainDb()
    while(True):
        print("\n\nParent process (id=", os.getppid(), ") while loop to give options")
        print("----------------------------------------")
        option = int(input("Choose option: \n1. Reserve Ticket\n2. Quit\n===> "))
        if(option==2):
            exit("\nThank you!\n")
        elif(option==1):
            show("all")
            gender = input("\n\nEnter gender: ")
            show(gender)
            id = int(input("Enter bus id: "))
            n = int(input("Enter number of tickets you want to reserve: "))
            reserve(id, n)
        else:
            print("Wrong input")