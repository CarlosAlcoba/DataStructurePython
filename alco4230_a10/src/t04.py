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
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

print("Testing Gnome Sort(Deque linked list):")

lst = Deque()
a = input("Enter a value to your list(Enter to stop): ")
while a != "":
    lst.insert_rear((int(a)))
    a = input("Enter a value to your list(Enter to stop): ")
print(f"Original list:")
for i in lst:
    print(i, end=" ")
print()
Sorts.gnome_sort(lst)
print(f"Sorted list:")
for i in lst:
    print(i, end=" ")
