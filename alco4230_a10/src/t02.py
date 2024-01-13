"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-27"
-------------------------------------------------------
"""
from Sorts_List_linked import Sorts
from List_linked import List, _List_Node
a = List()
print("original")
for i in [13, 1, 12, 10, 7, 43, 105, 52, 23, 9]:
    a.append(i)
    print(i, end=" ")
print()
Sorts.radix_sort(a)
print("radix sort:")
for i in a:
    print(i, end=" ")
