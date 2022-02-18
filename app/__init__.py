import logging
import os

from flask import Flask
from flask_cors import CORS

from app.extensions import api
from app.extensions.database import db
from app.extensions.schema import ma
from app.views import albums, artists, hello, tracks


def create_app(config, **kwargs):

    logging.basicConfig(level=logging.INFO)

    app = Flask(__name__, **kwargs)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config.from_object(config)
    # app.url_map.strict_slashes = False

    with app.app_context():
        api.init_app(app)

        db.init_app(app)
        db.create_all()

        ma.init_app(app)

        api.register_blueprint(hello.blp)
        api.register_blueprint(artists.blp)
        api.register_blueprint(albums.blp)
        api.register_blueprint(tracks.blp)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
