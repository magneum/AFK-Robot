import logging
import os
import sys
import time
import telegram.ext as tg
from telethon import TelegramClient


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)


ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
    API_ID = os.environ.get("API_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    DB_URI = os.environ.get("DATABASE_URL")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    WORKERS = int(os.environ.get("WORKERS", 8))

else:
    from HYPE_AFK_BOT.config import Development as Config
    TOKEN = Config.TOKEN
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")
    OWNER_USERNAME = Config.OWNER_USERNAME
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    WORKERS = Config.WORKERS

updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
dispatcher = updater.dispatcher