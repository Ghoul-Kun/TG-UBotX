# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# This module originally created by @spechide https://github.com/SpEcHiDe/UniBorg/blob/master/stdplugins/create_private_group.py
# Port to paperplane by @afdulfauzan and adapted to UBotX by @HitaloKun

from telethon.tl import functions, types
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import (PeerChannel, ChannelParticipantsAdmins,
                               ChatAdminRights, ChatBannedRights,
                               MessageEntityMentionName, MessageMediaPhoto,
                               ChannelParticipantsBots)
from userbot.events import register
from ..help import add_help_item


@register(outgoing=True, pattern="^\.create (b|g|c)(?: |$)(.*)")
async def telegraphs(grop):
    """ For .create command, Creating New Group & Channel """
    if not grop.text[0].isalpha() and grop.text[0] not in ("/", "#", "@", "!"):
        if grop.fwd_from:
            return
        type_of_group = grop.pattern_match.group(1)
        group_name = grop.pattern_match.group(2)
        if type_of_group == "b":
            try:
                result = await grop.client(functions.messages.CreateChatRequest(  # pylint:disable=E0602
                    users=["@MissRose_BOT"],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name
                ))
                created_chat_id = result.chats[0].id
                admin = chat.admin_rights
                creator = chat.creator
                rights = ChatAdminRights(
                                add_admins=True,
                                invite_users=True,
                                change_info=True,
                                ban_users=True,
                                delete_messages=True,
                                pin_messages=True)
                user_id = "@MissRose_BOT"
                rank = "Bot"
                await grop.client(EditAdminRequest(
                                        created_chat_id,
                                        user_id, 
                                        rights,
                                        rank 
                                        ))
                ))
                result = await grop.client(functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,

                await grop.edit("Your {} Group Created Successfully. Click [{}]({}) to join".format(group_name, group_name, result.link))
            except Exception as e:  # pylint:disable=C0103,W0703
                await grop.edit(str(e))
        elif type_of_group == "g" or type_of_group == "c":
            try:
                r = await grop.client(functions.channels.CreateChannelRequest(  # pylint:disable=E0602
                    title=group_name,
                    about="Welcome to this Channel",
                    megagroup=False if type_of_group == "c" else True
                ))
                created_chat_id = result.chats[0].id
                result = await grop.client(functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                ))
                await grop.edit("Your {} Group/Channel Created Successfully. Click [{}]({}) to join".format(group_name, group_name, result.link))
            except Exception as e:  # pylint:disable=C0103,W0703
                await grop.edit(str(e))


add_help_item(
    "create",
    "Me",
    "Creating new group & channel",
    """
    `.create g`
    **Usage:** Create a private Group.

    `.create b`
    **Usage:** Create a group with Bot.

    `.create c`
    **Usage:** Create a channel.
    """
)
