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
# Imports
from Sorts_array import Sorts

print("Testing gnome_sort(Array-based):")

lst = []
a = input("Enter a value to your list(Enter to stop): ")
while a != "":
    lst.append(int(a))
    a = input("Enter a value to your list(Enter to stop): ")
print(f"Original list: {lst}")
Sorts.gnome_sort(lst)
print(f"Sorted list: {lst}")
