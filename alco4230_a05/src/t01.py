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
from List_array import List

t = List()
s = List()
d = List()
d._values = [1, 2, 2, 3, 4, 4, 5, 5]
print('testing __eq__:', t == s)
print('testing append: 3')
t.append(3)
print('testing __eq__:', t == s)
print(f"testing clean method:")
print(d._values)
d.clean()
print(d._values)
print(f"testing combine method:")
d.combine(s, t)
print(d._values)
print('testing prepend: 3')
t.prepend(3)
print(f"testing intersection method:")
s.intersection(d, t)
print(s._values)
print(f"testing remove_front method:")
d.remove_front()
print(d._values)
print(f"testing remove many method:")
d.remove_many(3)
print(d._values)
target1, target2 = d.split()
print('Testing split method:')
print(target1._values)
print(target2._values)
t._values = [1, 2, 3, 4, 5]
target1, target2 = t.split_alt()
print('Testing split alt method:')
print(target1._values)
print(target2._values)
print("testing union method:")
d.union(target2, target1)
print(d._values)
print("testing getitem method:", d[2])
