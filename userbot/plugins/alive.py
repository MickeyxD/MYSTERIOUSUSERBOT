import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from userbot.Config import Config
from telethon import version
from userbot import ALIVE_NAME, StartTime, MYSTERIOUSversion
from MYSTERIOUSBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from . import *
async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "✞︎t͛ẞ̸ Mysterious 🇮🇳"
MYSTERIOUS_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "ℓєgєи∂ Choice 𝖑𝖊ɠêɳ̃dẞø✞︎"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@MYSTERIOUS_EMPIRE"

Legend = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={Legend})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  MYSTERIOUS_IMG:
        MYSTERIOUS_caption = f"🔥🔥MysteriousBօt ɨs օռʟɨռɛ🔥🔥\n"
        
        MYSTERIOUS_caption += f"        **♥ẞø† ẞ✞︎α†µѕ** \n"
        MYSTERIOUS_caption += f"╭──────────────\n"
        MYSTERIOUS_caption += f"┣─•⚜️• **Øաղ̃ҽ̈ɾ**          : {legend_mention}\n"
        MYSTERIOUS_caption += f"┣─•📍• **MysteriousBot**   : {MYSTERIOUSversion}\n"
        MYSTERIOUS_caption += f"┣─•📍• **†ҽ̀lҽ́ƭhøղ̃**     : `{version.__version__}`\n"
        MYSTERIOUS_caption += f"┣─•📍• **𝚄ρƭเɱε**         : `{uptime}`\n"
        MYSTERIOUS_caption += f"┣─•📍• **𝚂𝚞𝚙𝚙𝚘𝚛𝚝**           : [𝙶𝚛𝚘𝚞𝚙](t.me/MYSTERIOUS_EMPIRE)\n"
        MYSTERIOUS_caption += f"┣─•📍• **𝚄𝚙𝚍𝚊𝚝𝚎**  : [𝙲𝚑𝚊𝚗𝚗𝚎𝚕]{http://t.me//MYSTERIOUS_SUPPORT}\n" 
        MYSTERIOUS_caption += f"╰──────────────"  

        await alive.client.send_file(
            alive.chat_id, MYSTERIOUS_IMG, caption=MYSTERIOUS_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         𝕭𝖔𝖙 𝕾𝖙𝖆𝖙𝖚𝖘\n"
            f"•⚡• 𝕿єℓєτнοи    : `{version.__version__}`\n"
            f"🇮🇳 ℓєgєи∂ϐοτ  : `{MYSTERIOUSversion}`\n"
            f"🇮🇳 υρτιмє        : `{uptime}`\n"
            f"🔱 ɱαรƭεɾ        : {mention}\n"
            f"🔱 σωɳεɾ         : [ℓєgєи∂](t.me/MYSTERIOUS_SUPPORT)\n"
        )


botname = Config.BOT_USERNAME

CmdHelp("alive").add_command(
    'alive', None, 'υѕє αи∂ ѕєє'
).add()
