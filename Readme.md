# Flashcard Program

## Overview

The Flashcard Program is a tool designed to enhance language learning by enabling users to create, study, and manage flashcards. It supports multiple languages and offers advanced features such as category tagging and performance tracking.

## Features

- **SQL Storage**: Each language is stored in its own SQL database.
- **Category Tags**: Organize flashcards by categories for better sorting and studying.
- **Study Algorithm**: Optimizes learning by tracking known and struggle words.
  - Marks words as "learned" or "known" after repeated correct answers.
  - Flags frequently missed words for more frequent review.
- **Results Page**: Displays user performance statistics.
- **Error Handling**: Identifies incomplete flashcards with missing information.

## Files

- `main.py`: Entry point of the application. Handles the overall startup logic.
- `flashcard_main/`
  - `__init__.py`: Marks the directory as a Python package.
  - `db_handling.py`: Manages database connection, initialization, and operations.
  - `flashcard_logic.py`: Core logic for managing flashcards, including creation and study algorithms.
  - `flashcards_utility.py`: Utility functions to support flashcard operations.
  - `input_handling.py`: Handles user input and validation.
  - `modes.py`: Manages different modes of the application (e.g., Study, Create, Edit).
  - `startup.py`: Handles initialization tasks such as user data setup and database checks.
  - `user_data.yaml`: Stores user-specific data such as username and settings.
  - `__pycache__/`: Directory for compiled Python files.
  - `flashcards.db`: SQLite database file for storing flashcard data.

## Changelog

### Version 0.0.0

### Development Period

- **Start Date**: 10 October 2025
- **End Date**: _TBD_

### Implemented

- Basic `user_data.yaml` and `flashcards.db` initialization.
- Basic input handling skeleton:
  - String input.
  - Placeholder flashcard creation input.
- Basic database handling:
  - Empty check.
  - Connection setup.
  - Tentative first-time database setup:
    - Tables for languages, flashcards, and categories.
    - Support for multiple categories.
  - Language list retrieval and handling if none exist.

### Changes

- **14 Oct 2025**
  - Implemented beginning stages of `Flashcard` dataclass in `flashcard_logic.py`
  - Moved `choose_mode_input()` function from `input_handling.py` to `modes.py`
  - Worked on `flashcard_input()` implementation in `input_handling.py`

- **12 Oct 2025**
  - Reworked `main.py` to centralize database connection logic.
  - Cleaned up `startup_main()` function and moved logic to `db_handling.py`.
  - Created `modes.py` to handle all mode-related logic:
    - Moved `choose_mode()` function from `input_handling.py` to `modes.py`.
    - Updated `main()` to call `choose_mode` from `modes.py`.
  - Refactored `modes.choose_mode()` and added `input_handling.choose_mode_input()` helper function.
  - Created `flashcards_utility.py` for utility functions
    - `clear_console()` for clearing terminal
