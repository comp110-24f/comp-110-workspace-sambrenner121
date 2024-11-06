"""CQ05 Mutating Functions

__author__ = "730464539"
"""


def manual_append(a_list: list[int], item: int) -> None:
    """Appends an item to the list."""
    a_list.append(item)


def double(a_list: list[int]) -> None:
    """Doubles each element in the list."""
    i: int = 0
    while i < len(a_list):
        a_list[i] *= 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # list_2 refers to the same list as list_1

double(list_2)

print(
    list_1
)  # Since list_2 and list_1 point to the same object, this will print: [2, 4, 6]
print(list_2)  # This will also print: [2, 4, 6]
