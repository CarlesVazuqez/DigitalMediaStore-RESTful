import os


class Config(object):
    API_TITLE = os.environ["API_TITLE"]
    API_VERSION = os.environ["API_VERSION"]
    OPENAPI_VERSION = os.environ["OPENAPI_VERSION"]
    OPENAPI_URL_PREFIX = os.environ["OPENAPI_URL_PREFIX"]
    OPENAPI_RAPIDOC_PATH = os.environ["OPENAPI_RAPIDOC_PATH"]
    OPENAPI_RAPIDOC_URL = os.environ["OPENAPI_RAPIDOC_URL"]
    CSRF_ENABLED = True
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = os.environ["PROPAGATE_EXCEPTIONS"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]


class DesarrolloConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class PruebasConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI_TEST"]


class PreProduccionConfig(Config):
    DEBUG = True


class ProduccionConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    "DES": DesarrolloConfig,
    "PRU": PruebasConfig,
    "PRE": PreProduccionConfig,
    "PRO": ProduccionConfig,
}
