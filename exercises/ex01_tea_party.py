"""Let's Plan a Tea Party!"""

__author__ = "730464539"


def main_planner(guests: int) -> None:
    """Main function determining supplies for the party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


# this is writing the script for what the program will show as text
# and providing variable names for the calculated values


def tea_bags(people: int) -> int:
    "Provides total number of tea bags"
    return people * 2


def treats(people: int) -> int:
    "Provides total number of treats"
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    "Calculates total cost of the party"
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
