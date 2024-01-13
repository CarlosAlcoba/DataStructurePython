"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-29"
-------------------------------------------------------
"""
# Imports
from List_linked import List

source = List()


for v in [22, 33, 11, 55, 44]:
    source.insert(2, v)

p, c, i = source._linear_search(11)
print(f"p:{p}")
print(f"c:{c}")
print(f"i:{i}")
