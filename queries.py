
# Table Creation
CREATE_CARDS_TABLE = """CREATE TABLE IF NOT EXISTS cards (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        collection_code TEXT, player TEXT, team TEXT, card_set TEXT, year INTEGER, card_number TEXT, 
                        parallel TEXT, rookie INTEGER, sophomore INTEGER, sticker INTEGER, food_product INTEGER, 
                        autograph INTEGER, memorabilia INTEGER, set_insert INTEGER,	numbered INTEGER, grade TEXT, 
                        purchase_price REAL, purchase_date INTEGER);"""

CREATE_MEMORABILIA_TABLE = """CREATE TABLE IF NOT EXISTS memorabilia (id INTEGER PRIMARY KEY AUTOINCREMENT, collection_code TEXT,
                            item_name TEXT, signatures TEXT, inscriptions TEXT, authentication TEXT, notes TEXT,
                            purchase_price REAL, purchase_date INTEGER);"""

CREATE_CARD_IMAGES_TABLE = """CREATE TABLE IF NOT EXISTS card_images (card_id INTEGER NOT NULL,
                            image1 BLOB, image2 BLOB, image3 BLOB, FOREIGN KEY(card_id) REFERENCES cards(id));"""

CREATE_MEMORABILIA_IMAGES_TABLE = """CREATE TABLE IF NOT EXISTS memorabilia_images (memorabilia_id INTEGER NOT NULL, image1 BLOB, 
                                image2 BLOB, image3 BLOB, FOREIGN KEY(memorabilia_id) REFERENCES memorabilia(id));"""

CREATE_CARD_COLLECTION_CODES_TABLE = """CREATE TABLE IF NOT EXISTS card_collection_codes (collection_code TEXT NOT NULL, 
                                description TEXT, FOREIGN KEY(collection_code) REFERENCES cards(collection_code));"""

CREATE_MEMORABILIA_COLLECTION_CODES_TABLE = """CREATE TABLE IF NOT EXISTS memorabilia_collection_codes (collection_code TEXT NOT NULL,
                            description TEXT, FOREIGN KEY(collection_code) REFERENCES memorabilia(collection_code));"""

CREATE_CARD_VALUES_TABLE = """ """  # to do based on ebay api


# Insert Queries
INSERT_CARD = """INSERT INTO cards (collection_code, player, team, card_set, year, card_number, parallel, 
            rookie, sophomore, autograph, memorabilia, set_insert, numbered, grade, purchase_price, purchase_date) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) RETURNING id;"""

INSERT_MEMORABILIA = """INSERT INTO memorabilia (collection_code, item_name, signatures, inscriptions, 
                    authentication, notes, purchase_price, purchase_date) VALUES (?,?,?,?,?,?,?,?) RETURNING id;"""

INSERT_CARD_COLLECTION_CODE = """INSERT INTO card_collection_codes (collection code, description) VALUES (?,?);"""

INSERT_MEMORABILIA_COLLECTION_CODE = """INSERT INTO memorabilia_collection_codes (collection code, description)
                                    VALUES (?,?);"""

INSERT_CARD_IMAGES = """INSERT INTO card_images (card_id, image1, image2, image3) VALUES (?,?,?,?);"""

INSERT_MEMORABILIA_IMAGES = """INSERT INTO memorabilia_images (memorabilia_id, image1, image2, image3) 
                            VALUES (?,?,?,?);"""

# Select Queries
SEARCH_CARDS = """SELECT id, collection_code, player, team, card_set, year, card_number, parallel 
    FROM cards WHERE player LIKE ? OR card_set LIKE ? OR collection_code LIKE ?;"""
SEARCH_MEM = """SELECT id, collection_code, item_name FROM memorabilia WHERE 
    collection_code LIKE ? OR item_name LIKE ?;"""