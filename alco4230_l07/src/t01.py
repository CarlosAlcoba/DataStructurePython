"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-28"
-------------------------------------------------------
"""
# Imports
from List_linked import List


source = List()


for i in [22, 33, 11]:
    source.append(i)

previous, current, index = source._linear_search_r(11)
print(previous, current, index)
