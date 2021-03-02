#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | @AbirHasan2005
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

import datetime
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import (
    ChatAdminRequired
)
from bot import (
    BEGINNING_DEL_ALL_MESSAGE,
    DEL_ALL_COMMAND,
    IN_CORRECT_PERMISSIONS_MESSAGE
)
from bot.bot import Bot
from bot.helpers.custom_filter import allowed_chat_filter
from bot.helpers.get_messages import get_messages
from bot.helpers.make_user_join_chat import make_chat_user_join


@Bot.on_message(
    filters.command(DEL_ALL_COMMAND) &
    allowed_chat_filter
)
async def del_all_command_fn(client: Bot, message: Message):
    chat_name = message.chat.title
    chat_chit = message.chat.id
    chat_link = str(chat_chit)[4:]
    chat_link_m = message.message_id
    chat_username = None
    delete_msg = None
    try:
        chat_username = message.chat.username
    except:
        chat_username = None
    delete_msg = None
    try:
        status_message = await message.reply_text(
            BEGINNING_DEL_ALL_MESSAGE
        )
    except ChatAdminRequired:
        status_message = None

    s__, nop = await make_chat_user_join(
        client.USER,
        client.USER_ID,
        message
    )
    if not s__:
        if status_message:
            await status_message.edit_text(
                IN_CORRECT_PERMISSIONS_MESSAGE.format(
                    nop
                ),
                disable_web_page_preview=True
            )
        else:
            await message.delete()
        return

    if chat_username:
        delete_msg = await client.send_message(
            chat_id=chat_id,
            text=f"Bot Trying to Delete Selected Messages from @{chat_username} !!",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    else:
        delete_msg = await client.send_message(
            chat_id=chat_id,
            text=f"Bot Trying to Delete Selected Messages from [{chat_name}](https://t.me/c/{chat_link}/{chat_link_m}) !!",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    await get_messages(
        client.USER,
        message.chat.id,
        0,
        status_message.message_id if status_message else message.message_id,
        []
    )

    # leave the chat, after task is done
    info_last_msg = await message.reply_text("Deleted All Messages From Group!")
    last_chat_msg = info_last_msg.message_id
    await delete_msg.delete()
    if chat_username:
        await client.send_message(
            chat_id=chat_id,
            text=f"Deleted Selected Messages from @{chat_username}",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    else:
        await client.send_message(
            chat_id=chat_id,
            text=f"Deleted Selected Messages from [{chat_name}](https://t.me/c/{chat_link}/{last_chat_msg})",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    time.sleep(2)
    await client.USER.leave_chat(message.chat.id)
    await client.leave_chat(message.chat.id)
