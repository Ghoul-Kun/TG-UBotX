# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

import tempfile
from io import BytesIO

from ..help import add_help_item
from userbot import FACE_API_KEY, FACE_API_URL
from userbot.events import register
from userbot.modules.fun import resize_photo
from userbot.utils.deepfryer import deepfry


@register(outgoing=True, pattern=r"^\.deepfry")
async def fry(message):
    """ For .deepfry command, fries stickers or creates new ones. """
    reply_message = await message.get_reply_message()

    photo = BytesIO()
    if message.media:
        await message.edit("Frying...")
        await message.download_media(photo)
    elif reply_message.media:
        await message.edit("Frying...")
        await reply_message.download_media(photo)
    else:
        await message.edit("Can't deepfry nothing")
        return

    if photo:
        image = await resize_photo(photo)
        image = await deepfry(image, token=FACE_API_KEY, api_url=FACE_API_URL)

        temp = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        temp.close()
        image.save(temp.name)

        await message.delete()
        await message.client.send_file(message.chat.id, file=temp.name, reply_to=reply_message)


add_help_item(
    "deepfry",
    "Fun",
    "Deeprys the selected photo.",
    """
.deepfry In response to a photo
    """
)
