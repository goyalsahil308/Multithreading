from threading import *
import time
def a1():
    a=1
    print(a)
    while a<=96:
        a=a+4
        time.sleep(2)
        print(a)
def a2():
    b=2
    print(b)
    while b<=96:
        b=b+4
        time.sleep(2) 
        print(b)
def a3():
    c=3
    print(c)
    while c<=96:
        c=c+4
        time.sleep(2)   
        print(c)
def a4():
    d=4
    print(d)
    while d<=96:
        d=d+4
        time.sleep(2)    
        print(d)
t1=Thread(target=a1)
t2=Thread(target=a2)
t3=Thread(target=a3)
t4=Thread(target=a4)
t1.start()
time.sleep(0.15)
t2.start()
time.sleep(0.15)
t3.start()
time.sleep(0.15)
t4.start()
time.sleep(0.15)
print("Done")
