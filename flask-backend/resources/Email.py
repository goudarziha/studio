from flask import request, current_app
from flask_restful import Resource, reqparse
from Model import db, Media, Email, EmailSchema
import werkzeug
import uuid
import os
import json
import requests
import subprocess

# class Email(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
#     email = db.Column(db.String())
#     media_id = db.Column(db.Integer, db.ForeignKey('media.id'))
#     # media = db.relationship(
#     #     "Media", backref=db.backref('media', userlist=False))
#     is_posted = db.Column(db.Boolean, default=False)
#     api_id = db.Column(db.Integer)


class EmailResource(Resource):
    def get(self):
        email_schema = EmailSchema(many=True)
        emails = Email.query.all()
        data = email_schema.dump(emails).data
        return {
            'status': 'success',
            'emails': data
        }

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'media_id', help="Media ID is required", required=True)
        parser.add_argument('email', help="Email is required", required=True)
        data = parser.parse_args()

        new_email = Email(email=data['email'], media_id=data['media_id'])
        try:
            new_email.save()
            return {
                'status': True,
                'email': {
                    'id': new_email.id,
                    'media_id': new_email.media_id,
                    'is_posted': new_email.is_posted,
                    'api_id': new_email.api_id
                }
            }
        except:
            return {
                'status': False,
                'message': 'Failed to save email'
            }


class EmailJob(Resource):
    def get(self):
        # chekc internet
        unposted_emails = Email.query.filter_by(is_posted=False).all()
        for email in unposted_emails:
            media = Media.query.filter_by(
                id=email.media_id).first()
            print(media.is_posted)
            if media.is_posted:
                print('media is posted')
                gallery_media_id = media.gallery_id
                print(gallery_media_id)
                payload = {'email': email.email, 'media_id': gallery_media_id}
                print(payload)
                r = requests.post(
                    current_app.config['POST_EMAIL_URL'], data=payload)
                print(r.text)

                if r.status_code == 200:
                    print('here')
                    json = r.json()
                    print(json)
                    if json['email'] == 'success':
                        print('success')
                        email.post_success()
                        email.save()
                    else:
                        print("fail")
                else:
                    print('fail')
            else:
                print('media is not posted')

        return ''
