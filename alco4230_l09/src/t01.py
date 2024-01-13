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
from functions import hash_table
from Food_utilities import read_foods

fv = open("Foods.txt", "r")
values = read_foods(fv)

hash_table(7, values)
