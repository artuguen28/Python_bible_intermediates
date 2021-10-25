# Types of threading:
#   Kernel Threads: part of the operational system
#   User Threads: managed by the programmer

# Importing the respective library threading.
import time
import threading


def hello():
    print("Hello World!")


# it doesn't need parentheses, since we're not calling it.
t1 = threading.Thread(target=hello)
# t1.start()


# The run() function, on the other hand, is used when we're dealing eith more than just on thread.

def function1():
    for x in range(1000):
        print("ONE")


def function2():
    for x in range(1000):
        print("TWO")


t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

# Alternates between ONEs and TWOs.
# t1.start()
# t2.start()

# First ONEs and then TWOs.
# t1.run()
# t2.run()

# Will wait for the last thread to finish before we move with the last.
# t1.join()
#   It can also wait a specific time to procede.
#   t1.join(5)

# Building a class that inherits the Thread class

import threading

class MyThread(threading.Thread):

    def __init__(self, message):
        threading.Thread.__init__(self)
        self.message = message

    def run(self):
        for x in range(10):
            print(self.message)

#mt1 = MyThread("This is my thread message!")
#mt1.start()


# Synchronizing threads

import time

x = 8192
lock = threading.Lock()


def halve():
    global x, lock
    lock.acquire()
    while(x > 1):
        x /= 2
        print(x)
        time.sleep(1)
    print("END!")
    lock.release()


def double():
    global x, lock
    lock.acquire() #Locks here 
    while(x < 16384):
        x *= 2
        print(x)
        time.sleep(1)
    print("END!") 
    lock.release() #Release here

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

#t1.start()
#t2.start()

# Semaphores
