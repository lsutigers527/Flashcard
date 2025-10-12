"""
This File Contains Various Functions for Handling User Input at Various Times
"""


def basic_input_str() -> str:
    # This is a basic input function that will return a string
    user_input: str = input(f"Input: ")
    return user_input


def flashcard_input() -> dict:
    flashcard: dict = {
        "language": "",
        "categories": [],
        "word": "",
        "pronunciation": "",
        "translation": "",
    }


def choose_mode() -> None:
    # Extend List to Add Modes and Add Functionality Call to Check
    modes: list[str] = ["Study", "Create New Flashcards", "Edit Flashcards"]

    print("What Do You Want To Do?")
    for i in range(len(modes)):
        print(f"{i} | {modes[i]}")

    while True:
        user_input: str = basic_input_str()
        try:
            choice: int = int(user_input)
            break
        except:
            print("Please Only Enter the Number For Your Choice")
            choose_mode()

    if choice == 1:
        # Study Logic Here
        pass
    elif choice == 2:
        # Create New Logic Here
        pass
    elif choice == 3:
        # Edit Logic Here
        pass
    else:
        print("Please Make a Valid Choice")
        choose_mode()
