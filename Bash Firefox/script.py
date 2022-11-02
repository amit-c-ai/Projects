import os
import subprocess
import sys

arguments= sys.argv #First  Argument is IP
ip= arguments[1]
filename=arguments[2]  # Second is file.txt
f=open(filename) 
data=f.read().split('\n')
data.pop()
for i in  range(len(data)):
	data[i]=ip+data[i]
data=["firefox"]+["unused"]+ data
subprocess.call(data)

