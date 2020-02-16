# Module originally made by: @By_Azade
# Ported and adapted for UBotX github.com/HitaloKun/TG-UBotX

import asyncio

from asyncio import sleep
from os import remove
from telethon import events
from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (MessageTooLongError,
                                          UserIdInvalidError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins,
                               ChannelParticipantsBots, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto, PeerChat)

from userbot import spamwatch
from userbot import BOTLOG, BOTLOG_CHATID, bot


BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


@bot.on(ChatAction)
async def spam_watch_(event):
    chat_id = event.chat_id
    ban = spamwatch.get_ban(chat_id)
    if event.user_joined or event.user_added:
        try:
            if ban:
                await event.client(
                EditBannedRequest(
                    event.chat_id,
                    user.id,
                    BANNED_RIGHTS
                )
            )
            else:
                return
        except BadRequestError:
            return
        banobj = spamwatch.get_ban(user.id)
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#SPAMWATCH_BAN\n"
                f"**USER:** [{user.first_name}](tg://user?id={user.id})\n"
                f"**CHAT:** {event.chat.title}(`{event.chat_id}`)"
                f"**Reason:** `{banobj.reason}`"
            )