# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""App Config File"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Initialize Flask app
app = Flask(__name__)

this_dir = os.path.abspath(os.path.dirname(__file__))

# Configure Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(this_dir, "booklist.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

mm = Marshmallow(app)
