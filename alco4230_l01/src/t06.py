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
from Food_utilities import write_foods, read_foods

fv = open("Foods.txt", "r")
foods = read_foods(fv)
nfv = open("New_Foods.txt", "a")
write_foods(nfv, foods)
