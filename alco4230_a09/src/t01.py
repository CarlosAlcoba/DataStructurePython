"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-07-20"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_array import Hash_Set
fv = open("otoos610.txt", "r")
hash_set = Hash_Set(20)
insert_words(fv, hash_set)

total, max_word = comparison_total(hash_set)

print("Using array-based list Hash_Set")
print()
print(f"Total Comparisons: {total:,}")
print(
    f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,}")
