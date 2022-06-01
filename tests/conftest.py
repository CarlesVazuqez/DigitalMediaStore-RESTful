import pytest

from app import create_app
from app.config import app_config


@pytest.fixture(scope="session")
def flask_app():
    application = create_app(app_config["PRU"])
    application.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    application.config["TESTING"] = True

    from app.extensions.database import db

    with application.app_context():
        db.init_app(application)
        db.create_all()
        yield application


@pytest.fixture(scope="session")
def test_client(flask_app):
    return flask_app.test_client()