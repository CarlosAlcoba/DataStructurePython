"""
-------------------------------------------------------
[t03]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-16"
-------------------------------------------------------
"""
from functions import file_analyze

fv = open("test.txt", "r")

u, l, d, w, r = file_analyze(fv)
fv.close()
print(f"u: {u}")
print(f"l: {l}")
print(f"d: {d}")
print(f"w: {w}")
print(f"r: {r}")
