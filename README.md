# Inserting and Fetching Data into Database using Multi-threading
## Libraries Used
### 1. threading:
                1.a Events: To lock crucial parts of database to reduce race conditions
                1.b Locks : To lock parts of program
                1.c Currentthread().getName()  : To get name of current thread
#### 2. concurrent.futures:
                ThreadPoolExecutor to handle threads introduced in python 3.2 and above
### 3. queue:
                FIFO type queue is used
_________________________________________________________________________________________________________

## User defined Functions:
### a1-a4 :  Takes item from queue and print it
_________________________________________________________________________________________________________

## Target: We have to print 1-100 using 4 threads 
_________________________________________________________________________________________________________
## working of code
We have 4 functions a1-a4 and a queue .We have to put first 100 numbers in queue .
Using for loop in range of 1-101 we put each number in queue using below method
                       queue.put(number) 
Now we have to create 4 functions and paramater queue is passed in each function
In each function,we use below code ,the program will execute while the queue is not empty. 
                  while not queue.empty()
In each function, we use code to get item and this will get first input.Since it is FIFO queue Our first item will be printed and removed from queue.
                   queue.get() 
Now for controlling threads, we use 4 events e1-e4 and create events.
                  e1=Event()
First we will set the thread 1 using e1.set() method.This will set thread 1.After printing 1 number in thread 1,use e1.clear() and then e2.set().This will pause thread 1 and thread 2 will print 1 number and then e2.clear and e3.set() and same 4th thread.In 4th thread we use e4.clear() and e1.set()
This will print all numbers one by one but there is a problem when thread 1 wil print 97 and it wont end.
By this our program will run continuosly.
For that we use if statement and break statement.
        if queue.get()==97:
             break
The above line will break the loop we have to use this in every function.
Now its time to call the function .For this we use concurrent.futures.
   with concurrent.futures.ThreadPoolExecutor() as ex:
        ex.submit(a1,q)

This will call threads and pass argument queue as q and hence all threads will print each number one by one and form counting from 1 to 100 
 
