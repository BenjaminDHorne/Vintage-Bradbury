import sqlite3

import queries

from contextlib import closing

#connection = sqlite3.connect("dsm.db")
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
    collection_code, item_name, signatures, inscriptions, authentication, notes, \
                    purchase_price, purchase_date = packed_values

    # insert into to database
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute(queries.INSERT_CARD, (collection_code, item_name, signatures, inscriptions, authentication,
                                            notes, purchase_price, purchase_date))
        cursor.close()


def insert_card_image(images_path, cid):
    pass


def insert_memorabilia_image(images_path, mid):
    pass


# search functions
def search(table, term):
    term = f"%{term}%"
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        if table == 'card':
            cursor.execute(queries.SEARCH_CARDS, (term,term,term))
        elif table == 'mem':
            cursor.execute(queries.SEARCH_MEM, (term,term))
        return cursor.fetchall()


# report functions
