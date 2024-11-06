"""
test file for find_max.py"!"

_author_ = 730464539
"""

from CQs.cq07.find_max import find_and_remove_max


def test_return() -> None:
    assert find_and_remove_max([9, 22, 3, 1, 22, 22]) == 22
    # tests function and returns 1 integer


def test_mutation() -> None:
    test_list: list[int] = [25, 5, 1, 22, 25]
    find_and_remove_max(test_list)
    assert len(test_list) != len([25, 5, 1, 22, 25])
    # ensures that the function removes elements from the list


def test_empty() -> None:
    assert find_and_remove_max([]) == -1
    # tests the input of an empty list and returns -1
