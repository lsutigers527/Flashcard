"""
This File Contains Various Functions for Handling User Input
"""

from flashcard_main import db_handling, flashcard_logic


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


def flashcard_input() -> dict:
    # TODO Flashcard Input - Use Dataclass from flashcard_logic

    # Input and Insert Back into Dict
    print("Please Enter The Language: ")
    language: str = basic_input_str(prompt="Language")

    # TODO Handling for categories input
    print("Please Enter the Categories (If multiple separate by comma)")
    categories = []

    print("Please Enter the Word.")
    word: str = basic_input_str(prompt="Word")

    print("Enter the Pronunciation")
    pronunciation: str = basic_input_str(prompt="Pronunciation")

    print("Enter the Translation")
    translation: str = basic_input_str(prompt="Translation")

    flashcard: flashcard_logic.Flashcard = flashcard_logic.Flashcard(
        language, categories, word, pronunciation, translation
    )

    print(flashcard)
