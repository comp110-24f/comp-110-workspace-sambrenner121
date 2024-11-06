"""CQ02 Conditionals

__author__ = "730464539"
"""


def guess_a_number() -> None:
    secret: int = 7
    x = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is 7")
    else:
        print("Your guess was too high! The secret number is 7")

    if __name__ == "__main__":
        guess_a_number()
