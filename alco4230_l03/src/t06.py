"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-05-31"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from utilities import pq_to_array, array_to_pq, priority_queue_test
from Food_utilities import read_foods


q = Priority_Queue()
fv = open("Foods.txt", "r")

foods = read_foods(fv)
print(f"Q:{q._values}")
print(f"Array:{foods}")
print()

print("Testing Array to queue")
array_to_pq(q, foods)
print(f"Q:{q._values}")
print(f"Array:{foods}")
print()

print("Testing Queue to array")
pq_to_array(q, foods)
print(f"Q:{q._values}")
print(f"Array:{foods}")


print("Testing queue test method")
priority_queue_test([1, 23, 4])
