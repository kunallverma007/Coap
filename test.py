import os,sys
import threading
sys.path.append(r"C:\Users\hp\Desktop\Co-ap\txThings-master")

# import examples.clientGET as temp

def client(port):
    uris=r"C:\Users\hp\Desktop\Co-ap\txThings-master\examples\clientPUT.py "+ str(port)
    # print(uris)
    os.system(uris)
    # print(port)
    # temp.call(port)



for i in range(1):
    print("Thread",i,"starting .........................................")
    x=threading.Thread(target=client,args=(i,))
    x.start()
    print("Thread",i,"started ........................................")
