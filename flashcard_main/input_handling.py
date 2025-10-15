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
    categories: list = []

    while True:
        input: str = basic_input_str(prompt="Category (or DONE)")

        if input.upper().strip() == "DONE":
            print("Categories Input Complete!")
            print(f"Categories: {categories}")
            break

        elif input.strip() == "":
            continue

        else:
            categories.append(input)
            continue
