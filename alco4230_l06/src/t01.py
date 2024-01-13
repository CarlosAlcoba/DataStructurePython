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
# Imports
from List_linked import List

source = List()


for v in [22, 33, 11, 55, 44]:
    source.insert(2, v)


print(source._front._value)
print(source._front._next._value)
print(source._front._next._next._value)
print(source._front._next._next._next._value)
print(source._front._next._next._next._next._value)


source.insert(0, 3)
print(f"length of lst after insert method: {len(source)}")
source.append(4)
print(f"length of lst after append method: {len(source)}")
