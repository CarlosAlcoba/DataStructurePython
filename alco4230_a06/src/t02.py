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
from Priority_Queue_linked import Priority_Queue

queue = Priority_Queue()

print("Testing Queue is empty: ")
print(queue.is_empty())

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
print("Testing priority Queue peek: ")
print(queue.peek())

q1 = Priority_Queue()
q2 = Priority_Queue()

q1.insert(9)

q2.combine(queue, q1)

print()
print("Printing q2: ")
for value in q2:
    print(value)

target1, target2 = q2.split_alt()

print()
print("Printing target1: ")
for value in target1:
    print(value)

print()
print("Printing target2: ")
for value in target2:
    print(value)

q2.insert(3)

q2.insert(6)

q2.insert(9)

q2.insert(12)

target3, target4 = q2.split_key(6)

print()
print("Printing target1: ")
for value in target3:
    print(value)

print()
print("Printing target2: ")
for value in target4:
    print(value)
