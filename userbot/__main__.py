from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module, start_assistant
from userbot import LOAD_PLUG, LOGS, MYSTERIOUSversion
from pathlib import Path
import asyncio
import telethon.utils
os.system("pip install -U telethon")

l2= Config.SUDO_COMMAND_HAND_LER
MYSTERIOUS_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/75e1eda1498620f0030ea.jpg"
l1 = Config.COMMAND_HAND_LER


LOAD_USERBOT = os.environ.get("LOAD_USERBOT", True)
LOAD_ASSISTANT = os.environ.get("LOAD_ASSISTANT", True)    

async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"MYSTERIOUS_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.BOT_USERNAME))
        print("Startup Completed")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print(f"""
╔════❰MYSTERIOUSBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - MYSTERIOUS
║┣⪼{MYSTERIOUS_PIC}
║┣⪼ CREATOR -@MY5T3R10U5_X
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")



# Join LegndBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@MYSTERIOUS_SUPPORT"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@MYSTERIOUS_EMPIRE"))
    except BaseException:
         pass




if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
