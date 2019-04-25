from flask import request, current_app
from Model import db, Media, Email, EmailSchema
import os
import json
import requests
import subprocess


def connection_check():
    try:
        requests.get("http://google.com", timeout=3)
        return True
    except requests.ConnectionError:
        pass

    return False


def media():
    print("checking for unposted media")
    if connection_check():
        with db.app.app_context():
            unposted_media = Media.query.filter_by(is_posted=False)
            for x in unposted_media:
                gallery_id = db.app.config['GALLERY_ID']
                base_url = db.app.config['POST_MEDIA_URL']
                file_path = os.path.join(
                    db.app.config['STATIC_DIR'], x.file_url)
                url = base_url + str(gallery_id)
                media = {'media': open(file_path, 'rb')}
                res = requests.post(url, files=media)
                if res.status_code == 200:
                    json = res.json()
                    if json['media'] == 'success':
                        x.post_success(gallery_id=json['id'])
                        x.save()
                        print('media posted')
                    else:
                        print('media posted error...')
                else:
                    print('media post status failed')
    else:
        print("Internet connection down")
# return 'finished'


def email():
    print("Checking for unposted email")
    if connection_check():
        with db.app.app_context():
            unposted_emails = Email.query.filter_by(is_posted=False).all()
            for email in unposted_emails:
                media = Media.query.filter_by(id=email.media_id).first()
                if media.is_posted:
                    print('Attempt emailing ' + str(media.id))
                    gallery_media_id = media.gallery_id
                    payload = {'email': email.email,
                               'media_id': gallery_media_id}
                    print(payload)
                    print(db.app.config['POST_EMAIL_URL'])
                    r = requests.post(
                        db.app.config['POST_EMAIL_URL'], data=payload)
                    if r.status_code == 200:
                        json = r.json()
                        if json['email'] == 'success':
                            email.post_success()
                            email.save()
                        else:
                            print('Email post not successful')
                    else:
                        print('connection err')
    else:
        print('Internet connection down')
