"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-31"
-------------------------------------------------------
"""
from Queue_array import Queue


q = Queue()
print(f"Empty:{q.is_empty()}")
q.insert(3)
print("Insert method: 3")
print(f"Empty:{q.is_empty()}")
