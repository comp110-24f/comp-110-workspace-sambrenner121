"""Summing the elements of a list using different loops

__author__ = "730464539"
"""


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    out: float = 0.0
    while idx < len(vals):
        out += vals[idx]
        idx += 1
    return out


# Sums the elements of a list using a while loop


def f_sum(vals: list[float]) -> float:
    out: float = 0.0
    for num in vals:
        out += num
    return out


# Sums the elements of a list using a for loop


def f_range_sum(vals: list[float]) -> float:
    out: float = 0.0
    for i in range(0, len(vals), 1):
        out += vals[i]
    return out


# Sums the elements of a list using a for loop within a range
