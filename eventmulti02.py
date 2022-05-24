from threading import *
e1=Event()
e2=Event()
e3=Event()
e4=Event()

def a1():
    a=1
    e1.set()
    while a<=96:
        a=a+4
        if e1.wait():
                print(a)
                e2.set()
                e1.clear()
                
                
def a2():
    b=2
    while a<=96:
        b=b+4
        if e2.wait():
            print(b)
            e3.set()
            e2.clear()
                
def a3():
    c=3
    while c<=96:
        c=c+4
        if e3.wait():
            print(c)
            e4.set()
            e3.clear()
        
        
def a4():
    d=4
    while d<=96:
        d=d+4
        if e4.wait():
            e1.set()
            e4.clear()
            print(d)
a=1
print(a)
b=2
print(b)
c=3
print(c)
d=4
print(d)
t1=Thread(target=a1)
t2=Thread(target=a2)
t3=Thread(target=a3)
t4=Thread(target=a4)
t1.start()
t2.start()
t3.start()
t4.start()
