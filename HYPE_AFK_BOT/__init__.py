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
from HYPE_AFK_BOT.config import PIPER as Config
BOT_TOKEN = Config.BOT_TOKEN
API_ID = Config.API_ID
API_HASH = Config.API_HASH
DB_URI = Config.SQLALCHEMY_DATABASE_URI
LOAD = Config.LOAD
NO_LOAD = Config.NO_LOAD
WORKERS = Config.WORKERS

updater = tg.Updater(BOT_TOKEN, workers=WORKERS, use_context=True)
dispatcher = updater.dispatcher