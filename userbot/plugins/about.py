from . import *
import asyncio
import random
from telethon import events
from LEGENDBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"
from userbot.Config import Config
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG
# Thanks to LEGEND BRO.. 
# animation Idea by @Its_LegendBoy (op coder)
# Kang with credits else gay...
# alive.py for

edit_time = 5
""" =======================CONSTANTS====================== """
file1="https://telegra.ph/file/2d41a6b1b3713579c63c2.jpg"
file2="https://telegra.ph/file/9fb5502699714b8eabca3.jpg"
file3="https://telegra.ph/file/f04dcb487d52b97c36a54.jpg"
file4="https://telegra.ph/file/bac71ea81bebea8332f86.jpg"
file5="https://telegra.ph/file/56330a785e4f2a5919e1c.jpg"""" =======================CONSTANTS====================== """
pm_caption = "     **🔥『Lêɠêɳ̃dẞø†』🔥**\n\n"
pm_caption += f"**{CUSTOM_ALIVE_TEXT}**\n\n"
pm_caption += "༆༄🎀🌹Åbôût Mê \n\n"
pm_caption += "💫💫**✞︎t͛ẞ̸ Lêɠêɳ̃dẞø†**💫💫 >>》 V•2.Ø\n"
pm_caption += "😇😇**Lêɠêɳ̃d**😇😇   >>》 [Owner](https://t.me/Its_LegendBoy)\n"
pm_caption += f"🔰🔰**Mâßtêř**🔰🔰  >>》 {legend_mention}\n"
pm_caption += "❣❣ **𝖑𝖊ɠêɳ̃dẞø✞︎**❣❣ >>》 [𝕲𝖗ουρ](https://t.me/Legend_Userbot)\n\n"
pm_caption += "🎊🎊 **Řepô**🎊🎊  >>》 [𝕽єρο](https://github.com/LEGEND-OS/LEGENDBOT)\n\n"
pm_caption += "[....▄███▄███▄\n....█████████\n.......▀██❣🌹💫😇💫🌹❣███▀\n...............▀█▀\n](https://t.me/Its_LegendBoy)\n\n"
@borg.on(admin_cmd(pattern=r"abot"))
@bot.on(sudo_cmd(pattern="abot$", allow_sudo=True))
async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)
    
    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("about").add_command(
    'abot', None , 'BEST alive command'
).add()
