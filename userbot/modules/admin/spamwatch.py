# Originally by @By_Azade
# Ported and adapted by: github.com/HitaloKun/TG-UBotX

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
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins,
                               ChannelParticipantsBots, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto, PeerChat,
                               MessageService, MessageActionChatAddUser)
from telethon.tl.functions.contacts import DeleteContactsRequest

from telethon.events import ChatAction, NewMessage
from userbot import BOTLOG, BOTLOG_CHATID, bot
from userbot import spamwatch


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


@bot.on(ChatAction())
@bot.on(NewMessage())
async def spam_watch_(event):
    users = await get_user_from_event(event)
    for user in users:
        ban = spamwatch.get_ban(user.id)
        if event.chat_id != event.from_id and ban:
            try:
                await event.client(
                    EditBannedRequest(
                        event.chat_id,
                        user,
                        BANNED_RIGHTS
                    )
                )
                if isinstance(event, events.NewMessage.Event):
                    await event.delete()
                else:
                    return
            except BadRequestError:
                return
        elif ban:
            await event.client(BlockRequest(user))
            await event.client(DeleteContactsRequest(id=[user]))
        else:
            return
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#SPAM_WATCH_BAN\n" + \
            f"USER: [{user.first_name}](tg://user?id={user.id})\n" + \
           (f"CHAT: {event.chat.title}(`{event.chat_id}`)" if event.chat_id != event.from_id else "")
        )

