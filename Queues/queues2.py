# Lifo queues 
# That stands for last in first out. You can imagine this queue like some sort of stack. The element you put last on top of the stack is the first that you can get from it.

import queue

q = queue.LifoQueue()
numbers = [1, 2, 3, 4, 5]
for x in numbers:
    q.put(x)
while not q.empty():
    print(q.get())

# Prioritizing queues 

q = queue.PriorityQueue()
q.put((8, "Some string"))
q.put((1, 2023))
q.put((90, True))
q.put((2, 10.23))
while not q.empty():
    print(q.get()) # Or q.get()[1] to access only the actual value



