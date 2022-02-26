import time

import gspread
import json
import database


def get_sheet(worksheet):
    with open("sheet_info.json") as info_file:
        sheet_info = json.load(info_file)

    sa = gspread.service_account(filename="service_account.json")
    sh = sa.open(sheet_info['spreadsheet_name'])

    if worksheet == 'cards':
        wks = sh.worksheet(sheet_info['card_worksheet_name'])
    else:
        wks = sh.worksheet(sheet_info['memorabilia_worksheet_name'])

    return wks


def mark_in_db(wks, row_num):
    wks.update(f'T{row_num}', 'TRUE')


def mark_images_in_db(wks, row_num):
    wks.update(f'U{row_num}', 'TRUE')


def update_db_from_sheet(cards):
    if cards:
        sheet = get_sheet('cards')
        values = sheet.get_all_values()  # list of lists
    else:
        sheet = get_sheet('memorabilia')
        values = sheet.get_all_values()  # list of lists

    values = values[1:]  # remove header
    row_num = 2
    processed = 0

    # Note, this code is hard indexed, so the column order should remain static
    for packed_values in values:
        if processed % 60 == 0 and processed > 0:
            print(f'{processed} calls made to Google Drive API. Sleeping...')
            time.sleep(100)

        in_database = False if packed_values[-2] == "FALSE" else True
        if not in_database and cards:
            database.insert_card(tuple(packed_values[:-3]))  # Remove flag columns
            mark_in_db(sheet, row_num)
            processed += 1
        elif not in_database and not cards:
            database.insert_memorabilia(tuple(packed_values[:-3]))
            mark_in_db(sheet, row_num)
            processed += 1

        images_in_database = False if packed_values[-1] == "FALSE" else True
        images_path = packed_values[-3]
        if images_path != 'NA':
            if not images_in_database and cards:
                database.insert_card_image(images_path)
                mark_images_in_db(sheet, row_num)
                processed += 1
            elif not images_in_database and not cards:
                database.insert_memorabilia_image(images_path)
                mark_images_in_db(sheet, row_num)
                processed += 1

        row_num += 1


# Tester code
if __name__ == "__main__":
    update_db_from_sheet(True)  # Test card update function