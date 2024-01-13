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
from morse import encode_morse, fill_letter_bst, DATA1
from BST_linked import BST

bst = BST()
fill_letter_bst(bst, DATA1)
text = "This is a string"

code = encode_morse(bst, text)

code = code.strip()
print(code)
