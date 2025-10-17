"""
This File Contains Various Functions for Handling User Input
"""

from . import db_handling, flashcard_logic


def basic_input_str(prompt: str) -> str:
    """
    basic_input_str

    Handles basic user input operations

    Args:
        prompt (str): Name of What is Being Entered

    Returns:
        str: The User Input
    """
    user_input: str = input(f"Input {prompt}: ")
    return user_input


def categories_input() -> list:
    categories: list[str] = []

    while True:
        user_input: str = basic_input_str(prompt="Category (or DONE)").strip()

        if user_input.upper() == "DONE":
            print("Categories Input Complete!")
            print(f"Categories: {categories}")
            break

        # Handles blanks though falsy checks
        if user_input:
            categories.append(user_input)

    return categories


def yes_or_no() -> bool:
    # Handles basic Y/N input
    while True:
        user_input: str = basic_input_str(prompt="Y or N").upper()

        if user_input == "Y":
            return True

        elif user_input == "N":
            return False

        else:
            print("Please Enter Y or N")
            continue
