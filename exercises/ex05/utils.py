"""
This module provides utility functions for performing operations on lists of integers.

_author_ = 730464539
"""


def only_evens(my_list: list[int]) -> list[int]:
    """Returns all even integers from the given list."""
    evens: list[int] = []
    for num in my_list:
        if num % 2 == 0:
            evens.append(num)
    return evens


def sub(my_list: list[int], start: int, end: int) -> list[int]:
    """Returns a sub-portion of a list using start and end indices."""
    sub_list: list[int] = []
    if start < 0:
        start = 0
    if end > len(my_list):
        end = len(my_list)
    for idx in range(start, end):
        sub_list.append(my_list[idx])
    return sub_list


def add_at_index(my_list: list[int], val: int, idx: int) -> None:
    """Adds a value at an index in the input list."""
    if idx < 0 or idx > len(my_list):
        raise IndexError("Index is out of bounds for the input list")

    # If the index is equal to the length of the list, we can just append
    if idx == len(my_list):
        my_list.append(val)
        return

    # Add a placeholder at the end of the list to make space for the new value
    my_list.append(val)

    # Move elements one position to the right to create space at the target index.
    for i in range(len(my_list) - 1, idx, -1):
        my_list[1] = my_list[i - 1]
        my_list[idx] = val
