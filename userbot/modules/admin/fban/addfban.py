from userbot import is_mongo_alive
from userbot.events import register
from userbot.modules.admin.fban.fban_db import add_chat_fban


@register(outgoing=True, pattern=r"^\.addfban")
async def add_to_fban(chat):
    if not is_mongo_alive():
        await chat.edit("`Database connections failing!`")
        return
    await add_chat_fban(chat.chat_id)
    await chat.edit("`Added this chat under the Fbanlist!`")
