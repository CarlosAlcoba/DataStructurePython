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
from functions import is_mirror_stack

string = input("Enter a string: ")
valid_chars = input("Enter the valid chars: ")
m = input("Enter the mirror pivot: ")

mirror = is_mirror_stack(string, valid_chars, m)
print(mirror.value)
