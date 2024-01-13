"""
-------------------------------------------------------
[t04]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-16"
-------------------------------------------------------
"""
from functions import is_palindrome


string = str(input("Enter a string: "))
print(f"string: {string}")
palindrome = is_palindrome(string)

print(f"Palindrome: {palindrome}")
