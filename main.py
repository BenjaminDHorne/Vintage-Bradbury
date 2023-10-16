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


def add_images():
    if input(prompts.ADD_IMAGE) == 'card':
        path = input(prompts.IMAGE_PATH)
        # need to get card, can do a search to get back id?
        database.insert_card_image(path) # need to add cid
    elif input(prompts.ADD_IMAGE) == 'mem':
        path = input(prompts.IMAGE_PATH)
        # need to get item, can do a search to get back id?
        database.insert_memorabilia_image(path) # need to add mid


def print_results(results, result_type):
    if result_type == "card":
        for cid, collection_code, player, team, card_set, year, card_number, parallel in results:
            outstr = f"{cid}: {player} {card_set} {card_number} {parallel} in Collection {collection_code}" \
                if parallel != "NULL" else f"{cid}: {player} {card_set} {card_number} in Collection {collection_code}"
            print(outstr)
    elif result_type == "mem":
        for mid, collection_code, item_name in results:
            print(f"{mid}: {item_name} in Collection {collection_code}")


def search_prompt(search_type=None):
    search_results = None

    if search_type is None:
        search_type = input(prompts.SEARCH_TYPE)

    if search_type == 'card':
        term = input(prompts.CARD_SEARCH_TERM)
        search_results = database.search('card', term)
    elif search_type == 'mem':
        term = input(prompts.MEM_SEARCH_TERM)
        search_results = database.search('mem', term)

    if search_results is None:
        print("No matches were found.")
    else:
        print_results(search_results, search_type)


def produce_report():
    pass


# --- Main Menu ---

MENU_OPTIONS = {
        "1": add_new_cards,
        "2": add_new_memorabilia,
        "3": add_images,
        "4": search_prompt,
        "5": produce_report
    }


def menu():
    while (selection := input(prompts.MENU_PROMPT)) != "6":
        try:
            MENU_OPTIONS[selection]()
        except KeyError:
            print("Invalid input selected. Please try again.")


if __name__ == "__main__":
    database.create_tables()
    #google_sheet.update_db_from_sheet(True)
    menu()
