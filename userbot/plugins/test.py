


import asyncio

from MYSTERIOUSBOT.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="test ?(.*)"))
@bot.on(sudo_cmd(pattern="test ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Testing MYSTERIOUSBOT`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing MYSTERIOUSBOT.`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing MYSTERIOUSBOT..`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing MYSTERIOUSBOT...`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing MYSTERIOUSBOT....`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing MYSTERIOUSBOT.....`")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Testing Successful__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "`Generating Output`\nPlease wait")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Output Generated Successfully__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "**SAVING OUTPUT TO MYSTERIOUSBOT LOCAL DATABASE**")
        await asyncio.sleep(3.5)
        await edit_or_reply(event, 
            "Your [MYSTERIOUSBOT](https:/t.me/MYSTERIOUS_EMPIRE) is working Fine...\n       Join @MYSTERIOUS_EMPIRE For Any Help......"
        )

CmdHelp("test").add_command(
  "test", None, "Test wether your bot is running or not."
).add()
