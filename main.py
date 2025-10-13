# Main Flashcards
from flashcard_main import startup, modes
import sqlite3


def main():
    """
    main _summary_

    This will be the main function where we will call all logic from the flashcard_main directory
    """

    # Start up Logic Executed and Connection Established
    connection: sqlite3.Connection = startup.startup_main()

    # Choose Mode
    modes.choose_mode(connection)


if __name__ == "__main__":
    main()
