from flask import request, current_app
from flask_restful import Resource, reqparse
from Model import db, Media, MediaSchema
import werkzeug
import requests
import uuid
import os
import json
import subprocess
from utils.renders import time_symmatry_overlay, studio

media_schema = MediaSchema(many=True)


class MediaResource(Resource):
    def get(self):
        medias = Media.query.all()
        medias = media_schema.dump(medias).data
        return {
            'status': 'success',
            'data': medias
        }, 200

    def post(self):
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        f_path = os.path.join(current_app.config['TMP_DIR'], f_name)
        rel_path = f_path.split('static/')[1]
        file.save(f_path)

        final_path = os.path.join(
            current_app.config['MEDIA_DIR'], f_name + '.mp4')

        overlay_path = os.path.join(
            current_app.config['OVERLAY_DIR'], 'overlay.png')

        # time_symmatry_overlay(f_path, overlay_path, 2.0, 1.0, final_path)
        cmd = studio(f_path, overlay_path, 0.9, final_path)
        subprocess.call(cmd, shell=True)

        new_media = Media(filename=f_name + '.mp4',
                          file_url=final_path.split('static/')[1])

        db.session.add(new_media)
        db.session.commit()
        return json.dumps({'filename': f_name, 'file_path': rel_path, 'id': new_media.id})

    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = media_schema.load(json_data)
        if errors:
            return errors, 422
        media = Media.query.filter_by(id=data['id']).first()
        if not media:
            return {'message': 'Media does not exist'}, 400
        media.name = data['name']
        db.session.commit()

        result = media_schema.dump(media).data
        return {'status': 'success', 'data': result}, 204


class MediaJob(Resource):
    def get(self):
        # check if internet is available
        unposted_media = Media.query.filter_by(is_posted=False)
        for x in unposted_media:
            gallery_id = current_app.config['GALLERY_ID']
            base_url = current_app.config['POST_MEDIA_URL']
            file_path = os.path.join(
                current_app.config['STATIC_DIR'], x.file_url)
            # print(file_path)
            url = base_url + str(gallery_id)
            # url = "http://dev.journlr.co/api/gallery/4"
            # print(url)
            media = {'media': open(file_path, 'rb')}
            res = requests.post(url, files=media)
            if res.status_code == 200:
                json = res.json()
                if json['media'] == 'success':
                    x.post_success(gallery_id=json['id'])
                    x.save()
                    print('media posted')
                else:
                    print('error')
            else:
                return {
                    'status': 'fail',
                    'media': 'unposted'
                }

        return {
            'status': 'finished'
        }
