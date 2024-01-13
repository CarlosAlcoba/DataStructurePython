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
from Food_utilities import calories_by_origin, read_foods

fv = open("Foods.txt", "r")

foods = read_foods(fv)


avg = calories_by_origin(foods, 1)
print(f"Average calories: {avg}")
