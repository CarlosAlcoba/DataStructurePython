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
from functions import queue_split_alt
from Queue_array import Queue

source = Queue()
source._values = [11, 22, 33, 44, 55]

target1, target2 = queue_split_alt(source)

print(target1._values)
print(target2._values)
