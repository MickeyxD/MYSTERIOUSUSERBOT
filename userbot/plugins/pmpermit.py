import asyncio
import io
import os
import time
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon import events, functions, Button, custom
from telethon.tl.functions.users import GetFullUserRequest

from . import *
from userbot import ALIVE_NAME, PM_MSG, LEGEND_ID
from userbot.Config import Config
from LEGENDBOT.utils import admin_cmd
from userbot.cmdhelp import CmdHelp
from userbot.plugins.sql_helper import pmpermit_sql as pm_sql


WARN_PIC = Config.PM_PIC or "https://telegra.ph/file/fcfb3d70fceb0c6ddf151.jpg"
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
PM_ON_OFF = Config.PM_DATA
CSTM_PMP = Config.PM_MSG or "**You Have Trespassed To My Master's PM!\nThis Is Illegal And Regarded As Crime.**"
LEGEND_ZERO = "Go get some sleep retard. \n\n**Blocked !!**"
LEGEND_FIRST = (
    "**🔥 LegendBo† Prîvã†é Sêçürïty Prø†öçõl 🔥**\n\nThis is to inform you that "
    "{} is currently unavailable.\nThis is an automated message.\n\n"
    "{}\n\n**Please Choose Why You Are Here!!**".format(legend_mention, CSTM_PMP)
)
if Var.PRIVATE_GROUP_ID is not None:
    @borg.on(admin_cmd(pattern="block|.blk ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if chat.id == 1938996006:
                await event.edit(
                    "You tried to block my master😡. GoodBye for 100 seconds!🥱😴😪💤"
                )
                time.sleep(100)
            else:
                if pmpermit_sql.is_approved(chat.id):
                    pmpermit_sql.disapprove(chat.id)
                    await event.edit(
                        "gєτ ℓοѕτ мγ мαѕτєя нαѕ ϐℓοϲκє∂ υ!!.\nϐℓοϲκє∂ [{}](tg://user?id={})".format(
                            firstname, chat.id
                        )
                    )
                    await asyncio.sleep(3)
                    await event.client(functions.contacts.BlockRequest(chat.id))
        elif event.is_group:
            if chat.id == 1938996006:
                await event.edit(
                    "You tried to block my master😡. GoodBye for 100 seconds!🥱😴😪💤"
                )
                time.sleep(100)
            else:
                reply_s = await event.get_reply_message()
                if not reply_s:
                    await event.edit('`Reply To User To Block Him !`')
                    return
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                if pmpermit_sql.is_approved(event.chat_id):
                    pmpermit_sql.disapprove(event.chat_id)
                await event.edit("ϐℓοϲκє∂ [{}](tg://user?id={})".format(firstname, reply_s.sender_id))
                await event.client(functions.contacts.BlockRequest(reply_s.sender_id))
                await asyncio.sleep(3)
                await event.delete()
        
        
if PM_ON_OFF != "DISABLE":
    @bot.on(events.NewMessage(outgoing=True))
    async def auto_approve_for_out_going(event):
        if event.fwd_from:
            return
        if not event.is_private:
            return
        chat_ids = event.chat_id
        sender = await event.client(GetFullUserRequest(await event.get_input_chat()))
        first_name = sender.user.first_name
        if chat_ids == bot.uid:
            return
        if sender.user.bot:
            return
        if sender.user.verified:
            return
        if PM_ON_OFF == "DISABLE":
            return
        if str(event.chat_id) in DEVLIST:
            return
        if not pm_sql.is_approved(event.chat_id):
            if not event.chat_id in PM_WARNS:
                pm_sql.approve(event.chat_id, "outgoing")
                
    @bot.on(admin_cmd(pattern="(a|approve|allow)$"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        if event.is_private:
            replied_user = await event.client(GetFullUserRequest(await event.get_input_chat()))
            firstname = replied_user.user.first_name
            if not pm_sql.is_approved(event.chat_id):
                if event.chat_id in PM_WARNS:
                    del PM_WARNS[event.chat_id]
                if event.chat_id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[event.chat_id].delete()
                    del PREV_REPLY_MESSAGE[event.chat_id]
                pm_sql.approve(event.chat_id, "Approved")
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(firstname, event.chat_id)
                )
                await asyncio.sleep(3)
                await event.delete()
            elif pm_sql.is_approved(event.chat_id):
                hel_ = await event.edit('Already In Approved List!!')
                await asyncio.sleep(3)
                await hel_.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit('Reply to someone to approve them !!')
                return
            if not pm_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pm_sql.approve(reply_s.sender_id, "Approved")
                await event.edit(
                        "Approved to pm [{}](tg://user?id={})".format(firstname, reply_s.sender_id)
                    )
                await asyncio.sleep(3)
                await event.delete()
            elif pm_sql.is_approved(reply_s.sender_id):
                await event.edit('User Already Approved !')
                await event.delete()

    @bot.on(admin_cmd(pattern="(da|disapprove|disallow)$"))
    async def dapprove(event):
        if event.fwd_from:
            return
        if event.is_private:
            replied_user = await event.client(GetFullUserRequest(await event.get_input_chat()))
            firstname = replied_user.user.first_name
            if str(event.chat_id) in DEVLIST:
                await event.edit("**Unable to disapprove this user. Seems like God !!**")
                return
            if pm_sql.is_approved(event.chat_id):
                pm_sql.disapprove(event.chat_id)
                await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(firstname, event.chat_id)
                )
                await asyncio.sleep(3)
                await event.delete()
            elif not pm_sql.is_approved(event.chat_id):
                led = await event.edit("I don't think he was approved !!")
                await asyncio.sleep(3)
                await led.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit("Reply to someone to Disapprove them !!")
                return
            if str(reply_s.sender_id) in DEVLIST:
                await event.edit("**Unable to disapprove this user. Seems like God !!**")
                return
            if pm_sql.is_approved(reply_s.sender_id):
                replied_user = await event.client(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pm_sql.disapprove(reply_s.sender_id)
                await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(firstname, reply_s.sender_id)
                )
                await asyncio.sleep(3)
                await event.delete()
            elif not pm_sql.is_approved(reply_s.sender_id):
                await event.edit('Not even in my approved list.')
                await event.delete()    
                
                
    @bot.on(admin_cmd(pattern="listapproved$"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pm_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if not event.is_private:
            return
        if event.sender_id == bot.uid:
            return
        if str(event.sender_id) in DEVLIST:
            return
        if Config.LOGGER_ID is None:
            await bot.send_message(bot.uid, "Please Set `LOGGER_ID` For Working Of Pm Permit")
            return
        message_text = event.message.raw_text
        chat_id = event.sender_id
        if LEGEND_FIRST == message_text:
            return
        sender = await bot.get_entity(chat_id)
        if chat_id == bot.uid:
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if PM_ON_OFF == "DISABLE":
            return
        if pm_sql.is_approved(chat_id):
            return
        if not pm_sql.is_approved(chat_id):
            await do_pm_permit_action(chat_id, event)
                                       
    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == Config.MAX_FLOOD_IN_PM:
            r = await event.reply(LEGEND_ZERO)
            await asyncio.sleep(3)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PM\n\n"
            the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Message Counts: {PM_WARNS[chat_id]}\n"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True,
                )
                return
            except BaseException:
                pass
        
        botusername = Config.BOT_USERNAME
        tap = await bot.inline_query(botusername, "pm_warn")
        legend_ = await tap[0].click(event.chat_id)
        PM_WARNS[chat_id] += 1
        chat_id = chat_id
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = legend_

NEEDIT = Config.INSTANT_BLOCK
if NEEDIT == "ENABLE":
    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        event.message.message
        event.message.media
        event.message.id
        event.message.to_id
        chat_id = event.chat_id
        sender = await bot.get_entity(chat_id)
        if chat_id == bot.uid:
            return
        if chat_id == 1938996006:
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if not pm_sql.is_approved(chat_id):
            await bot(functions.contacts.BlockRequest(chat_id))


@bot.on(events.NewMessage(incoming=True, from_users=(1938996006)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pm_sql.is_approved(chat.id):
            pm_sql.approve(
                chat.id, "**My Boss iz here.... It's your lucky day nibba😏**"
            )
            await borg.send_message(chat, "**Welcome My Master! Lucky you!!😏**")


CmdHelp("pm_permit").add_command(
  "allow", "<in pm>", "Approves the user in which pm cmd is used."
).add_command(
  "disallow", "<in pm>", "Disapprove User to PM you."
).add_command(
  "block", "<in pm>", "Blocks the user"
).add_command(
  "listapproved", None, "Sends the list of all users approved by LegendBot"
).add_info(
  "PM SECURITY"
).add_warning(
  "✅ Harmless Module."
).add()
