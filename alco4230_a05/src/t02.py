"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-15"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List

a = Sorted_List()
a._values = [1, 1, 3, 4, 5, ]
b = Sorted_List()
b._values = [6, 7, 8, 9]
print(f"a = {a._values}")
print(f"b = {b._values}")
print(f"Testing for __contains__ method: Contains 3: {a.__contains__(3)}")
print("")
print(f"Testing for __eq__ between list a and b: {a.__eq__(b)}")
print("")

print(f"Testing for __getitem__: {a[3]})")
print("")

print(f"Testing for count: 1 in a = {a.count(1)}")
print("")
a.clean()
print(f"Testing for clean: a = {a._values}")
print("")

print(f"Testing for find:6 in a = {a.find(6)}")
print("")

print(f"Testing for index: index of 3 in a = {a.index(3)}")
print("")

source1 = Sorted_List()
source2 = Sorted_List()
source1._values = [10, 11]
source2._values = [12, 11]
print(f"source1 = {source1._values}")
print(f"source2 = {source2._values}")
a.intersection(source1, source2)
print(f"Testing for intersection: a = {a._values}")
print("")

print(f"Testing for max and min in b: Max: {b.max()}, Min:{b.min()}")
print("")

print(f"Testing for peek method in a: {a.peek()}")
print("")

a.remove(a.peek())
print(f"Testing for remove: a = {a._values}")
print("")

b.remove_front()
print(f"Testing for remove front: b = {b._values}")
print("")

a.insert(11)
print(f"Testing for insert: a = {a._values}")
print("")

a.remove_many(11)
print(f"Testing for remove_many: a = {a._values}")
print("")

target1, target2 = a.split()
print(f"Testing for split:")
print(f"target1 = {target1._values}, target2 = {target2._values}")
print("")

target1, target2 = b.split_alt()
print(f"Testing for split_alt:")
print(f"target1 = {target1._values}, target2 = {target2._values}")
print("")

a.union(source1, source2)
print(f"Testing for union: a = {a._values}")
print("")

target1, target2 = a.split_key(11)
print(f"Testing for split_key: key = 11")
print(f"target1 = {target1._values}, target2 = {target2._values}")
