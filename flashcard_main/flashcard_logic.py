"""
Logic For Flash Card Handling
"""

from . import db_handling, input_handling, flashcard_logic, flashcards_utility
from dataclasses import dataclass, field


@dataclass
class Flashcard:
    # Data Class for Handling Flashcard Data
    language: str
    word: str
    pronunciation: str
    translation: str
    categories: list[str]

    # Idk maybe do all this as flashcards methods?
    def upload_to_db() -> None:
        pass

    # String Print of FC Obj
    def __str__(self):
        return (
            f"Language: {self.language}\n"
            f"Word: {self.word}\n"
            f"Pronunciation: {self.pronunciation}\n"
            f"Translation: {self.translation}\n"
            f"Categories: {self.categories}"
        )


def new_fc() -> Flashcard:
    # This is the logic for creating a new flashcard

    # Input Flashcard Info
    print("Please Enter The Language: ")
    language: str = input_handling.basic_input_str(prompt="Language")

    print("Please Enter the Categories (Enter Done to Complete)")
    categories: list = input_handling.categories_input()

    print("Please Enter the Word.")
    word: str = input_handling.basic_input_str(prompt="Word")

    print("Enter the Pronunciation")
    pronunciation: str = input_handling.basic_input_str(prompt="Pronunciation")

    print("Enter the Translation")
    translation: str = input_handling.basic_input_str(prompt="Translation")

    # Create Flashcard Object
    flashcard: flashcard_logic.Flashcard = flashcard_logic.Flashcard(
        language, word, pronunciation, translation, categories
    )

    # Clear Console Before info check
    flashcards_utility.clear_console()

    # TODO Info Check Here before return
    fc_check_info(flashcard)

    # Return Flashcard Obj
    return flashcard


def fc_check_info(flashcard: Flashcard) -> None:
    # TODO Check info logic
    print(flashcard)
    print("Does this Look Correct?")

    correct: bool = input_handling.yes_or_no()


def edit_fc(flashcard: Flashcard) -> Flashcard:
    # TODO Edit Logic
    pass
