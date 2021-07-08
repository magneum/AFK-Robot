import importlib
import time
import re
from sys import argv
from typing import Optional
from HYPE_AFK_BOT import (
    OWNER_ID,
    dispatcher,
    updater,
    LOGGER,
)

from AWAY import ALL_MODULES
from MISCL import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import (
    BadRequest,
    ChatMigrated,
    NetworkError,
    TelegramError,
    TimedOut,
    Unauthorized,
)
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
)
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown



AFKSAY = """—🚸••÷[Hყρҽ Aϝƙ Bσƚ]÷••🚸—
ᴡᴀɪᴛ ɪ ʜᴇᴀʀᴅ ᴛʜᴀᴛ ʏᴏᴜ ɴᴇᴇᴅᴇᴅ ꜱᴏᴍᴇᴛʜɪɴɢ ᴛʜᴀᴛ ᴡᴏᴜʟᴅ ꜱᴀʏ ᴛʜᴀᴛ ʏᴏᴜ ᴀʀᴇ ᴀꜰᴋ.
𝘞𝘦𝘭𝘭 𝘸𝘦𝘭𝘭 𝘞𝘦𝘭𝘭, 𝘥𝘰𝘯'𝘵 𝘺𝘰𝘶 𝘸𝘰𝘳𝘳𝘺.

ᴊᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛʏᴘᴇ /afk ᴀɴᴅ ʀᴇꜱᴛ ɪꜱ ᴍʏ ᴡᴏʀᴋ.


—🚸••÷[Hყρҽ Aϝƙ Bσƚ]÷••🚸—
"""

# AFKWHAT = """
# Hey there! My name is 

# """

HYPE_AFK_BOT_IMG = "https://telegra.ph/file/8e5be7f7bd1f93ef370b1.jpg"

IMPORTED = {}
HELPABLE = {}
GDPR = []

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("AWAY." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module

    # if hasattr(imported_module, "__help__") and imported_module.__help__:
    #     HELPABLE[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__gdpr__"):
        GDPR.append(imported_module)



def start(update: Update, context: CallbackContext):
    if update.effective_chat.type == "private":
            update.effective_message.reply_photo(
                HYPE_AFK_BOT_IMG,
                AFKSAY,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Add AFKBot to your group",
                                url="t.me/{}?startgroup=true".format(
                                    context.bot.username
                                ),
                            )
                        ],
                    
                    ]
                ),
            )
    else:
        update.effective_message.reply_text(
            "Ready",
            parse_mode=ParseMode.HTML,
        )



def main():
    start_handler = CommandHandler("start", start, run_async=True)
    dispatcher.add_handler(start_handler)
    LOGGER.info("READY")




LOGGER.info("Successfully loaded AWAY: " + str(ALL_MODULES))
updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
main()
updater.idle()
updater.stop()