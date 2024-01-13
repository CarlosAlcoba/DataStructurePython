"""
-------------------------------------------------------
[t06]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-16"
-------------------------------------------------------
"""
from functions import matrix_stats

a = [[1, 2, 3], [4, 5, 6]]
print(f"Matrix : {a}")

small, large, total, average = matrix_stats(a)

print("Small:", small)
print("Large:", large)
print("Total:", total)
print("Average:", average)
