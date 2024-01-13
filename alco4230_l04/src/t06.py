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
from utilities import array_to_list, list_to_array

array = [1, 2, 3]
llist = List()

array_to_list(llist, array)
for i in llist:
    print(i)
list_to_array(llist, array)

print(array)
