from userbot.util import admin_cmd
from userbot import CmdHelp


@borg.on(admin_cmd(pattern="cop"))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.text
        event.reply_to_msg_id
        the_real_message = the_real_message.replace("*", "*")
        the_real_message = the_real_message.replace("_", "_")
        await event.edit(the_real_message)
    else:
        await event.edit("Reply to a  message .cop to copy nd paste ")


CmdHelp("copy").add_command(
   'cop', None, 'Use and See'
).add()
