# In Python, queues are structures that take in data in a certain order to then output it in a certain order. The default queue type is the so-called FIFO queue. (First in first out)

import queue

q = queue.Queue()

#for x in range(5, 10):
#    q.put(x)

# The put function adds an element to the queue that can then be extracted by the get function.

#for x in range(5):
#    print(q.get(x))

#  Queuing resources

import threading
import queue
import math

q = queue.Queue()
threads = []

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(math.factorial(item))
        q.task_done()


for x in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

zahlen = [134000, 14, 5, 300, 98, 88, 11, 23]

for item in zahlen:
    q.put(item)

q.join()

for i in range(5):
    q.put(None)


