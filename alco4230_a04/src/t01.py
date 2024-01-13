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
from Queue_circular import Queue

q = Queue()
a = Queue()


for i in range(8):
    a.insert(1)
    q.insert(1)
a.insert(2)
q.insert(3)
equals = q == a

print("Testing for __eq__:")
print("equals:", equals)
