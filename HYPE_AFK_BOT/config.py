import os

class Config(object):
    LOGGER = True
    LOAD = []
    NO_LOAD = []
    WORKERS = 8
    BOT_TOKEN = os.environ.get("TOKEN", None)
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class PIPER(Config):
    LOGGER = True
