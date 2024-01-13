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
from Food_utilities import food_search, read_foods

fv = open("Foods.txt", "r")

foods = read_foods(fv)

origin = int(input("Origin:"))
max_cals = int(input("Max cals:"))
is_veg = input("is veg(Y/N):")
if is_veg == "Y":
    is_veg = True
else:
    is_veg = False
print()
result = food_search(foods, origin, max_cals, is_veg)

for i in result:
    print(i)
    print()
