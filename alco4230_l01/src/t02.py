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
from Food import Food

some_food = Food('Ravioli', 7, False, 246)


print("Testing __str__ method:")
s = str(some_food)
print(s)