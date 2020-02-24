import asyncio

from ..help import add_help_item
from userbot.events import register


@register(outgoing=True, pattern='^\.think(?: |$)(.*)')
async def think(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    await event.edit(input_str)
    animation_chars = [
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING",
            "THI&K#N₹",
            "T+IN@I?G",
            "¿H$NK∆NG",
            "¶H×NK&N*",
            "NGITHKIN",
            "T+I#K@₹G",
            "THINKING... 🤔"
        ]

        for i in animation_ttl:
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 35])


add_help_item(
    "think",
    "Fun",
    "Think about it yourself.",
    """
    `.think`
    """
)
