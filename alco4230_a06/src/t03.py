"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-30"
-------------------------------------------------------
"""
from Deque_linked import Deque

q = Deque()

print("Testing Queue is empty: ")
print(q.is_empty())

q.insert_front(3)

q.insert_rear(6)

print()
print("Testing Length of q: ")
print(len(q))

print()
print("Front value: ")
print(q.peek_front())

print()
print("Rear value: ")
print(q.peek_rear())

print()
print("Value Removed: ")
print(q.remove_front())

print()
print("Value Removed: ")
print(q.remove_rear())

q.insert_front(3)

q.insert_rear(6)

q.insert_rear(9)

q.insert_rear(12)

q._swap(q._rear, q._front)

print()
print("Values in q: ")
for value in q:
    print(value)
