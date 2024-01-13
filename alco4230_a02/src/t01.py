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
from Food_utilities import read_foods, by_origin

fv = open("Foods.txt", "r")

foods = read_foods(fv)

origins = by_origin(foods, 1)

for i in origins:
    print(i)
    print()
