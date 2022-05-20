from threading import *

class Flight():
    def __init__(self,seats) :
        self.seats=seats
        self.l=Lock()
    def bookSeat(self,needSeat,name):
        self.l.acquire()
        print(f"Available seats ={self.seats}")
        print(current_thread().name)
        if needSeat>self.seats:
            print("Sorry,Seats Unavailable")
        else:
            print(f"Dear {name}, Your seat is confirmed ")
            self.seats-=1
        self.l.release()
f=Flight(2)
t1=Thread(target=f.bookSeat,args=(1,"Sahil"))
t2=Thread(target=f.bookSeat,args=(1,"Raj"))
t3=Thread(target=f.bookSeat,args=(1,"Sonam"))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print(current_thread().name)