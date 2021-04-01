#Pass the first parameter as any file.txt and second as ip address.
for i in `cat $2 | sed "s#/#$1/#g"`; do firefox $i;done;
