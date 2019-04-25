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
    is_posted = db.Column(db.Boolean, default=False)
    gallery_id = db.Column(db.Integer)
    emails = db.relationship("Email", backref="medias", lazy='dynamic')

    def __init__(self, filename, file_url):
        self.filename = filename
        self.file_url = file_url

    def post_success(self, gallery_id):
        self.is_posted = True
        self.gallery_id = gallery_id

    def save(self):
        db.session.add(self)
        db.session.commit()


class MediaSchema(ma.Schema):
    id = fields.Integer()
    created = fields.String()
    filename = fields.String()
    file_url = fields.String()


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    email = db.Column(db.String())
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'))
    media = db.relationship("Media")
    is_posted = db.Column(db.Boolean, default=False)
    api_id = db.Column(db.Integer)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def post_success(self):
        self.is_posted = True


class EmailSchema(ma.Schema):
    id = fields.Integer()
    created = fields.String()
    email = fields.String()
    media_id = fields.Integer()
    is_posted = fields.Boolean()
    api_id = fields.Integer()
