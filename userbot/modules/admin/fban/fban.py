import asyncio

from telethon.tl.types import MessageEntityMentionName, MessageEntityMention

from userbot import is_mongo_alive, bot
from userbot.events import register
from userbot.modules.admin.fban.fban_db import get_fban
from userbot.utils import parse_arguments, get_user_from_event


@register(outgoing=True, pattern=r"^\.fban(\s+[\S\s]+|$)")
async def fedban_all(msg):
    if not is_mongo_alive():
        await msg.edit("`Database connections failing!`")
        return
    textx = await msg.get_reply_message()
    if textx:
        try:
            banreason = "[userbot] "
            banreason += banreason.join(msg.text.split(" ")[1:])
            if banreason == "[userbot]":
                raise TypeError
        except TypeError:
            banreason = "[userbot] fban"
    else:
        banid = msg.text.split(" ")[1]
        if banid.isnumeric():
            # if its a user id
            banid = int(banid)
        else:
            # deal wid the usernames
            if msg.message.entities is not None:
                probable_user_mention_entity = msg.message.entities[0]
 
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                ban_id = probable_user_mention_entity.user_id
        try:
            banreason = "[userbot] "
            banreason += banreason.join(msg.text.split(" ")[2:])
            if banreason == "[userbot]":
                raise TypeError
        except TypeError:
            banreason = "[userbot] fban"
    count = 1
    fbanlist = []
    x = (await get_fban())
    for i in x:
        fbanlist.append(i["chatid"])
    for bangroup in fbanlist:

    if not banid:
        return await msg.edit("**No user to ban**")

    failed = dict()
    count = 1
    fbanlist = [i['chat_id'] for i in await get_fban()]

    for bangroup in fbanlist:
        async with bot.conversation(bangroup) as conv:
            await conv.send_message(f"/fban {banid} {banreason}")
            resp = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
            if "New FedBan" not in resp.text:
                failed[bangroup] = str(conv.chat_id)
            else:
                count += 1
                await msg.edit("`Fbanned on " + str(count) + " feds!`")
            # Sleep to avoid a floodwait.
            # Prevents floodwait if user is a fedadmin on too many feds
            await asyncio.sleep(0.2)
    if failed:
        failedstr = ""
        for i in failed.keys():
            failedstr += failed[i]
            failedstr += " "
        await msg.reply(f"`Failed to fban in {failedstr}`")
    else:
        await msg.reply("`Fbanned in all feds!`")
