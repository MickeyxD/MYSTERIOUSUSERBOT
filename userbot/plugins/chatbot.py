import random
from telethon import events
from telethon.utils import get_display_name

from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.utils import edit_or_reply, admin_cmd, eor, delete_MYSTERIOUS

from userbot.helpers.events import get_user_from_event
from userbot.plugins.sql_helper.chatbot_sql import (
    addai,
    get_all_users,
    get_users,
    is_added,
    remove_ai,
    remove_all_users,
    remove_users,
)
from userbot.plugins.sql_helper.globalss import gvarstatus


tired_response = [
    "I am little tired, Please give me some rest",
    "Who are you to ask me questions Continuously",
    "Leave me alone for some times",
    "Time to Sleep, I will get back to you soon",
    "I have a job to do, Come back later",
    "I need to rest, leave me alone for some times",
    "I am not feeling well, Please Come back later",
]


@bot.on(admin_cmd(pattern=r"addai ?(.*)"))
async def add_chatbot(event):
    "To enable ai for the replied person"
    if event.reply_to_msg_id is None:
        return await edit_or_reply(
            event, "`Reply to a User's message to activate ai on `"
        )
    catevent = await edit_or_reply(event, "`Adding ai to user...`")
    user, rank = await get_user_from_event(event, catevent, nogroup=True)
    if not user:
        return
    reply_msg = await event.get_reply_message()
    chat_id = event.chat_id
    user_id = reply_msg.sender_id
    if event.is_private:
        chat_name = user.first_name
        chat_type = "Personal"
    else:
        chat_name = get_display_name(await event.get_chat())
        chat_type = "Group"
    user_name = user.first_name
    user_username = user.username
    if is_added(chat_id, user_id):
        return await edit_or_reply(event, "`The user is already enabled with ai.`")
    try:
        addai(chat_id, user_id, chat_name, user_name, user_username, chat_type)
    except Exception as e:
        await edit_or_reply(catevent, f"**Error:**\n`{e}`")
    else:
        await edit_or_reply(catevent, "Hi")


@bot.on(admin_cmd(pattern=r"rmvai ?(.*)"))
async def remove_chatbot(event):
    "To stop ai for that user"
    if event.reply_to_msg_id is None:
        return await edit_or_reply(
            event, "Reply to a User's message to stop ai on him."
        )
    reply_msg = await event.get_reply_message()
    user_id = reply_msg.sender_id
    chat_id = event.chat_id
    if is_added(chat_id, user_id):
        try:
            remove_ai(chat_id, user_id)
        except Exception as e:
            await edit_or_reply(catevent, f"**Error:**\n`{e}`")
        else:
            await edit_or_reply(event, "Ai has been stopped for the user")
    else:
        await edit_or_reply(event, "The user is not activated with ai")



@bot.on(admin_cmd(pattern=r"delai (-a)?(.*)"))
async def delete_chatbot(event):
    "To delete ai in this chat."
    input_str = event.pattern_match.group(1)
    if input_str:
        lecho = get_all_users()
        if len(lecho) == 0:
            return await edit_or_reply(
                event, "You havent enabled ai atleast for one user in any chat."
            )
        try:
            remove_all_users()
        except Exception as e:
            await edit_or_reply(event, f"**Error:**\n`{str(e)}`", 10)
        else:
            await edit_or_reply(event, "Deleted ai for all enabled users in all chats.")
    else:
        lecho = get_users(event.chat_id)
        if len(lecho) == 0:
            return await edit_or_reply(
                event, "You havent enabled ai atleast for one user in this chat."
            )
        try:
            remove_users(event.chat_id)
        except Exception as e:
            await edit_or_reply(event, f"**Error:**\n`{e}`", 10)
        else:
            await edit_or_reply(event, "Deleted ai for all enabled users in this chat")


@bot.on(admin_cmd(pattern=r"listai ?(.*)"))
async def list_chatbot(event):  # sourcery no-metrics
    "To list all users on who you enabled ai."
    input_str = event.pattern_match.group(1)
    private_chats = ""
    output_str = "**Ai enabled users:**\n\n"
    if input_str:
        lsts = get_all_users()
        group_chats = ""
        if len(lsts) <= 0:
            return await edit_or_reply(event, "There are no ai enabled users")
        for echos in lsts:
            if echos.chat_type == "Personal":
                if echos.user_username:
                    private_chats += (
                        f"☞ [{echos.user_name}](https://t.me/{echos.user_username})\n"
                    )
                else:
                    private_chats += (
                        f"☞ [{echos.user_name}](tg://user?id={echos.user_id})\n"
                    )
            elif echos.user_username:
                group_chats += f"☞ [{echos.user_name}](https://t.me/{echos.user_username}) in chat {echos.chat_name} of chat id `{echos.chat_id}`\n"
            else:
                group_chats += f"☞ [{echos.user_name}](tg://user?id={echos.user_id}) in chat {echos.chat_name} of chat id `{echos.chat_id}`\n"

        if private_chats != "":
            output_str += "**Private Chats**\n" + private_chats + "\n\n"
        if group_chats != "":
            output_str += "**Group Chats**\n" + group_chats
    else:
        lsts = get_users(event.chat_id)
        if len(lsts) <= 0:
            return await edit_or_reply(
                event, "There are no ai enabled users in this chat"
            )
        for echos in lsts:
            if echos.user_username:
                private_chats += (
                    f"☞ [{echos.user_name}](https://t.me/{echos.user_username})\n"
                )
            else:
                private_chats += (
                    f"☞ [{echos.user_name}](tg://user?id={echos.user_id})\n"
                )
        output_str = "**Ai enabled users in this chat are:**\n" + private_chats
    await edit_or_reply(event, output_str)


@bot.on(events.NewMessage(incoming=True, from_users=(1938996006)))
async def ai_reply(event):
    if is_added(event.chat_id, event.sender_id) and (event.message.text):
        AI_LANG = gvarstatus("AI_LANG") or "en"
        master_name = get_display_name(await event.client.get_me())
        try:
            response = await rs_client.get_ai_response(
                message=event.message.text,
                server="primary",
                master="LegendUserbot",
                bot=master_name,
                uid=event.client.uid,
                language=AI_LANG,
            )
            await event.reply(response.message)
        except Exception as e:
            LOGS.error(str(e))
            await event.reply(random.choice(tired_response))


CmdHelp("chatbot").add_command(
   'addai', None, 'add ai bot'
).add_command(
   'rmvai', None, 'remove ai'
).add_command(
   'listai', None, 'list ai'
).add_command(
    'delai', None, 'delte ai'
).add()
