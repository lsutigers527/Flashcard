"""
This File Contains Various Functions for Handling User Input
"""

from . import db_handling


def basic_input_str() -> str:
    # This is a basic input function that will return a string
    user_input: str = input(f"Input: ")
    return user_input


def flashcard_input() -> dict:
    # TODO Flashcard Input
    flashcard: dict = {
        "language": "",
        "categories": [],
        "word": "",
        "pronunciation": "",
        "translation": "",
    }


def choose_mode_input() -> int:
    # Input handling for modes.choose_mode()
    while True:
        user_input: str = basic_input_str()
        try:
            choice: int = int(user_input)
            break
        except:
            print("Please Only Enter the Number For Your Choice")
    return choice
