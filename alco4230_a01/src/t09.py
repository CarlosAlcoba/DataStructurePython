"""
-------------------------------------------------------
[t09]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-16"
-------------------------------------------------------
"""
from functions import substitute

string = str(input("Input a string:"))
ciphertext = str(input("Input a CipherText:"))

estring = substitute(string, ciphertext)

print(estring)
