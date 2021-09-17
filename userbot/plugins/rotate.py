import os
#MADE BY Legend DONT KANG

from userbot.cmdhelp import CmdHelp
#MADE BY Legend DONT KANG
#MADE BY Legend DONT KANG
from telethon.tl.types import MessageMediaPhoto
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import bot 
from userbot import bot as bot
import os , shutil

from PIL import Image
sedpath = "./LEGEND_Logo/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
@bot.on(admin_cmd(pattern=r"rotate"))
async def hmm(event):
    s=event.text
    h=s[8:]
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    await event.delete()
    sed = await event.get_reply_message()
    if isinstance(sed.media, MessageMediaPhoto):
        img = await bot.download_media(sed.media, sedpath)
    elif "image" in sed.media.document.mime_type.split("/"):
        img = await bot.download_media(sed.media, sedpath)
    else:
        await event.edit("Reply To Image")
        return
    window_name = 'Made By Legend'
    img = Image.open(img)
    rotate_img= img.rotate(int(h))
    rotate_img.save("Legend.png")
    await event.client.send_file(event.chat_id, "Legend.png", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(sedpath)
    os.remove("Legend.png")
    
    
    
CmdHelp("rotate").add_command(
    "rotate", "reply to image", ".rotate reply to any image to turn pic"
).add()
