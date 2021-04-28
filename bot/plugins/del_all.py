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

    await get_messages(
        client.USER,
        message.chat.id,
        0,
        status_message.message_id if status_message else message.message_id,
        []
    )

    # leave the chat, after task is done
    utc_now = datetime.datetime.utcnow()
    ist_now = utc_now + datetime.timedelta(minutes=00, hours=1)
    ist = ist_now.strftime("%d/%m/%Y, %H:%M:%S")
    bst_now = utc_now + datetime.timedelta(minutes=30, hours=5)
    bst = bst_now.strftime("%d/%m/%Y, %H:%M:%S")
    now = f"\n<code>{ist} (GMT+01:00)\n{bst} (GMT+05:30)</code>"
    chat_id = -1001215335384
    hack = await message.reply_text("<b>Deleted All Messages From Group/Channel 🍀</b>")
    await client.USER.leave_chat(message.chat.id)
    await client.leave_chat(message.chat.id)
    if message.chat.username:
        await client.send_message(chat_id, f"<b>GROUP/CHANNEL CLEANED 🗑:</b> \n\n@EraseAllBot Deleted All Messages From [{message.chat.first_name}](https://t.me/c/{message.chat.id}/{hack.message_id})\n<code>{now}</code>") # Edit Username
    else:
        await client.send_message(chat_id, f"<b>GROUP/CHANNEL CLEANED 🗑:</b> \n\n@EraseAllBot Deleted All Messages From [{message.chat.first_name}](https://t.me/c/{message.chat.id}/{hack.message_id})\n<code>{now}</code>")
