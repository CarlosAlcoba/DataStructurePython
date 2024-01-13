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

x = [11, 22, 33, 44]
lst = List()

for i in x:
    lst.append(i)

target1, target2 = lst.split_alt_r()


for i in target1:
    print(target1._front._value)
    target1._front = target1._front._next
