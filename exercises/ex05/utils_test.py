"""
This module contains unit tests for the list utility functions defined in utils.py.

_author_ = 730464539
"""

import pytest
from ex05.utils import only_evens, sub, add_at_index


def test_only_evens() -> None:
    """Tests an edge case of the only_evens function."""
    assert only_evens([]) == []


def test_only_evens2() -> None:
    """Tests a use case of the only_evens function."""
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_only_evens3() -> None:
    """Tests a use case of the only_evens function."""
    assert only_evens([1, 3, 5]) == []


def test_sub1() -> None:
    """Tests a use case of the sub function."""
    assert sub([7, 11, 12], 0, 1) == [7, 11]


def test_sub2() -> None:
    """Tests a use case of the sub function"""
    assert sub([1, 2, 3, 4, 5, 6], 3, 5) == [4, 5, 6]


def test_sub3() -> None:
    """Tests an edge case of the sub function"""
    assert sub([], 0, 1) == []


def test_add_at_index3() -> None:
    """Tests a use case of the add_at_index function."""
    assert add_at_index([1, 2, 3], 1, 0) == [1, 1, 2, 3]


def test_add_at_index2() -> None:
    """Tests a use case of the add_at_index function."""
    assert add_at_index([1, 2, 3], 10, 2) == [1, 2, 10, 3]


def test_add_at_index_raises_indexerror():
    """Tests an edge case of the add_at_index function."""
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3], 10, 10)
