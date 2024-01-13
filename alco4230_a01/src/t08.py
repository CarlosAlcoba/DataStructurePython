"""
-------------------------------------------------------
[t08]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-16"
-------------------------------------------------------
"""
from functions import matrixes_add
a = [[0, 1], [2, 3], [4, 5]]
b = [[6, 7], [8, 9], [1, 0]]
print(f"matrix a: {a} ")
print(f"matrix b: {b} ")
c = matrixes_add(a, b)
print(f"matrix c(Sum of a and b): {c}")
