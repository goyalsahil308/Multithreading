from threading import *
e=Event()
def odd():
        for i in range(1,100,2):
            print(i)
            e.wait()
            e.set()


def even ():
        e.wait()
        for i in range(2,101,2):
            print(i)
            e.set()


t1=Thread(target=odd)
t2=Thread(target=even)
t1.start()
t2.start()

