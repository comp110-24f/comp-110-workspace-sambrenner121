"""EX02 - Chardle - A cute step towards Wordle"""

__author__ = "730464539"


def input_word() -> str:
    """Prompts the user to enter a 5-character word."""
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # Exits program if users types a word that is not 5 letters.
    return word  # Returns the word that the user input.


def input_letter() -> str:
    """Prompts the user to enter a single character."""
    letter = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # Exits program if users types a word that is not 5 letters.
    return letter  # Returns the letter that the user input.


def contains_char(word: str, letter: str) -> None:
    """Searches for the given letter in the word. Prints the index of
    each match and counts the total instances found."""
    print(f"Searching for {letter} in {word}")
    match_count = 0

    # Check for the letter at index 0.
    if word[0] == letter:
        print(f"{letter}found at index 0")
        match_count += 1

    # Check for the letter at index 1.
    if word[1] == letter:
        print(f"{letter}found at index 1")
        match_count += 1

    # Check for the letter at index 2.
    if word[2] == letter:
        print(f"{letter}found at index 2")
        match_count += 1

    # Check for the letter at index 3.
    if word[3] == letter:
        print(f"{letter}found at index 3")
        match_count += 1

    # Check for the letter at index 4.
    if word[4] == letter:
        print(f"{letter}found at index 4")
        match_count += 1

    # Prints instances of the letter.
    if match_count == 0:
        print(f"No instances of {letter} found in {word}")
    elif match_count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{match_count} instances of {letter} found in {word}")


def main() -> None:
    """
    Main function to run the word-matching game.
    Gathers user inputs and checks for matches between word and character.
    """
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
