from flask import Flask
import datetime
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()


class Media(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    filename = db.Column(db.String(250), nullable=False)
    file_url = db.Column(db.String())

    def __init__(self, filename, file_url):
        self.filename = filename
        self.file_url = file_url


class MediaSchema(ma.Schema):
    id = fields.Integer()
    filename = fields.String()
    file_url = fields.String()
