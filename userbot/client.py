# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

import asyncio

from telethon import TelegramClient, hints
from telethon.tl import types
from telethon.tl.custom import Message


class UserBot(TelegramClient):
    async def send_message_sd(
            self: 'TelegramClient',
            entity: 'hints.EntityLike',
            delete_in: int,
            message: 'hints.MessageLike' = '',
            **kwargs
    ) -> 'types.Message':
        message = await self.send_message(entity, message, **kwargs)
        await asyncio.sleep(delete_in)
        await message.delete()

    async def edit_message_sd(
            self: 'TelegramClient',
            message: 'hints.MessageLike' = None,
            delete_in: int = None,
            text: str = None,
            **kwargs
    ) -> 'types.Message':
        message = await self.edit_message(message, text, **kwargs)
        await asyncio.sleep(delete_in)
        await message.delete()


Message._edit_ = Message.edit
Message._reply_ = Message.reply
Message._respond_ = Message.respond


async def edit(self, *args, **kwargs):
    delete_in = kwargs.pop('delete_in', None)
    await self._edit_(*args, **kwargs)
    if delete_in:
        await asyncio.sleep(int(delete_in))
        await self.delete()


async def reply(self, *args, **kwargs):
    delete_in = kwargs.pop('delete_in', None)
    await self._reply_(*args, **kwargs)
    if delete_in:
        await asyncio.sleep(int(delete_in))
        await self.delete()


async def respond(self, *args, **kwargs):
    delete_in = kwargs.pop('delete_in', None)
    await self._respond_(*args, **kwargs)
    if delete_in:
        await asyncio.sleep(int(delete_in))
        await self.delete()


Message.edit = edit
Message.reply = reply
Message.respond = respond
