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


source1 = List()
source2 = List()

for i in [22, 33, 11]:
    source2.append(i)
for i in [22, 33, 11, 55, 44]:
    source1.append(i)

target = List()

target.union_r(source1, source2)

for i in target:
    print(target._front._value)
    target._front = target._front._next
