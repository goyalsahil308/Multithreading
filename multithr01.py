import time
from threading import *
def odd():
    for i in range(1,100,2):
        time.sleep(1)
        print(i,current_thread().getName())
def even():
    for i in range(2,101,2):
        time.sleep(1)
        print(i,current_thread().getName())
t1=Thread(target=odd,)
t2=Thread(target=even,)
t1.start()
time.sleep(0.2)
t2.start()
t1.join()
t2.join()
print("Bye",current_thread().getName())
