from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

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

GALLERY_ID = 3
POST_MEDIA_URL = 'http://dev.journlr.co/api/gallery/'
# POST_MEDIA_URL = 'http://localhost:5000/api/gallery/'
POST_EMAIL_URL = 'http://dev.journlr.co/api/email'

JOBS = [
    {
        'id': 'one',
        'func': 'jobs:media',
        'trigger': 'interval',
        'seconds': 30
    },
    {
        'id': 'email',
        'func': 'jobs:email',
        'trigger': 'interval',
        'seconds': 30
    }
]
SCHEDULER_API_ENABLED = True
