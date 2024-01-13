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
from utilities import queue_to_array, array_to_queue, queue_test


q = Queue()
q._values = [11, 22, 33, 44]

foods = []
print(f"Q:{q._values}")
print(f"Array:{foods}")
queue_to_array(q, foods)
print("Testing Queue to array")
print(f"Q:{q._values}")
print(f"Array:{foods}")
print("Testing Array to queue")
array_to_queue(q, foods)
print(f"Q:{q._values}")
print(f"Array:{foods}")
print("Testing queue test method")
queue_test([1, 23, 4])
