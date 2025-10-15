"""
This is the logic for modes and related
"""

from . import input_handling, db_handling, flashcards_utility
import sqlite3
from time import sleep


def choose_mode_input() -> int:
    # Input handling for modes.choose_mode()
    while True:
        user_input: str = input_handling.basic_input_str(prompt="Mode")
        try:
            choice: int = int(user_input)
            break
        except:
            print("Please Only Enter the Number For Your Choice")
    return choice


def choose_mode(connection: sqlite3.Connection) -> None:
    # Extend List to Add Modes and Add Functionality Call to Check
    modes: list[str] = ["Study", "Create New Flashcards", "Edit Flashcards", "Quit"]

    while True:
        print("What Do You Want To Do?")
        for i in range(len(modes)):
            print(f"{i+1} | {modes[i]}")

        choice: int = choose_mode_input()

        if choice == 1:
            # 1 = Study Mode
            print("1-Study")
            mode_study(connection)
            break

        elif choice == 2:
            # 2 = Create Mode
            print("2-Create")
            mode_create(connection)
            break

        elif choice == 3:
            # 3 = Edit Mode
            print("3-Edit")
            mode_edit(connection)
            break

        elif choice == 4:
            print("4-Quit")
            mode_quit(connection)
            break

        else:
            print("Please Make a Valid Choice")


def mode_study(connection: sqlite3.Connection) -> None:
    # TODO Study Functionality
    # This will be the main logic for the study mode

    # Retrieve the Languages List and get User Input choice
    db_handling.lang_list(connection)
    pass


def mode_create(connection: sqlite3.Connection) -> None:
    # TODO Create Functionality
    # This will be the main logic for the create new mode
    pass


def mode_edit(connection: sqlite3.Connection) -> None:
    # TODO Edit Functionality
    # This will be the logic for the edit mode
    pass


def mode_quit(connection: sqlite3.Connection) -> None:

    # This will be the main logic for quitting (save/close db)
    print("Saving and Shutting Down. Please Wait.")

    # Save DB
    connection.commit()
    sleep(2)
    print("Database Saved.")

    # Close DB Connection
    connection.close()
    sleep(2)
    print("Database Connection Closed.")

    # Print Success
    print("Program Successfully Saved and Exited!")
    sleep(2)

    # Clear Console / Quit
    flashcards_utility.clear_console()
    quit()
