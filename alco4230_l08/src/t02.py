"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-05"
-------------------------------------------------------
"""
from morse import ByCode

a = ByCode(None, "---")
b = ByCode(None, "---")

print(f"B: {b}")
print(f"A: {a}")
print("Comparing A and B")
print(f"Equal: {a == b}")
print(f"A < B: {a < b}")
print(f"A <= B: {a <= b}")
