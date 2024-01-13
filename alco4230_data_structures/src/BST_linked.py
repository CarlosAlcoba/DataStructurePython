"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-07-20"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._value
            self._count -= 1
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.
                node = None

            elif node._left is None:
                # node has no left child.

                node = node._right

            elif node._right is None:
                # node has no right child.

                node = node._left

            else:
                # Node has two children
                repl_node = self._delete_node_left(node._left)
                repl_node._left = node._left
                repl_node._right = node._right
                node = repl_node

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """
        child = parent._right
        while child._right is not None:
            parent = child
            child = child._right
        if child._left is not None:
            parent.right = child._left
        else:
            parent.right = None
        repl_node = child

        return repl_node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """

        return self.retrieve(key) is not None

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """

        # your code here

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are equal.
        Values in self and target are compared and if all values are equal
        and in the same location, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a bst (BST)
        Returns:
            equals - True if source contains the same values
                as target in the same location, otherwise False. (boolean)
        -------------------------------------------------------
        """
        equals = self._count == target._count

        if equals:
            equals = self._eq_aux(self._root, target._root)
        return equals

    def _eq_aux(self, nodeS, nodeT):

        if nodeS is None and nodeT is None:
            equals = True
        elif nodeS is not None and nodeT is not None:
            equals = self._eq_aux(nodeS._left, nodeT._left)
            if equals:
                equals = self._eq_aux(nodeS._right, nodeT._right)
        else:
            equals = False

        return equals

    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"
        parent = None
        current = self._root

        while current is not None and current._value != key:
            parent = current
            if current._value > key:
                current = current._left
            else:
                current = current._right
        if parent is not None:
            value = deepcopy(parent._value)
        else:
            value = None

        return value

    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        value = self._parent_r_aux(self._root, key, None)
        return value

    def _parent_r_aux(self, current, key, parent):

        if current is None:
            value = None
        elif current._value > key:
            value = self._parent_r_aux(current._left, key, current)
        elif current._value < key:
            value = self._parent_r_aux(current._right, key, current)
        elif parent is None:
            value = None
        else:
            value = deepcopy(parent._value)

        return value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"
        value = self._root._value
        return value

    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        # your code here

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"
        value = self._root
        while value._left is not None:
            value = value._left

        return value._value

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        # your code here

    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        if self._count == 0:
            count = 0
        else:
            count = self._leaf_count_aux(self._root)
        return count

    def _leaf_count_aux(self, node):

        if node._left is None and node._right is None:
            count = 1
        elif node._left is None and node._right is not None:
            count = self._leaf_count_aux(node._right)
        elif node._right is None and node._left is not None:
            count = self._leaf_count_aux(node._left)
        else:
            count = self._leaf_count_aux(
                node._left) + self._leaf_count_aux(node._right)

        return count

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        count = self._two_child_count_aux(self._root)
        return count

    def _two_child_count_aux(self, node):

        if node is None:
            count = 0
        elif node._left is not None and node._right is not None:
            count = 1 + self._two_child_count_aux(
                node._left) + self._two_child_count_aux(node._right)
        else:
            count = self._two_child_count_aux(
                node._left) + self._two_child_count_aux(node._right)

        return count

    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        count = self._one_child_count_aux(self._root)
        return count

    def _one_child_count_aux(self, node):

        if node is None:
            count = 0
        elif node._left is None and node._right is not None:
            count = 1 + self._one_child_count_aux(node._right)
        elif node._right is None and node._left is not None:
            count = 1 + self._one_child_count_aux(node._left)
        else:
            count = self._one_child_count_aux(
                node._left) + self._one_child_count_aux(node._right)

        return count

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """

        zero, one, two = self._node_counts_aux(self._root)

        return zero, one, two

    def _node_counts_aux(self, node):

        if node is None:
            # No node
            zero = 0
            one = 0
            two = 0

        elif node._left is None and node._right is None:
            # no children
            zero = 1
            one = 0
            two = 0
        elif node._left is None and node._right is not None:
            # One right child
            zero, one, two = self._node_counts_aux(node._right)
            one += 1
        elif node._left is not None and node._right is None:
            # One left child
            zero, one, two = self._node_counts_aux(node._left)
            one += 1
        else:
            # two children
            left_zero, left_one, left_two = self._node_counts_aux(node._left)
            right_zero, right_one, right_two = self._node_counts_aux(
                node._right)

            zero = left_zero + right_zero
            one = left_one + right_one
            two = 1 + left_two + right_two

        return zero, one, two

    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if self._count == 0:
            balanced = True
        else:
            balanced, _ = self._is_balanced_aux(self._root)

        return balanced

    def _is_balanced_aux(self, node):

        if node._height == 1:
            balanced = True
            height = 1
        else:
            l_height = 0
            r_height = 0
            if node._left is not None:
                balanced, l_height = self._is_balanced_aux(node._left)
            if node._right is not None:
                balanced, r_height = self._is_balanced_aux(node._right)
            if abs(l_height - r_height) > 1:
                balanced = False

            height = 1 + (l_height if l_height > r_height else r_height)

        return balanced, height

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """

        # your code here

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if self._count == 0:
            valid = True
        else:
            valid = self._is_valid_aux(self._root)
        return valid

    def _is_valid_aux(self, node):

        if node is None:
            valid = True
        elif node._left is not None and node._left._value > node._value:
            valid = False
        elif node._right is not None and node._right._value < node._value:
            valid = False
        else:
            if self._node_height(node) == 1 + self._node_height(node._left) or self._node_height(node) == 1 + self._node_height(node._right):
                valid = self._is_valid_aux(node._left)
                if valid:
                    self._is_valid_aux(node._right)
            else:
                valid = False
        return valid

    def update(self, value, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Iterative algorithm.)
        --------------------------------------------------------- -
        """

        # your code here

    def update_r(self, key, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Recursive algorithm.)
        --------------------------------------------------------- -
        """

        # your code here

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        if self._root is not None:
            a = self._inorder_aux(self._root, a)
        return a

    def _inorder_aux(self, node, a):

        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(node._value)
            self._inorder_aux(node._right, a)
        return a

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        if self._root is not None:
            a = self._preorder_aux(self._root, a)
        return a

    def _preorder_aux(self, node, a):
        if node is not None:
            a.append(node._value)
            self._preorder_aux(node._left, a)
            self._preorder_aux(node._right, a)
        return a

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        if self._root is not None:
            a = self._postorder_aux(self._root, a)
        return a

    def _postorder_aux(self, node, a):
        if node is not None:
            self._postorder_aux(node._left, a)
            self._postorder_aux(node._right, a)
            a.append(node._value)
        return a

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """

        values = []
        if self._root is not None:
            queue = []
            queue.append(self._root)
            while len(queue) > 0:
                node = queue.pop(0)
                values.append(node._value)
                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
        return values

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """

        # your code here
