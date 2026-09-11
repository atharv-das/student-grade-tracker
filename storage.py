import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    # If the file hasn't been created yet, return an empty list
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        # In case the file is empty or corrupted, start fresh
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)
