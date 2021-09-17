from telethon import events
from . import *
from userbot import ALIVE_NAME
from userbot import bot
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"
PM_IMG = "https://telegra.ph/file/2c9be46a59b1497553f06.jpg"
pm_caption = "➥ αssísԵαղԵ ís օղlíղҽ \n\n"
pm_caption += "➥ ѕγѕτєм ѕτατѕ\n"
pm_caption += "➥ τєℓєτнοи νєяѕιοи: `1.15.0` \n"
pm_caption += "➥ ℓєgєϐ∂ϐοτ: `3.8.6` \n"
pm_caption += "➥ ∂αταϐαѕє ѕτατυѕ: `Functional`\n"
pm_caption += "➥ ϲυяяєиτ ϐяαиϲн: `master`\n"
pm_caption += f"➥ νєяѕιοи : `2.0`\n"
pm_caption += f"➥ мγ ϐοѕѕ: {DEFAULTUSER} \n"
pm_caption += "➥ нєяοκυ ∂αταϐαѕє: `AWS - Working Properly`\n\n"
pm_caption += "➥ **𝓛𝓲𝓬𝓮𝓷𝓼𝓮** : [GNU General Public License v3.0](github.com/MYSTERIOUS-OS/LEGENBOT/blob/master/LICENSE)\n"
pm_caption += "➥ 𝓒𝓸𝓹𝔂𝓻𝓲𝓼𝓱𝓽 : By [lҽցҽղժճօԵ](https://t.me/MYSTERIOUS_EMPIRE)\n"
pm_caption += "[Assistant By ℓεɠεn∂](https://t.me/MY5T3R10U5_X)"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
