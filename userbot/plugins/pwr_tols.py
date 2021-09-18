from userbot.helpers.runner import reload_MYSTERIOUSBOT 
import os
import sys
import asyncio
from os import execl
from time import sleep

from MYSTERIOUSBOT.utils import admin_cmd, sudo_cmd, eor
from userbot.cmdhelp import CmdHelp
from userbot import HEROKU_APP, bot

@bot.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("яєϐοοτιиg **[ ░░░ ]** ...\nωαιτ ƒєω мιиυτє⚠️")
    await event.edit("яєϐοοτιиg **[ █░░ ]** ...\nωαιτ ƒєω мιиυτє☣️")
    await event.edit("яєϐοοτιиg **[ ██░ ]** ...\nωαιτ ƒєω мιиυτє☢️")
    await event.edit("яєϐοοτιиg **[ ███ ]** ...\nωαιτ ƒєω мιиυτєѕ☢️")
    await event.edit("Rєϐοοτє∂ MYSTERIOUSBOT**[ ✔️ ]** ...\nType `.ping` or `.legend` after 5min to check if I am working✔️")
    await bot.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

@bot.on(admin_cmd(pattern="shutdown$"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**[ ! ]** `⚰️Turning off bot now ... Manually turn me on later or follow step of update in @MYSTERIOUS_EMPIRE` ಠ_ಠ")
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)

@bot.on(admin_cmd(pattern="reload$"))
@bot.on(sudo_cmd(pattern="reload$", allow_sudo=True))
async def rel(event):
    await eor(event, "Reloading MYSTERIOUS... Wait for few seconds...")
    await reload_MYSTERIOUSBOT()


CmdHelp("pwr tools").add_command(
  "restart", None, "Restarts your userbot. Reѕtarting Bot may result in better functioning of bot when its laggy"
).add_command(
  "shutdown", None, "Turns off Dynos of Userbot. Userbot will stop working unless you manually turn it on from heroku"
).add_command(
 "reload", None, "Reload Ur All Plugins "
).add()
