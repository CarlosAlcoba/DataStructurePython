"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-06"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List
from Food_utilities import read_foods
from utilities import list_test

file = open('foods.txt', 'r', encoding="utf-8")

foods = read_foods(file)

list_test(foods)
