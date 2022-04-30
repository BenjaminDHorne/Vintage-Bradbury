import sqlite3

import queries

db_name = "dsm.db"


def create_tables():
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(queries.CREATE_MEMORABILIA_TABLE)
        cursor.execute(queries.CREATE_CARDS_TABLE)
        cursor.execute(queries.CREATE_CARD_COLLECTION_CODES_TABLE)
        cursor.execute(queries.CREATE_MEMORABILIA_COLLECTION_CODES_TABLE)
        cursor.execute(queries.CREATE_CARD_IMAGES_TABLE)
        cursor.execute(queries.CREATE_MEMORABILIA_IMAGES_TABLE)
        cursor.close()


# insert data functions
def insert_card(packed_values):
    # unpack values
    collection_code, player, team, card_set, year, card_number, parallel, numbered, rookie, \
                    sophomore, sticker, food_product, autograph, memorabilia, insert, grade, purchase_price, \
                    purchase_date = packed_values

    # insert into to database
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(queries.INSERT_CARD, (collection_code, player, team, card_set, year, card_number, parallel,
                                            rookie, sophomore, autograph, memorabilia, insert, numbered, grade,
                                            purchase_price, purchase_date))
        cursor.close()


def insert_memorabilia(packed_values):
    # unpack values
    collection_code, item_name, signatures, inscriptions, game_used, number_of_autographs, authentication, notes, purchase_price, estimated_value = packed_values

    # insert into to database
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(queries.INSERT_MEMORABILIA, (collection_code, item_name, signatures, inscriptions, game_used,
                                             number_of_autographs, authentication, notes, purchase_price, estimated_value))
        cursor.close()


def insert_card_image(images_path):
    pass


def insert_memorabilia_image(images_path):
    pass


def insert_values(packed_values):
    dateChecked, marketValue, lowestValue, highestValue, avgValue, medValue, stdValue, numSold = packed_values
    # TODO: insert to db, decide on how to pass around id and serach terms

# report functions


def get_starter_data():
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(queries.STARTER_DASH_DATA)
        return cursor.fetchall()
