import base64
from io import BytesIO

from PIL import Image

from userbot.events import register
from userbot.utils.thonkify_dict import thonkifydict
from userbot import CMD_HELP


@register(outgoing=True, pattern='.thonk(?: |$)(.*)')
async def thonkify(thonk):
    """ Thonkifies the requested text """
    textx = await thonk.get_reply_message()
    message = thonk.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await thonk.edit("`Give me something to thonkify`")
        return

    if len(message) > 39:
        await thonk.edit("Can't thonk messages over 39 characters -_-")

    tracking = Image.open(BytesIO(base64.b64decode(
        'iVBORw0KGgoAAAANSUhEUgAAAAYAAAOACAYAAAAZzQIQAAAALElEQVR4nO3BAQ0AAADCoPdPbQ8HFAAAAAAAAAAAAAAAAAAAAAAAAAAAAPwZV4AAAfA8WFIAAAAASUVORK5CYII=')))  # base64 encoded empty image(but longer)

    # remove characters thonkify can't parse
    for character in message:
        if character not in thonkifydict:
            message = message.replace(character, "")

    # idk PIL. this part was untouched and ask @devrism for better explanation. According to my understanding,
    # Image.new creates a new image and paste "pastes" the character one by one comparing it with "value" variable
    x = 0
    y = 896
    image = Image.new('RGBA', [x, y], (0, 0, 0, 0))
    for character in message:
        value = thonkifydict.get(character)
        addedimg = Image.new('RGBA', [x + value.size[0] + tracking.size[0], y], (0, 0, 0, 0))
        addedimg.paste(image, [0, 0])
        addedimg.paste(tracking, [x, 0])
        addedimg.paste(value, [x + tracking.size[0], 0])
        image = addedimg
        x = x + value.size[0] + tracking.size[0]

    maxsize = 1024, 896
    if image.size[0] > maxsize[0]:
        image.thumbnail(maxsize, Image.ANTIALIAS)

    # put processed image in a buffer and then upload cause async
    with BytesIO() as buffer:
        buffer.name = 'image.png'
        image.save(buffer, 'PNG')
        buffer.seek(0)
        await thonk.delete()
        await thonk.client.send_file(thonk.chat_id, file=buffer, reply_to=textx)


CMD_HELP.update({
    "thonkify":
    ".thonk (message)
    \n\nOr, in reply to a message
    \n.thonk"
})
