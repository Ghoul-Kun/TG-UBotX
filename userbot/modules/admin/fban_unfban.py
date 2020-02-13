# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio

from telethon.tl.types import MessageEntityMentionName

from userbot import bot
from userbot.events import register
from userbot import GBAN_GROUP
from ..help import add_help_item


@register(outgoing=True, pattern=r"^\.fban")
async def gban_all(msg):
    textx = await msg.get_reply_message()
    if textx:
        try:
            banreason = "[userbot] "
            banreason += banreason.join(msg.text.split(" ")[1:])
            if banreason == "[userbot]":
                raise TypeError
        except TypeError:
            banreason = "[userbot] gban"
    else:
        banid = msg.text.split(" ")[1]
        if banid.isnumeric():
            # if its a user id
            banid = int(banid)
        else:
            # deal wid the usernames
            if msg.message.entities is not None and isinstance(msg.message.entities[0],
                                                               MessageEntityMentionName):
                ban_id = msg.message.entities[0].user_id
        try:
            banreason = "[userbot] "
            banreason += banreason.join(msg.text.split(" ")[2:])
            if banreason == "[userbot]":
                raise TypeError
        except TypeError:
            banreason = "[userbot] fban"
    if not textx:
        await msg.edit(
            "Reply Message missing! Might fail on many bots! Still attempting Gban!"
        )
            if textx:
                c = await bot.send_message(GBAN_GROUP)
                await c.reply("/id")
            await conv.send_message(f"/fban {banid} {banreason}")
            await bot.send_read_acknowledge(conv.chat_id)
            count += 1


@register(outgoing=True, pattern=r"^\.unfban(?: |$)(.*)")
async def _(event):
    if GBAN_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        r_from_id = r.from_id
        await bot.send_message(GBAN_GROUP,
            "/unfban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()


add_help_item(
    "fban",
    "Admin",
    "Give FedBan through userbot",
    """
.fban [reason]
.unfban [reason]
    """
)
