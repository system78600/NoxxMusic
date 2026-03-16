import asyncio

from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from NoxxNetwork import app
from NoxxNetwork.misc import SUDOERS
from NoxxNetwork.utils.database import (
    get_assistant,
    get_lang,
    is_active_chat,
    is_maintenance,
)

from config import SUPPORT_CHAT
from strings import get_string

links = {}


def UserbotWrapper(command):
    async def wrapper(client, message):
        language = await get_lang(message.chat.id)
        _ = get_string(language)

        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} is under maintenance, visit [support chat]({SUPPORT_CHAT}) for knowing the reason.",
                    disable_web_page_preview=True,
                )

        try:
            await message.delete()
        except:
            pass

        chat_id = message.chat.id

        if not await is_active_chat(chat_id):
            userbot = await get_assistant(chat_id)

            try:
                member = await app.get_chat_member(chat_id, userbot.id)

                if member.status in [
                    ChatMemberStatus.BANNED,
                    ChatMemberStatus.RESTRICTED,
                ]:
                    return await message.reply_text(
                        "Assistant is banned in this group.",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text="Unban Assistant",
                                        callback_data="unban_assistant",
                                    )
                                ]
                            ]
                        ),
                    )

            except UserNotParticipant:

                try:
                    link = await app.create_chat_invite_link(chat_id)
                    invitelink = link.invite_link
                except ChatAdminRequired:
                    return await message.reply_text(
                        "Please make me admin with invite users permission."
                    )

                msg = await message.reply_text("Assistant joining this chat...")

                try:
                    await userbot.join_chat(invitelink)

                except InviteRequestSent:

                    try:
                        await app.approve_chat_join_request(chat_id, userbot.id)
                    except Exception as e:
                        return await message.reply_text(f"Error: {e}")

                except UserAlreadyParticipant:
                    pass

                except Exception as e:
                    return await message.reply_text(f"Assistant join error:\n{e}")

                await asyncio.sleep(2)

                await msg.delete()

                await message.reply_text(
                    f"{app.mention} Assistant Successfully Joined ✅\n\nAssistant: @{userbot.username}"
                )

                links[chat_id] = invitelink

                try:
                    await userbot.resolve_peer(chat_id)
                except:
                    pass

        return await command(client, message, _, chat_id)

    return wrapper
