# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, bot
from userbot.events import register
from ..help import add_help_item


@register(outgoing=True, pattern="^.ubo$")
async def shalom(e):
    await e.edit(
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰❄️❄️❄️❄️❄️❄️💰"
        "\n💰❄️💰💰💰💰💰💰💰"
        "\n💰❄️💰💰💰💰💰💰💰"
        "\n💰❄️💰💰💰💰💰💰💰"
        "\n💰💰❄️❄️❄️❄️❄️❄️💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰💰❄️❄️💰❄️❄️💰💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰❄️❄️❄️❄️❄️💰💰"
        "\n💰❄️💰💰💰💰💰❄️💰"
        "\n💰❄️💰💰💰💰💰❄️💰"
        "\n💰❄️💰💰💰💰💰❄️💰"
        "\n💰💰❄️❄️❄️❄️❄️💰💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰❄️💰💰💰💰💰❄️💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰❄️💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰❄️💰💰💰❄️❄️💰💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰💰❄️❄️💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰💰💰💰❄️💰💰💰💰"
        "\n💰💰💰💰❄️💰💰💰💰"
        "\n💰💰💰💰❄️💰💰💰💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰💰❄️❄️💰❄️❄️💰💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰❄️💰💰💰❄️❄️💰💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰❄️💰💰❄️💰💰❄️💰"
        "\n💰💰❄️❄️💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰💰💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰❄️❄️❄️❄️❄️❄️❄️💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰❄️💰"
        "\n💰💰💰💰💰💰💰💰💰")


add_help_item(
    "ubotx",
    "Fun",
    "UBotX is the best.",
    """
.ubo\
\nUsage: gives a nice UBOT as output.
    """
)



