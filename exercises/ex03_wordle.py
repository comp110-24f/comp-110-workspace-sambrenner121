"""EX03 - Wordle - Guess the five letter word!"""

__author__ = "730464539"


def input_guess(secret_word_len: int) -> str:
    """Prompt the user to input a guess of the correct length."""
    guess: str = input(f"Enter a {secret_word_len} character word: ")

    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess


# Prompts the user to guess a word, prints the prompt and returns the user input


def contains_char(word: str, char_guess: str) -> bool:
    """Check if a character is present in the word."""
    assert len(char_guess) == 1  # Ensure char_guess is a single character

    i: int = 0
    while i < len(word):
        if word[i] == char_guess:
            return True
        i += 1

    return False


# Checks if the letter is present in the secret word


def emojified(guess: str, secret: str) -> str:
    """Returns emoji feedback for each character in the guess."""
    assert len(guess) == len(secret)  # Ensure guess and secret are of equal length

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_str: str = ""

    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji_str += GREEN_BOX
        elif contains_char(secret, guess[i]):
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX
        i += 1

    return emoji_str


# Creates the emoji output to determine the placement of each letter
# and whether it is present in the secret word and where


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    max_turns: int = 6

    while turns <= max_turns:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turns}/{max_turns} turns!")
            turns = 7
        elif turns == 6:
            print(f"X/{max_turns} - Sorry, try again tomorrow!")
        turns += 1


# Runs the game loop, ensuring each guess is the correct number of letters
# and allows the user to make progress in the game.


if __name__ == "__main__":
    main(secret="codes")
