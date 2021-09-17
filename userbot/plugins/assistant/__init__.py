# MYSTERIOUSBOT Assistant
from . import *
from telethon import Button, custom

from userbot import bot
from userbot import ALIVE_NAME
OWNER_NAME = ALIVE_NAME
OWNER_ID = bot.uid


async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
