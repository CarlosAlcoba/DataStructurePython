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
from List_linked import List

source = List()

for i in ["A", "B", "C", "D"]:
    source.append(i)


source.reverse_r()
for i in source:
    print(source._front._value)
    source._front = source._front._next
