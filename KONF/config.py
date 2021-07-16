import os

class Config(object):
    LOGGER = True
    LOAD = []
    NO_LOAD = []
    WORKERS = 8
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
class PIPER(Config):
    LOGGER = True
