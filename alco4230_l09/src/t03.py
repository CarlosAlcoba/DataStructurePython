"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-12"
-------------------------------------------------------
"""
from Food_utilities import read_foods
from Hash_Set_array import Hash_Set

fv = open("Foods.txt", "r")
values = read_foods(fv)

hs = Hash_Set(7)
for i in values:
    hs.insert(i)

hs.debug()
