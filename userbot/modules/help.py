# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import textwrap

from userbot import CMD_HELP
from userbot.events import register

CAT_ITEMS = {}


@register(outgoing=True, pattern=r"^\.help(?: |$)(.*)")
async def show_help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1)
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("**Please specify a valid module name.**", delete_in=3)
    else:
        categories = list(CAT_ITEMS.keys())
        categories.sort()

        categorized = []
        for cat in categories:
            cat_items = sorted(CAT_ITEMS[cat])
            msg = f"**{cat}** \n```{', '.join(cat_items)}```"
            categorized.append(msg)

        message = "**Please specify which module do you want help for!** \n\n" + '\n\n'.join(categorized)
        await event.edit(message)
