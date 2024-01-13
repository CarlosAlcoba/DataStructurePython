"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-08"
-------------------------------------------------------
"""
# Imports
from utilities import list_test
from Food_utilities import read_foods


fv = open("foods.txt", "r")

source = read_foods(fv)

fv.close()

list_test(source)
