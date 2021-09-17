


from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import ALIVE_NAME, CMD_HELP
from MYSTERIOUSBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND User"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


@bot.on(admin_cmd("ascii ?(.*)"))
@bot.on(sudo_cmd(pattern="ascii ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "яєρℓγ το αиγ ιмαgє😒🤐")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "Reply to media ιмαgє😒🤐")
        return
    chat = "@asciiart_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "Reply to actual мє∂נα ιмαgє.😒🤐")
        return
    legend = await edit_or_reply(event, "Wait making ASCII...🤓🔥🔥")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=164766745)
            )
            await event.client.send_message(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await legend.edit("`Please unblock @asciiart_bot and try again`")
            return
        if response.text.startswith("Forward"):
            await legend.edit(
                "`can you kindly disable your forward privacy settings for good?`"
            )
        else:
            await legend.delete()
            await event.client.send_file(
                event.chat_id,
                response.message.media,
                caption=f"**Image Type :** ASCII Art\n**Uploaded By :** {mention}",
            )
            await event.client.send_read_acknowledge(conv.chat_id)


@bot.on(admin_cmd(pattern="line ?(.*)"))
@bot.on(sudo_cmd(pattern="line ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "Reply to any мє∂ια message.😒🤐")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await edit_or_reply(event, "Reply to media message😒🤐")
        return
    chat = "@Lines50Bot"
    reply_message.sender
    if reply_message.sender.bot:
        await edit_or_reply(event, "Reply to actual мє∂ια message.😒🤐")
        return
    legend = await edit_or_reply(event, "`Processing`")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(reply_message)
            await conv.get_response()
            pic = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await legend.edit("Please unblock @Lines50Bot and try again")
            return
        await legend.delete()
        await event.client.send_file(
            event.chat_id,
            pic,
            caption=f"**Image Type :** LINE Art \n**Uploaded By :** {mention}",
        )

CmdHelp("ascii").add_command(
  'ascii', 'reply to any image file', 'Makes an image ascii style, try out your own'
).add_command(
  'line', 'reply to any image file', 'Makes an image in line style'
).add()
