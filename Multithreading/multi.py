# Types of threading:
#   Kernel Threads: part of the operational system
#   User Threads: managed by the programmer

# Importing the respective library threading.
import time
import threading
from typing import Text


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

import threading
import time


semaphore = threading.BoundedSemaphore(value=5) # Create the semaphore object


def access(thread_number):

    print("{}: Trying access...".format(thread_number))
    semaphore.acquire()
    print("{}: Access granted!".format(thread_number))
    print("{}: Waiting 5 seconds...".format(thread_number))
    time.sleep(5)
    semaphore.release()
    print("{}: Releasing!".format(thread_number))

#for thread_number in range(10):
#    t = threading.Thread(target=access, args=(thread_number,))
#    t.start()

# When we run this code, you will see that the first five threads will immediately run the code, whereas the remaining five threads will need to wait five seconds until the first threads release the semaphore.


# Events 

# Basically used to manage our threads even better.
# It will activate a thread when a certain event happens.

import threading

event = threading.Event()

def function():
    print("Waitng for event...")
    event.wait()
    print("Continuing!")

thread = threading.Thread(target=function)
#thread.start()

#x = input("Trigger event? ")
#if x == "yes":
#    event.set()

# Daemon Threads

#Daemon threads are typically used for background tasks like synchronizing, loading or cleaning up files that are not needed anymore.

import threading
import time

path = "text.txt"
text = ""

def readFile():
    global path, Text
    while True:
        with open(path) as file:
            text = file.read()
            time.sleep(3)

def printLoop():
    global text
    for c in range(30):
        print(text)
        time.sleep(1)
    
t1 = threading.Thread(target=readFile, daemon=True)
t2 = threading.Thread(target=printLoop)

#t1.start()
#t2.start()

# Since the ordinary threads are all finished, the program ends and the daemon thread just gets terminated.