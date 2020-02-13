import asyncio

from telethon.tl.types import MessageEntityMentionName, MessageEntityMention

from userbot import bot
from userbot import GBAN_GROUP
from ..help import add_help_item
from userbot.events import register
from userbot.utils import parse_arguments, get_user_from_event

@register(outgoing=True, pattern=r"^\.fban(\s+[\S\s]+|$)")
async def fedban_all(msg):

    reply_message = await msg.get_reply_message()

    params = msg.pattern_match.group(1) or ""
    args, text = parse_arguments(params, ['reason'])

    if reply_message:
        banid = reply_message.from_id
        banreason = args.get('reason', '[spam]')
    else:
        banreason = args.get('reason', '[fban]')
        if text.isnumeric():
            banid = int(text)
        elif msg.message.entities:
            ent = await bot.get_entity(text)
            if ent: banid = ent.id

    if not banid:
        return await msg.edit("**No user to ban**")

    failed = dict()
    count = 1

    for GBAN_GROUP:
        async with bot.conversation(GBAN_GROUP) as conv:
            await conv.send_message(f"/fban {banid} {banreason}")
            resp = await conv.get_response()
            await bot.send_read_acknowledge(conv.chat_id)
            if "New FedBan" not in resp.text:
                failed[GBAN_GROUP] = str(conv.chat_id)
            else:
                count += 1
                await msg.reply("**Fbanned in " + str(count) + " feds!**", delete_in=3)
            # Sleep to avoid a floodwait.
            # Prevents floodwait if user is a fedadmin on too many feds
            await asyncio.sleep(0.2)

    if failed:
        failedstr = ', '.join([f'`i`' in failed.keys()])
        await msg.reply(f"**Failed to fban in {failedstr}**")
    else:
        await msg.reply("**Fbanned in all feds!**")

    msg.delete()


add_help_item(
    "fban",
    "Admin",
    "Give FedBan through userbot",
    """
.fban [ID/username] [reason]
.unfban [ID/username] [reason]
    """
)
