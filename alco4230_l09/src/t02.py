"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-12"
-------------------------------------------------------
"""
# Imports
from Hash_Set_array import Hash_Set

hs = Hash_Set(7)

print(f"Testing insert: {hs.insert(2)}")
print(f"len: {len(hs)}")
print(f"Testing remove: {hs.remove(2)}")
print(f"len: {len(hs)}")
