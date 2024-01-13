"""
-------------------------------------------------------
[t07]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-16"
-------------------------------------------------------
"""
from functions import matrix_flatten

a = [["a", "b"], ["x", "z"], ["e", "f"]]
print(f"Original matrix : {a}")

flat_matrix = matrix_flatten(a)

print("Flat matrix:", flat_matrix)
