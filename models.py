"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ A pet for adoption """

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default="")
    age = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)