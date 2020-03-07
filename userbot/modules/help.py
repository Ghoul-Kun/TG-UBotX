# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

import textwrap

from userbot.events import register

CAT_ITEMS = {}
HELP_ITEMS = {}


def add_help_item(command, category, description, examples, keywords=None):
    if category not in CAT_ITEMS:
        CAT_ITEMS.update({category: []})

    HELP_ITEMS.update({
        command: {
            "description": description,
            "examples": examples,
            "keywords": keywords
        }
    })

    CAT_ITEMS[category].append(command)


@register(outgoing=True, pattern=r"^\.help(?: |$)(.*)")
async def show_help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1)
    if args:
        if args in HELP_ITEMS:
            halp = HELP_ITEMS[args]

            help_message = f"**{args}** \n"
            help_message += f"{halp['description']} \n\n"
            help_message += "**Usage:**\n"
            help_message += textwrap.dedent(halp['examples']).strip()

            await event.edit(help_message)
        else:
            await event.edit("**Please specify a valid module name.**")
    else:
        categories = sorted(CAT_ITEMS.keys())

        categorized = []
        for cat in categories:
            cat_items = sorted(CAT_ITEMS[cat])
            msg = f"**{cat}** \n```{', '.join(cat_items)}```"
            categorized.append(msg)

        message = "**Please specify which module do you want help for!** \n\n" + \
            '\n\n'.join(categorized)
        await event.edit(message)
