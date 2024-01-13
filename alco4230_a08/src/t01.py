"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
from BST_linked import BST

bst = BST()

a = [11, 7, 6, 9, 8, 15, 12, 18]

for i in a:
    bst.insert(i)

print(f"Testing valid:{bst.is_valid()} ")
print()

print(f"Testing balanced: {bst.is_balanced()}")

ScndBST = BST()

for i in [6, 3, 9, 12]:
    ScndBST.insert(i)
print()

print(f"Min: {bst.min()}")
print()

print(f"# nodes with 0 children: {bst.leaf_count()}")
print()

print(f"# nodes with 1 child: {bst.one_child_count()}")
print()

print(f"# nodes with 2 children: {bst.two_child_count()}")
print()

print(f"Ordered values bst: {bst.inorder()}")
print()

print(f"Preordered values bst: {bst.preorder()}")
print()

print(f"Postorder values bst: {bst.postorder()}")
print()

print(f"Levelorder values bst: {bst.levelorder()}")
print()

print(f"Removed Value: {bst.remove(11)}")
print()

print("BST: ")
for i in bst:
    print(f"{i} ", end="")
