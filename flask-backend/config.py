import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

STATIC_DIR = os.path.join(basedir, "static")
MEDIA_DIR = os.path.join(STATIC_DIR, "media")
OVERLAY_DIR = os.path.join(STATIC_DIR, "overlay")
TMP_DIR = os.path.join(STATIC_DIR, "tmp")

UPLOAD_FOLDER = MEDIA_DIR
