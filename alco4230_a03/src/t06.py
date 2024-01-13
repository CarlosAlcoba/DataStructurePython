"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-01"
-------------------------------------------------------
"""
# Imports
from functions import reroute

opstring = "SSSSXXXX"
values_in = [1, 2, 3, 4]
values_out = reroute(opstring, values_in)
print(f"Opstring: {opstring}")
print(f"Order: {values_in}")
print(f"New order: {values_out}")
