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
# Imports
from functions import stack_combine
from Stack_array import Stack

source1 = Stack()
source1._values = [8, 12, 8, 5]

source2 = Stack()
source2._values = [14, 9, 7, 1, 6, 3]


target = stack_combine(source1, source2)
print("Target:")
for i in target:
    print(i)
