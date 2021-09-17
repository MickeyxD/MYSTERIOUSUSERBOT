from userbot import CmdHelp, bot
from userbot.utils import admin_cmd, sudo_cmd
import asyncio
from . import *
from userbot.cmdhelp import CmdHelp
CmdHelp("detail").add_command(
   'detailed', None, 'help to get detail of plugin'
).add()
@bot.on(sudo_cmd(pattern="detailed ?(.*)", allow_sudo=True))
@bot.on(admin_cmd(pattern="detailed ?(.*)"))
async def _(event):
    help_plugs = event.pattern_match.group(1).lower()
    if help_plugs:
        if help_plugs in CmdHelp:
            await event.edit(f"Details For 🗡 {CmdHelp[help_plugs]}")
        else:
            await event.edit(
                f"Nothign Is Named as {help_plugs} `.help` to see valid plugs"
            )
    else:
        help_string = ""
        for i in CmdHelp.values():
            help_string += f"`{str(i[0])}`, "
        help_string = help_string[:-2]
        await event.edit(
            "`Are You Commedy Me?`!\n\n" f"{help_string}"
        )
        await asyncio.sleep(2)
        await event.edit("`Specify A Plugin`")
