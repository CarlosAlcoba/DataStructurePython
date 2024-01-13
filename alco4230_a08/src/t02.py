"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-13"
-------------------------------------------------------
"""
from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total


bst1 = BST()
bst2 = BST()
bst3 = BST()

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

for i in DATA1:
    letter = Letter(i)
    bst1.insert(letter)
for i in DATA2:
    letter = Letter(i)
    bst2.insert(letter)
for i in DATA3:
    letter = Letter(i)
    bst3.insert(letter)

fv = open("otoos610.txt", "r")

do_comparisons(fv, bst1)

total = comparison_total(bst1)

fv.close()

print(f"Comparing by order: {DATA1}")
print(f"Total Comparisons:  {total:,}")


fv = open("otoos610.txt", "r")

do_comparisons(fv, bst2)

total = comparison_total(bst2)

fv.close()

print()
print(f"Comparing by order: {DATA2}")
print(f"Total Comparisons:  {total:,}")

fv = open("otoos610.txt", "r")

do_comparisons(fv, bst3)

total = comparison_total(bst3)

fv.close()

print()
print(f"Comparing by order: {DATA3}")
print(f"Total Comparisons:  {total:,}")
