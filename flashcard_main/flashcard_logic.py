"""
Logic For Flash Card Handling
"""

from . import db_handling, input_handling
from dataclasses import dataclass


@dataclass
class Flashcard:
    # Data Class for Handling Flashcard Data
    language: str
    categories: list
    word: str
    pronunciation: str
    translation: str


def new_fc() -> None:
    # TODO New Flashcard Logic
    # This is the logic for creating a new flashcard
    pass
    # Take In Input Dict from input_handling.flashcard_input

    # Verify Data

    # Insert into DB
