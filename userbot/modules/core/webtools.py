# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from telethon import functions

from ..help import add_help_item
from userbot.events import register


@register(outgoing=True, pattern=r"^\.speedtest$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Running speed test ...`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit(
        "**Speedtest Results:** \n\n"
        "**Download** "
        f"`{speed_convert(result['download'])}` \n"
        "**Upload** "
        f"`{speed_convert(result['upload'])}` \n"
        "**Ping** "
        f"`{result['ping']}` \n"
        "**ISP** "
        f"`{result['client']['isp']}`"
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern=r"^\.dc$")
async def neardc(event):
    """ For .dc command, get the nearest datacenter information. """
    result = await event.client(functions.help.GetNearestDcRequest())
    await event.edit(f"**Country:** `{result.country}`\n"
                     f"**Nearest Datacenter:** `{result.nearest_dc}`\n"
                     f"**This Datacenter:** `{result.this_dc}`")


@register(outgoing=True, pattern=r"^\.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong!`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit("🏓 **Pong!**\n`%sms`" % (duration))


add_help_item(
    "webtools",
    "Core",
    "Some useful web tools",
    """
    `.ping`
    **Usage:** Shows how long it takes to ping your bot.

    `.speedtest`
    **Usage:** Does a speedtest and shows the results.

    `.dc`
    **Usage:** Finds the nearest datacenter from your server.
    """
)
