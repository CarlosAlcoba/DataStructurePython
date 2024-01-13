"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-17"
-------------------------------------------------------
"""
from Food_utilities import read_foods

fv = open("Foods.txt", "r")

foods = read_foods(fv)

for food in foods:
    print(food)
    print()
