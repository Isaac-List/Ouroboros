# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Application"""

from flask import Flask, render_template, request, Response, jsonify
from app.config import app, db
from app.classify import getInfo
from app import Book, BookSchema
import json


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        # Get book information via Classify
        isbn: str = str(request.form.get("isbn"))
        book = getInfo(isbn)

        author = book["classify"]["work"]["@author"]
        title = book["classify"]["work"]["@title"].title()
        dewey = book["classify"]["recommendations"]["ddc"]["mostPopular"]["@sfa"]
        congress = book["classify"]["recommendations"]["lcc"]["mostPopular"]["@sfa"]

        # Add book to the database
        book: Book = Book(
            isbn = isbn,
            author = author,
            title = title,
            call_no = congress
        )

        db.session.add(book)
        db.session.commit()

        # Render the success method
        res = {"author": author, "title": title, "dewey": dewey, "congress": congress}

        return render_template("add.html", result=res)

@app.route("/api/books", methods=["GET"])
def api_books():
    books = Book.query.all()
    book_schema = BookSchema(many=True)
    bookdata = book_schema.dump(books)

    resp: dict = {"results": []}
    for book in books:
        resp["results"].append({
            "isbn": book.isbn,
            "author": book.author,
            "title": book.title,
            "call_no": book.call_no
        })

    resp_json: str = Response(json.dumps(resp))
    resp_json.headers["Access-Control-Allow-Origin"] = "*"
    resp_json.headers["Content-Type"] = "application/json"

    return resp_json
