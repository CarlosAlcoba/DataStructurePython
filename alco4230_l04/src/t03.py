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

lst.insert(0, 3)
print(f"length of lst after insert method: {len(lst)}")
lst.append(4)
print(f"length of lst after append method: {len(lst)}")
lst.remove(4)
print(f"length of lst after remove method: {len(lst)}")
