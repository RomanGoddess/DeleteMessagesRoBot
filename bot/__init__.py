#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

""" credentials """

import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from bot.get_config import get_config


# apparently, no error appears even if the path does not exists
load_dotenv("config.env")


# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = int(get_config("APP_ID", should_prompt=True))
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
# string session for running as user
TG_USER_SESSION = get_config("TG_USER_SESSION", should_prompt=True)
TG_BOT_SESSION = get_config("TG_BOT_SESSION", "bot")
# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "MessageDeletErBot.log")
# number of messages that can be deleted in One Request, in Telegram
TG_MAX_SEL_MESG = int(get_config("TG_MAX_SEL_MESG", 99))
TG_MIN_SEL_MESG = int(get_config("TG_MIN_SEL_MESG", 0))
# a dictionary to store the currently running processes
AKTIFPERINTAH = {}


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)

GUIDE_MESSAGE = "<a href='https://t.me/HowToUseDeleteAllRobot/2'>THIS GUIDE</a>"
REQD_PERMISSIONS = "<a href='https://t.me/HowToUseDeleteAllRobot/2'>HOW TO USE DELETE ALL ROBOT</a> "
GIT_REPO_LINK = "@Iggie"
""" strings to be used in the bot """
START_MESSAGE = get_config("START_MESSAGE", (
    "<b>I'm a bot that can delete all your channel or supergroup messages.\n\nTo use me:\n- Add Me To The Channel/Supergroup As Admin <a href='https://t.me/HowToUseDeleteAllRobot/2'>WITH ALL GIVEN PERMISSIONS LISTED HERE</a> \n\n➤ Delete Messages ✅\n➤ Invite Users Via Link ✅\n➤ Add New Admins ✅\n\n- send /delall if you want all the messages to be deleted\n- send as reply to a message /delfrom (beginning point) & /delto (end point) before using /delsel if you want to delete that & all subsequent messages.</b> "
    "\n\n"
    f"<b>READ THIS GUIDE BEFORE USING BOT</b> 👉 {REQD_PERMISSIONS} 👈"
    "\n\n"
    f"<b>In case of issues, contact</b> {GIT_REPO_LINK}"
))
START_COMMAND = get_config("START_COMMAND", "start")
DEL_ALL_COMMAND = get_config("DEL_ALL_COMMAND", "delall")
BEGINNING_DEL_ALL_MESSAGE = get_config("BEGINNING_DEL_ALL_MESSAGE", (
    "Deleting All Messages Now, Make Sure All Permissions Have Been Given From {GUIDE_MESSAGE}..."
))
IN_CORRECT_PERMISSIONS_MESSAGE = get_config("IN_CORRECT_PERMISSIONS_MESSAGE", (
    "Something Went Wrong. ⚠ \n\n"
    "<code>{}</code>"
    "\n\n"
    f"Please Verify <a href='https://t.me/HowToUseDeleteAllRobot/2'>ALL PERMISSIONS HAVE BEEN GIVEN BY CLICKING HERE</a>, "
    "& Try Again After Sometime."
))
SEL_DEL_COMMAND = get_config("SEL_DEL_COMMAND", "delsel")
BEGINNING_SEL_DEL_MESSAGE = get_config("BEGINNING_SEL_DEL_MESSAGE", (
    "Deleting Selected Messages Has Began, Make Sure All Permission Have Been Given From {GUIDE_MESSAGE}.."
))
DEL_FROM_COMMAND = get_config("DEL_FROM_COMMAND", "delfrom")
DEL_TO_COMMAND = get_config("DEL_TO_COMMAND", "delto")
NOT_USED_DEL_FROM_DEL_TO_MESSAGE = get_config(
    "NOT_USED_DEL_FROM_DEL_TO_MESSAGE", (
        f"please use /{DEL_FROM_COMMAND} or /{DEL_TO_COMMAND} "
        f"before using /{SEL_DEL_COMMAND}"
    )
)
TL_FILE_TYPES = (
    "photo",
    "animation",
    "audio",
    "document",
    "video",
    "video_note",
    "voice",
    # "contact",
    # "dice",
    # "poll",
    # "location",
    # "venue",
    "sticker",
    "text"
)
