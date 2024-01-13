"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-29"
-------------------------------------------------------
"""
from Queue_linked import Queue

queue = Queue()

print("Testing Queue is empty: ")
print(queue.is_empty())

print()
print("Testing Queue is Full: ")
print(queue.is_full())

print()
print("Length of queue: ")
print(len(queue))

queue.insert(3)

print()
print("Length of queue: ")
print(len(queue))

queue.insert(6)

print()
print("Removed Node: ")
print(queue.remove())

print()
print("Testing Queue peek: ")
print(queue.peek())

q1 = Queue()
q2 = Queue()

q1.insert(9)
q2.combine(queue, q1)

print()
print("Printing q2: ")
for value in q2:
    print(value, end="")

target1, target2 = q2.split_alt()

print()
print("Printing target1: ")
for value in target1:
    print(value)

print()
print("Printing target2: ")
for value in target2:
    print(value)
