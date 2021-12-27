# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Building the DataBase"""

import csv
import os
from app import Book, Shelf
from app.config import db


def build_db(dbname):
    # Delete existing DB
    if os.path.exists(f"{dbname}.sqlite3"):
        os.remove(f"{dbname}.sqlite3")

    # Create DB structure
    db.create_all()


def main():
    build_db("booklist")
    build_db("shelves")

if __name__ == "__main__":
    main()