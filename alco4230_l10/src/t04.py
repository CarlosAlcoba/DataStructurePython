"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-19"
-------------------------------------------------------
"""
from test_Sorts_List_linked import test_sort, SORTS
print('n:   100       |      Comparisons       | |         Swaps          |')
print('Algorithm      In Order Reversed   Random In Order Reversed   R')
print("-------------- -------- -------- -------- -------- -------- --------")
for sort in SORTS:
    test_sort(sort[0], sort[1])
