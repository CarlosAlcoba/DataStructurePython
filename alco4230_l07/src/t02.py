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

x = [1, 2, 3]

source = List()
target = List()


for i in [22, 33, 11]:
    source.append(i)
    target.append(i)
print(source.is_identical_r(target))
