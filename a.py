import threading as th
import os
def func(offset):

    sv_addr = 

    ct_addr = "127.0.0.1:"+str(offset+1000)
    os.system("java -jar cf-cocoa-3.9.0-SNAPSHOT.jar")
n = 10 # number of threads
for i in range(n):
    
    t[i]=th.Thread(target=func,args=(i,))
    t[i].start()
for i in range(n):
    t[i].join()


