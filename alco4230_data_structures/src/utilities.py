"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Carlos Henrique Alcoba Pinto
ID:      169044230
Email:   alco4230@mylaurier.ca
__updated__ = "2023-06-08"
-------------------------------------------------------
"""
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    for i in range(len(source)):
        stack.push(source.pop())
    return


def stack_to_array(stack, foods):
    """
    -------------------------------------------------------
    Pops contents of stack into foods. At finish, stack is empty.
    Top value of stack is at end of foods,
    bottom value of stack is at beginning of foods.
    Use: stack_to_array(stack, foods)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        foods - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while stack.is_empty() == False:
        foods.append(stack.pop())
    foods.reverse()
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()

    for i in source:
        stack.push(i)

    if stack.is_empty():
        print(f"is_empty on empty stack: {stack.is_empty()}")
    else:
        print(f"is_empty on stack with data: {stack.is_empty()}")

    i = stack.peek()
    print(f"peek method on stack: i on top of stack: \n {i}")
    i = stack.pop()
    print(f"pop method on stack: i popped from the top of the stack: \n {i}")

    return None


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        queue.insert(source.pop(0))

    return


def queue_to_array(queue, foods):
    """
    -------------------------------------------------------
    Removes contents of queue into foods. At finish, queue is empty.
    Front value of queue is at front of foods,
    rear value of queue is at end of foods.
    Use: queue_to_array(queue, foods)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        foods - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not queue.is_empty():
        foods.append(queue.peek())
        queue.remove()
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand
    print(f"Testing for is_empty method: {q.is_empty()}")
    print(f"Testing for insert method")
    for i in a:
        q.insert(i)
    print(f"Testing for is_empty method: {q.is_empty()}")
    print(f"Testing for peek method: {q.peek()}")
    print(f"Testing for remove method:{q.remove()}")
    print(f"Testing for len method: {len(q)}")
    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in range(len(source)):
        pq.insert(source.pop(0))

    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand
    print(f"Testing for is_empty method: {pq.is_empty()}")
    print(f"Testing for insert method")
    for i in a:
        pq.insert(i)
    print(f"Testing for is_empty method: {pq.is_empty()}")
    print(f"Testing for peek method: {pq.peek()}")
    print(f"Testing for remove method:{pq.remove()}")
    print(f"Testing for len method: {len(pq)}")
    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        llist.append(source.pop(0))
    return None


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(llist) != 0:
        target.append(llist.pop(0))

    return None


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    print(f"Test for is_empty method: {lst.is_empty()}")
    print()
    print(f"Test for insert method:")
    lst.insert(0, source[0])
    print()
    print(f"Test for is_empty method: {lst.is_empty()}")
    print()
    print(f"Test for remove method:")
    lst.remove(source[0])
    print()
    print(f"Test for is_empty method: {lst.is_empty()}")
    print()
    print(f"Test for count method: {lst.count(source[0])}")
    print()
    print(f"Test for append method: {lst.append(source[0])}")
    print()
    print(f"Test for index method: {lst.index(source[0])}")
    print()
    print(f"Test for find method: {lst.find(source[0])}")
    print()
    print(f"Test for max method: {lst.max()}")
    print()
    print(f"Test for min method: {lst.min()}")

    return
