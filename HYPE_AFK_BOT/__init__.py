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
    from HYPE_AFK_BOT.config import Development as Config
    TOKEN = Config.TOKEN
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    WORKERS = Config.WORKERS
else:
    sys.exit
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
dispatcher = updater.dispatcher