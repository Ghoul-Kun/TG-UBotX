# Copyright (C) 2020 Adek Maulana.
# All rights reserved.

from humanize import naturalsize
from subprocess import PIPE, Popen

import re
import json
import wget
import os

from os.path import exists

from userbot import CMD_HELP
from userbot.events import register


def subprocess_run(cmd):
    reply = ''
    subproc = Popen(cmd, stdout=PIPE, stderr=PIPE,
                    shell=True, universal_newlines=True)
    talk = subproc.communicate()
    exitCode = subproc.returncode
    if exitCode != 0:
        reply += ('An error was detected while running the subprocess:\n'
                  f'exit code: {exitCode}\n'
                  f'stdout: {talk[0]}\n'
                  f'stderr: {talk[1]}')
        return reply
    return talk


@register(outgoing=True, pattern=r"^.mega(?: |$)(.*)")
async def mega_downloader(megadl):
    await megadl.edit("`Processing...`")
    textx = await megadl.get_reply_message()
    link = megadl.pattern_match.group(1)
    if link:
        pass
    elif textx:
        link = textx.text
    else:
        await megadl.edit("`Usage: .mega <mega url>`")
        return
    if not link:
        await megadl.edit("`No MEGA.nz link found!`")
    await mega_download(link, megadl)


async def mega_download(url, megadl):
    try:
        link = re.findall(r'\bhttps?://.*mega.*\.nz\S+', url)[0]
    except IndexError:
        await megadl.edit("`No MEGA.nz link found`\n")
        return
    cmd = f'bin/megadirect {link}'
    result = subprocess_run(cmd)
    try:
        data = json.loads(result[0])
    except json.JSONDecodeError:
        await megadl.edit("`Error: Can't extract the link`\n")
        return
    file_name = data['file_name']
    file_size = naturalsize(int(data['file_size']))
    file_url = data['url']
    file_hex = data['hex']
    file_raw_hex = data['raw_hex']
    if exists(file_name):
        os.remove(file_name)
    if not exists(file_name):
        await megadl.edit('Downloading...\n\n'
                          f'File: `{file_name}`\n'
                          f'Size: {file_size}\n'
                          '...')
        wget.download(file_url, out=file_name)
        if exists(file_name):
            await megadl.edit('Encrypting file...')
            encrypt_file(file_name, file_hex, file_raw_hex)
            await megadl.edit(f"`{file_name}`\n\n"
                              "Successfully downloaded...")
        else:
            await megadl.edit("Failed to download...")
    return


def encrypt_file(file_name, file_hex, file_raw_hex):
    os.rename(file_name, r"old_{}".format(file_name))
    cmd = ("cat 'old_{}' | openssl enc -d -aes-128-ctr -K {} -iv {} > '{}'"
           .format(file_name, file_hex, file_raw_hex, file_name))
    subprocess_run(cmd)
    os.remove(r"old_{}".format(file_name))
    return


add_help_item(
    "megadown",
    "Misc",
    "UserBot module to download files from MEGA.nz",
    """
    `.mega <mega url>`
    **Usage:** Reply to a mega link or paste your mega link to
    download the file into your userbot server
    Only support for *FILE*.
    """
)
