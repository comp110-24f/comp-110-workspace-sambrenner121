"""
Function that searches and removes all of the largest values in a list

_author_ = 730464539
"""


def find_and_remove_max(input_list: list[int]) -> int:
    max: int = -1
    index: int = 0
    for element in input_list:
        if element > max:
            max = element
    while index < len(input_list):
        if max == input_list[index]:
            input_list.pop(index)
            index -= 1
        index += 1
    return max
