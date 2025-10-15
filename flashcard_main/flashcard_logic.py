"""
Logic For Flash Card Handling
"""

from . import db_handling, input_handling, flashcard_logic
from dataclasses import dataclass, field


@dataclass
class Flashcard:
    # Data Class for Handling Flashcard Data
    language: str
    word: str
    pronunciation: str
    translation: str
    categories: list

    # Idk maybe do all this as flashcards methods?
    def upload_to_db() -> None:
        pass


def new_fc() -> Flashcard:
    # This is the logic for creating a new flashcard

    # Input and Insert Back into Dict
    print("Please Enter The Language: ")
    language: str = input_handling.basic_input_str(prompt="Language")

    # TODO Handling for categories input - Kinda Working See Below TODO About None Return
    print("Please Enter the Categories (Enter Done to Complete)")
    categories: list = input_handling.categories_input()

    print("Please Enter the Word.")
    word: str = input_handling.basic_input_str(prompt="Word")

    print("Enter the Pronunciation")
    pronunciation: str = input_handling.basic_input_str(prompt="Pronunciation")

    print("Enter the Translation")
    translation: str = input_handling.basic_input_str(prompt="Translation")

    flashcard: flashcard_logic.Flashcard = flashcard_logic.Flashcard(
        language, word, pronunciation, translation, categories
    )

    # TODO Why do i get NONE for the categories list
    print(flashcard)
    print(flashcard.categories)
    print(flashcard.language)
    return flashcard
