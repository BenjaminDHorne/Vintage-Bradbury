

import database
import reports
import images
import prompts
import google_sheet


def add_new_cards():
    if input(prompts.UPDATE_FROM_CSV) == 'y':
        google_sheet.update_db_from_sheet(cards=True)
    else:
        pass


def add_new_memorabilia():
    if input(prompts.UPDATE_FROM_CSV) == 'y':
        google_sheet.update_db_from_sheet(cards=False)
    else:
        pass


def produce_report():
    pass


# --- Main Menu ---

MENU_OPTIONS = {
        "1": add_new_cards,
        "2": add_new_memorabilia,
        "3": produce_report,
    }


def menu():
    while (selection := input(prompts.MENU_PROMPT)) != "4":
        try:
            MENU_OPTIONS[selection]()
        except KeyError:
            print("Invalid input selected. Please try again.")


if __name__ == "__main__":
    database.create_tables()
    google_sheet.update_db_from_sheet(True)
    #menu()
