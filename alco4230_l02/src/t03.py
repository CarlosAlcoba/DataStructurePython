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
from Stack_array import Stack
from utilities import stack_to_array

stack = Stack()
stack._values = [1, 2, 3]
foods = []

stack_to_array(stack, foods)

print(f"Target: {foods}")
