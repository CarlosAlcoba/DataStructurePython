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
from Hash_Set_array import Hash_Set


hs = Hash_Set(7)

print(f"Testing rehash method, current capacity:{hs._capacity}")
hs._rehash()
print(f"New capacity: {hs._capacity}")
