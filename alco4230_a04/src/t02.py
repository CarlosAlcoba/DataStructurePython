"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-08"
-------------------------------------------------------
"""
from Queue_array import Queue


a = Queue()
b = Queue()
for i in range(3):
    a.insert(1)

b.insert(1)
a.remove()
a.remove()

equals = a == b
print("Testing for __eq__:")
print("equals:", equals)
