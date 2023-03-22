import threading as th
import os,time
def func(offset):

    # sv_addr = 

    # ct_addr = "127.0.0.1:"+str(offset+1000)
    # os.system("java -jar cf-cocoa-3.9.0-SNAPSHOT.jar coap://127.0.0.1:5683")
    os.system("java -jar cf-cocoaA-3.9.0-SNAPSHOT.jar coap://192.168.137.10:5683")

n = 10 # number of threads
t=[0]*n
st=time.time()
for i in range(n):
    
    t[i]=th.Thread(target=func,args=(i,))
    t[i].start()
for i in range(n):
    t[i].join()
en=time.time()
print((en-st)/n)


