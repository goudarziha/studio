from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Media import MediaResource, MediaJob
from resources.Email import EmailResource, EmailJob

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(Hello, '/Hello')
api.add_resource(MediaResource, '/media')
api.add_resource(MediaJob, '/media/job')
api.add_resource(EmailResource, '/email')
api.add_resource(EmailJob, '/email/job')
