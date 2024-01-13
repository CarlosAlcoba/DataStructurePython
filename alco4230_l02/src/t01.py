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

stack = Stack()

if stack.is_empty():
    print("Empty stack")
else:
    print("Non-empty Stack")

stack.push(3)
print("3 pushed into the stack")

value = stack.pop()

print(f"Value popped from stack : {value}")

stack.push(5)
value = stack.peek()
print(f"Last value added to stack: {value}")
