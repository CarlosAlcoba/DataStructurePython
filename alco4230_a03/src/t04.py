"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-01"
-------------------------------------------------------
"""
from Stack_array import Stack

source1 = Stack()
source1._values = [8, 12, 7, 5]
print("source")
for i in source1:
    print(i)

source1.reverse()
print("reversed source")
for i in source1:
    print(i)
