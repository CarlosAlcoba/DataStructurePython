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
from List_array import List

lst = List()

for i in [1, 2, 3, 4, 3, 6]:
    lst.append(i)

print(f"Index of 3 in lst: {lst.index(3)}")
print()
print(f"Testing for Find method: {lst.find(1)}")
print()
print(f"Testing for __contains__: {lst.__contains__(8)}")
print()
print(f"Testing for count with 3 as key: {lst.count(3)}")
print()
print(f"Testing for max and min: Max-> {lst.max()}, Min->{lst.min()}")
