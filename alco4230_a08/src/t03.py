"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-13"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from functions import do_comparisons, letter_table
from Letter import Letter


DATA = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()

for i in DATA:
    letter = Letter(i)
    bst.insert(letter)

fv = open("otoos610.txt", "r")

do_comparisons(fv, bst)

fv.close()

letter_table(bst)
