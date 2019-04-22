from flask import request, current_app
from flask_restful import Resource, reqparse
from Model import db, Media, MediaSchema
import werkzeug
import uuid
import os
import json
import subprocess
from utils.renders import time_symmatry_overlay

media_schema = MediaSchema(many=True)


class MediaResource(Resource):
    def get(self):
        medias = Media.query.all()
        medias = media_schema.dump(medias).data
        out = subprocess.Popen('ffmpeg', shell=True, stdout=subprocess.PIPE)
        stdout, stderr = out.communicate()
        print(stdout)
        return {
            'status': 'success',
            'data': medias
        }, 200

    def post(self):
        print(request)
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

        time_symmatry_overlay(f_path, overlay_path, 2.0, 1.0, final_path)
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
