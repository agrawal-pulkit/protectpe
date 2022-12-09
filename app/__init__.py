from flask import Flask
from flask_restful import Api

from flasgger import Swagger
from .config import config_by_name, Config
from app import resource
from .model import database
from flask_cors import CORS, cross_origin
from flask_compress import Compress

from .utils.swagger.config import swagger_config, swagger_template

cors = CORS(support_credentials=True)
compress = Compress()

swagger = Swagger(template=swagger_template(), config=swagger_config())


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    cors.init_app(app)
    compress.init_app(app)
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 8
    # app.config['SQLALCHEMY_ECHO'] = True
    database.db.init_app(app)
    database.ma.init_app(app)

    swagger.init_app(app)

    # flask-restful
    api = Api(app, errors={
        'Exception': {
            'status': 400,
            'message': 'bad_request',
            'some_description': 'Something wrong with request'
        }
    })
    resource.create_resources(api)
    return app
