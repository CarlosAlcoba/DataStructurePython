"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-05"
-------------------------------------------------------
"""
from morse import decode_morse, fill_code_bst, DATA1
from BST_linked import BST


bst = BST()
fill_code_bst(bst, DATA1)
code = """-.. .- ...- .. -.."""

text = decode_morse(bst, code)
print(text)
