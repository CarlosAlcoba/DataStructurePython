"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author: Carlos Alcoba Pinto
ID:     169044230
Email:  alco4230@mylaurier.ca
__updated__ = "2023-06-21"
-------------------------------------------------------
"""
from List_array import List
from Queue_array import Queue


def list_spin(source, n):
    """
    -------------------------------------------------------
    Rotates position of elements in source by n positions to the left.
    Use: source.spin(n)
    Use: list_spin(source, n)
    -------------------------------------------------------
    Parameters:
        source - the List to rotate (List)
        n - amount to rotate contents of List (int)
    Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌​​​​​‌‌​:
        None
    -------------------------------------------------------
    Examples:
        source: [0, 1, 2, 3, 4, 5], list_spin(source, 3), source: [3, 4, 5, 0, 1, 2]
        source: [0, 1, 2, 3, 4, 5], list_spin(source, -1), source: [5, 0, 1, 2, 3, 4]
    -------------------------------------------------------
    """
    i = 0
    while i + n < len(source) - 1:
        x = source.pop(i - n)
        source.insert(i, x)
        i += 1

    return


def thread_packets(threads):
    """
    -------------------------------------------------------
    Combines multiple queues into one queue where values
    in resulting queue are in order from minimum to maximum.
    Use: packets = thread_packets(threads)
    -------------------------------------------------------
    Parameters:
        threads - a list of queues to process (list of Queue)
    Returns‌​‌​​​​‌​​‌‌​‌‌​‌​​‌​​​​​‌‌​:
        packets - a Queue (Queue)
    -------------------------------------------------------
    """

    return
