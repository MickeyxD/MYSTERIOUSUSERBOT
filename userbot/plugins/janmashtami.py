# made by @MY5T3R10U5_X


from . import *

@bot.on(admin_cmd(pattern="krisnanime(.*)"))
async def xd(event):
    await event.edit("wishing to all.....")
    themessage = event.pattern_match.group(1)
    async for tele in borg.iter_dialogs():
        lol = 0
        done = 0
        if tele.is_group:
            chat = tele.id
            try:
                await bot.send_message(chat, f"╭╮╱╭╮\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n┃┃╱┃┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭━━╯\n┃┃\n╰╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭━━╯\n┃┃\n╰╯\b╭╮╱╱╭╮\n┃╰╮╭╯┃\n╰╮╰╯╭╯\n╱╰╮╭╯\n╱╱┃┃\n╱╱╰╯\n╱╱╭╮\n╱╱┃┃\n╱╱┃┃\n╭╮┃┃\n┃╰╯┃\n╰━━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━╮╱╭╮\n┃┃╰╮┃┃\n┃╭╮╰╯┃\n┃┃╰╮┃┃\n┃┃╱┃┃┃\n╰╯╱╰━╯\n╭━╮╭━╮\n┃┃╰╯┃┃\n┃╭╮╭╮┃\n┃┃┃┃┃┃\n┃┃┃┃┃┃\n╰╯╰╯╰╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃╰━━╮\n╰━━╮┃\n┃╰━╯┃\n╰━━━╯\n╭╮╱╭╮\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n┃┃╱┃┃\n╰╯╱╰╯\n╭━━━━╮\n┃╭╮╭╮┃\n╰╯┃┃╰╯\n╱╱┃┃\n╱╱┃┃\n╱╱╰╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━╮╭━╮\n┃┃╰╯┃┃\n┃╭╮╭╮┃\n┃┃┃┃┃┃\n┃┃┃┃┃┃\n╰╯╰╯╰╯\n╭━━╮\n╰┫┣╯\n╱┃┃\n╱┃┃\n╭┫┣╮\n╰━━╯\n\n[Happy Janmashtami To All Of U](https://t.me/MYSTERIOUS_EMPIRE)")
                done += 1
            except:
                lol += 1
                pass
    await event.reply(f"happy Janmashtami from LegendBot support\nthanks for using this Plugin.")


CmdHelp("janmashtami").add_command(
    "krisnanime", None, "Wish u happy JANMASHTAMI day"
).add()
