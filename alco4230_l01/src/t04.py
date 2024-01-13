
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
from Food_utilities import read_food
from Food import Food

line = "Spanakopita|5|True|260"
source = read_food(line)
print(type(source))
print(source)
