"""
This File is the Logic Run at App Start
"""

from . import db_handling, input_handling
import yaml  # type: ignore
import os
import sqlite3


def user_data() -> None:
    # Check for Existence of User Data File
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_dir, "user_data.yaml")

    if os.path.exists(file_name):
        # Read User Data
        with open(file_name, "r") as file:
            data: dict = yaml.safe_load(file)
        username = data.get("user", {}).get("username", "Unknown")
        print(f"Welcome back {username}!")

    else:
        print("Welcome to the Language Flashcard App!")
        # Get Username
        print("Please Enter A Username.")
        username: str = input_handling.basic_input_str()
        # Create User Data
        user_data: dict = {
            "user": {
                "username": username,
                "settings": {"theme": "dark"},
            }
        }
        with open(file_name, "w") as file:
            yaml.dump(user_data, file, default_flow_style=False, sort_keys=False)
        print("User Data File Created!")


def startup_main() -> None:
    # Initialize DB
    connection: sqlite3.Connection = db_handling.db_connect()

    # User Data File Check
    user_data()

    # Database Check
    db_handling.db_check_if_empty(connection)
    print("What Do You want to Study?")
    # Print Existing Sets / Create New
