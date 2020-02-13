# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# This module originally created by @spechide https://github.com/SpEcHiDe/UniBorg/blob/master/stdplugins/GBan.py

from telethon import events
import asyncio
from userbot.events import register
from userbot import bot
from userbot import GBAN_GROUP
from ..help import add_help_item


@register(outgoing=True, pattern=r"^\.fban(?: |$)(.*)")
async def _(event):
    if GBAN_GROUP is None:
        await event.edit("ENV VAR is not set. This module will not work.")
        return
    if event.fwd_from:
        return
    reason = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        r = await event.get_reply_message()
        if r.forward:
            r_from_id = r.forward.from_id or r.from_id
        else:
            r_from_id = r.from_id
        await bot.send_message(GBAN_GROUP,
            "/fban [user](tg://user?id={}) {}".format(r_from_id, reason)
        )
    await event.delete()


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
 