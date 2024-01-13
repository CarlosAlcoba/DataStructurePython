"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-25"
-------------------------------------------------------
"""
# Import
from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()
stack._values = []
source = [1, 23, 4]
array_to_stack(stack, source)
print(stack._values)
