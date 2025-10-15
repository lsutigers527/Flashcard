"""
This File Contains Various Functions for Handling User Input
"""

from . import db_handling


def basic_input_str(prompt: str) -> str:
    # TODO Maybe add to print statement what is being input
    # This is a basic input function that will return a string
    user_input: str = input(f"Input {prompt}: ")
    return user_input


def flashcard_input() -> dict:
    # TODO Flashcard Input - Use Dataclass from flashcard_logic
    flashcard: dict = {
        "language": "",
        "categories": [],
        "word": "",
        "pronunciation": "",
        "translation": "",
    }

    # TODO Need to Clean up this input handling could be much more elegant
    # Input and Insert Back into Dict
    print("Please Enter The Language: ")
    flashcard["language"] = basic_input_str(prompt="Language")

    # TODO Create Handling Function For List Input
    print("Please Enter the Categories (If multiple separate by comma)")
    # flashcard["categories"] =  Will have to create a list input function and process it

    print("Please Enter the Word.")
    flashcard["word"] = basic_input_str(prompt="Word")

    print("Enter the Pronunciation")
    flashcard["pronunciation"] = basic_input_str(prompt="Pronunciation")

    print("Enter the Translation")
    flashcard["translation"] = basic_input_str(prompt="Translation")
