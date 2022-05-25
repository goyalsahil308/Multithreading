from concurrent.futures import thread
from threading import *
import concurrent.futures 
import queue
e1=Event()
e2=Event()
e3=Event()
e4=Event()

def a1(q):
    e1.set()
    while not q.empty():
        if e1.wait():
            x=q.get()
            if x!=97:
                print(x)
                e2.set()
                e1.clear()
            else:
                print(x)
                e2.set()
                break
    print("1 finished")
                
                
def a2(q):
    while not q.empty():
        if e2.wait():
            x=q.get()
            if x!=98:
                print(x)
                e3.set()
                e2.clear()
            else:
                print(x)
                e3.set()
                break
    print("2 finished")
                
def a3(q):
    while not q.empty():
        if e3.wait():
            x=q.get()
            if x!=99:
                print(x)
                e4.set()
                e3.clear()
            else:
                print(x)
                e4.set()
                break
    print("3 finish")        
        
def a4(q):
    while not q.empty():
        if e4.wait():
            x=q.get()
            if x!=100:
                print(x)
                e1.set()
                e4.clear()
            else:
                print(x)
                break
    print("4 finished")
q=queue.Queue()
for i in range(1,101):
    q.put(i)
with concurrent.futures.ThreadPoolExecutor() as ex:
    ex.submit(a1,q)
    ex.submit(a2,q)
    ex.submit(a3,q)
    ex.submit(a4,q)