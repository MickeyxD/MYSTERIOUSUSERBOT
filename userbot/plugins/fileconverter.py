"""plugin made for reading nd  exploting message in tg {i}reveal <reply to file>"""
# originally made by @ItzSjDude All Rights reserved!!
#  Added Paste System by @danish_00
# All Credits - @ItzSjDude  #Added Paste System by @danish_00
# @ItzSjDude
# @ItzSjDude


import os, requests, re
import asyncio
import time
from datetime import datetime

from MYSTERIOUSBOT.utils import admin_cmd, edit_or_reply, sudo_cmd, sudo_cmd , edit_or_reply
from userbot.cmdhelp import CmdHelp
from . import *
@bot.on(admin_cmd(pattern=r"open", outgoing=True))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("Reading file...")
    if len(c) >= 4096:            
            await event.edit("output file too large lemme paste it 😜😜")#hehe
            out = c
            url = "https://del.dog/documents"
            r = requests.post(url, data=out.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
            await event.edit(
                f" Output file is too large Not supported By Telegram\n**So Pasted to** [Dog Bin]({url}) 😁😁", link_preview=False)            
            await a.delete()
    else:
        await event.client.send_message(event.chat_id, f"{c}")
        await a.delete()
    os.remove(b)


@bot.on(admin_cmd(pattern="doc ?(.*)"))
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.edit("reply to text message as .ttf <file name>")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.edit("reply to text message as .doc <file name.extension>")



thumb_image_path = Config.TMP_DOWNLOAD_DIRECTORY + "thumb_image.jpg"


@bot.on(admin_cmd(pattern="stoi"))
@bot.on(sudo_cmd(pattern="stoi", allow_sudo=True))
async def danish(hehe):
    if hehe.fwd_from:
        return
    thumb = None
    reply_to_id = hehe.message.id
    if hehe.reply_to_msg_id:
        reply_to_id = hehe.reply_to_msg_id
    cobra = await edit_or_reply(hehe, "Converting.....")
    
  
    input_str = "dc.jpeg"
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if cobra.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await cobra.get_reply_message()
      
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await hehe.client.download_media(
            reply_message,
            downloaded_file_name
        )
      
        try:
            thumb = await reply_message.download_media(thumb=-1)
        except Exception:
            thumb = thumb
        if os.path.exists(downloaded_file_name):
            
            dc = await hehe.client.send_file(
                hehe.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=reply_message,
                thumb=thumb
                
            )
            
            os.remove(downloaded_file_name)
            await cobra.delete()
        else:
            await cobra.edit("Something went wrong")
    else:
        await cobra.edit("reply to a non animated sticker")

  
  
  #hehe
  
@bot.on(admin_cmd(pattern="itos"))
@bot.on(sudo_cmd(pattern="itos", allow_sudo=True))
async def teamcobra(hehe):
    if hehe.fwd_from:
        return
    thumb = None
    reply_to_id = hehe.message.id
    if hehe.reply_to_msg_id:
        reply_to_id = hehe.reply_to_msg_id
    cobra = await edit_or_reply(hehe, "Converting.....")
    
  
    input_str = "dc.webp"
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if cobra.reply_to_msg_id:
        start = datetime.now()
        file_name = input_str
        reply_message = await cobra.get_reply_message()
      
        to_download_directory = Config.TMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await hehe.client.download_media(
            reply_message,
            downloaded_file_name
        )
      
        try:
            thumb = await reply_message.download_media(thumb=-1)
        except Exception:
            thumb = thumb
        if os.path.exists(downloaded_file_name):
            
            dc = await hehe.client.send_file(
                hehe.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=True,
                allow_cache=False,
                reply_to=reply_message,
                thumb=thumb
                
            )
            
            os.remove(downloaded_file_name)
            await cobra.delete()
        else:
            await cobra.edit("Something went wrong")
    else:
        await cobra.edit("reply to a non animated sticker")

  

CmdHelp("fileconverter").add_command(
    "open", None, "open files as text "
).add_command(
    ".doc <file name.extension> <reply to any text/media>", None, "Create a document of anything (example:- .doc dc.mp4, .doc dc.txt, .doc dc.webp)"
).add_command(
    ".stoi", None, "★  Convert sticker to image"
).add_command(
    ".itos", None, "Convert Image to Sticker"
).add()
