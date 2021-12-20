# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""Application"""

from flask import Flask, render_template, request
from config import app, db
from classify import getInfo


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        isbn: str = str(request.form.get("isbn"))
        book = getInfo(isbn)

        author = book["classify"]["work"]["@author"]
        title = book["classify"]["work"]["@title"].title()
        dewey = book["classify"]["recommendations"]["ddc"]["mostPopular"]["@sfa"]
        congress = book["classify"]["recommendations"]["lcc"]["mostPopular"]["@sfa"]

        res = {"author": author, "title": title, "dewey": dewey, "congress": congress}

        return render_template("add.html", result=res)
