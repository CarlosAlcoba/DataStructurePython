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

q = Queue()
q._values = [11, 22, 33, 44, 55]
print("Source: ", q._values)
target1, target2 = q.split_alt()
print("Target1: ", target1._values)
print("target2: ", target2._values)
