"""
This File Contains Functions Related to SQL Database Handling
"""

import sqlite3
import os
from . import input_handling


def db_connect() -> sqlite3.Connection:
    # Connects to Our Database
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "flashcards.db")
    connection: sqlite3.Connection = sqlite3.connect(db_path)
    return connection


def db_first_time_setup(connection: sqlite3.Connection):
    """
    db_first_time_setup

    Initializes database with all needed tables

    Args:
        connection (sqlite3.Connection): DB Connection
    """
    cursor = connection.cursor()

    # Languages table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS languages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    """
    )

    # Flashcards table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            language_id INTEGER NOT NULL,
            word TEXT NOT NULL,
            pronunciation TEXT,
            translation TEXT NOT NULL,
            FOREIGN KEY (language_id) REFERENCES languages(id)
        );
    """
    )

    # Categories table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    """
    )

    # Flashcard-Categories (many-to-many)
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS flashcard_categories (
            flashcard_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            PRIMARY KEY (flashcard_id, category_id),
            FOREIGN KEY (flashcard_id) REFERENCES flashcards(id),
            FOREIGN KEY (category_id) REFERENCES categories(id)
        );
    """
    )

    connection.commit()
    print(
        "Database initialized with languages, flashcards, categories, and flashcard_categories tables."
    )


def db_check_if_empty(connection: sqlite3.Connection):
    # Checks if db is empty
    cursor = connection.cursor()

    # Returns all tables in DB
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # If DB is empty will run initialization
    if len(tables) == 0:
        db_first_time_setup(connection)
    else:
        pass


def lang_list(connection: sqlite3.Connection) -> list:
    """
    lang_list

    Retrieves all languages from the database.

    Args:
        connection (sqlite3.Connection): DB Connection

    Returns:
        list: A list of language names
    """
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM languages;")
    languages = [row[0] for row in cursor.fetchall()]
    return languages


def choose_lang(lang_list: list) -> str:
    lang: str = input_handling.basic_input_str()
    lang_list: list = lang_list
    # Confirm Choice Exists
    if lang not in lang_list:
        # likely have to do upper/lowercase handling here
        print("Please Enter a Valid Language")
        choose_lang(lang_list)

    else:
        return lang
