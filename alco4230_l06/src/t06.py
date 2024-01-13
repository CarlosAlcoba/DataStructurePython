"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-21"
-------------------------------------------------------
"""
from List_linked import List

lst = List()


for v in [22, 33, 11, 55, 44]:
    lst.insert(2, v)

print(f"Set item testing: 99 to index 2")
lst[2] = 99
print()
print(f"Get item testing: index 2 = {lst[2]}")
print()
