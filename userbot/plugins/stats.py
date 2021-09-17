#ℓєgєи∂
import time

from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

from userbot import CMD_HELP
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern="stats$"))
@bot.on(sudo_cmd(pattern="stats$", allow_sudo=True))
async def stats(
    event: NewMessage.Event,
) -> None:  # pylint: disable = R0912, R0914, R0915
    """Command to get stats about the account"""
    LEGEND = await edit_or_reply(event, "`Collecting stats...`")
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            # participants_count = (await event.get_participants(dialog,
            # limit=0)).total
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1
            elif entity.megagroup:
                groups += 1
                # if participants_count > largest_group_member_count:
                #     largest_group_member_count = participants_count
                if entity.creator or entity.admin_rights:
                    # if participants_count > largest_group_with_admin:
                    #     largest_group_with_admin = participants_count
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1
        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"❣️**𝚂𝚝𝚊𝚝𝚜 𝙵𝚘𝚛  {full_name}**❣️\n\n"
    response += f"🌷private stats  : {private_chats} \n"
    response += f" ♦️               `υѕєяѕ: {private_chats - bots}` \n"
    response += f"♦️                  `ϐοτѕ: {bots}` \n"
    response += f"♦️              gяουρѕ: {groups} \n"
    response += f"♦️           ϲнαииєℓѕ: {broadcast_channels} \n"
    response += f"♥️α∂мιи ιи gяουρѕ: {admin_in_groups} \n"
    response += f"🔺             `ϲяєατοя: {creator_in_groups}` \n"
    response += f"♥️     `α∂мιи яιgнτѕ: {admin_in_groups - creator_in_groups}` \n"
    response += f"♥️α∂мιи ιи ϲнαииєℓѕ: {admin_in_broadcast_channels} \n"
    response += f"🔺                 `ϲяєατοя: {creator_in_channels}` \n"
    response += (
        f"♥️         `α∂мιи яιgнτѕ: {admin_in_broadcast_channels - creator_in_channels}` \n"
    )
    response += f"🎒                 υияєα∂: {unread} \n"
    response += f"🎒 υияєα∂ мємτιοиѕ: {unread_mentions} \n\n"
    response += f"🎒       __ιτ τοοκ:__ {stop_time:.02f}s \n"
    response += (
        f"ƒɾσɱ ƭɦε ∂αƭαɓαรε σƒ:-[♥️✞︎t͛ẞ̸ 𝖑𝖊ɠêɳ̃dẞø✞︎♥️](https://t.me/Legend_Userbot)"
    )
    await LEGEND.edit(response)


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


CmdHelp("stats").add_command(
  'stats', None, 'Shows you the count of your groups, channels, private chats, etc.'
).add()

