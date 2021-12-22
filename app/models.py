# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Data Models"""

from config import db, mm


class Book(db.Model):
    __tablename__ = "BOOKS"
    isbn = db.Column(db.String, primary_key=True)
    author = db.Column(db.String)
    title = db.Column(db.String)
    call_no = db.Column(db.String)


class BookSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        sqla_session = db.session


class User(db.Model):
    __tablename__ = "SHELVES"
    username = db.Column(db.String)
    userid = db.Column(db.Integer, primary_key=True)

class UserSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session