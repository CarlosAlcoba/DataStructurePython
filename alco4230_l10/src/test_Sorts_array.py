"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2023-07-19"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts
from random import randint

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []

    for i in range(SIZE):
        values.append(Number(i))

    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    values = []

    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    arrays = []
    columns = []
    for row in range(TESTS):
        for column in range(SIZE):
            columns.append(Number(randint(0, XRANGE)))
        arrays.append(columns)
        columns = []
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    order = create_sorted()
    reversed_list = create_reversed()
    random_order = create_randoms()

    # Ordered List
    Number.comparisons = 0
    Sorts.swaps = 0
    func(order)
    order_comp = round(Number.comparisons, 0)
    order_swaps = round(Sorts.swaps, 0)

    # Reversed List
    Number.comparisons = 0
    Sorts.swaps = 0
    func(reversed_list)
    reversed_comp = round(Number.comparisons, 0)
    reversed_swaps = round(Sorts.swaps, 0)

    # Random List
    Number.comparisons = 0
    Sorts.swaps = 0
    func(random_order)
    random_comp = round(Number.comparisons, 0)
    random_swaps = round(Sorts.swaps, 0)

    print(f"{title:14} {order_comp:8} {reversed_comp:8} {random_comp:8} {order_swaps:8} {reversed_swaps:8} {random_swaps:8}")

    return
