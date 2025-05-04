import asyncio
import importlib

from pyrogram import idle

import config
from NoxxNetwork import LOGGER, app, userbot
from NoxxNetwork.core.call import RAUSHAN
from NoxxNetwork.misc import sudo
from NoxxNetwork.plugins import ALL_MODULES
from NoxxNetwork.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɴᴏᴛ ꜰɪʟʟᴇᴅ, ᴘʟᴇᴀꜱᴇ ꜰɪʟʟ ᴀ ᴘʏʀᴏɢʀᴀᴍ ᴠ2 ꜱᴇꜱꜱɪᴏɴ 🤬"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NoxxNetwork.plugins" + all_module)
    LOGGER("NoxxNetwork.plugins").info("➽ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ ʟᴏᴀᴅᴇᴅ ʙʏ ɴᴀɴᴅ ʏᴀᴅᴜᴡᴀɴsʜɪ")
    await userbot.start()
    await RAUSHAN.start()
    await RAUSHAN.decorators()
    LOGGER("NoxxNetwork").info("➤\n ʀᴇᴘᴏ ᴍᴀᴅᴇ ʙʏ ɴᴀɴᴅ ʏᴀᴅᴜᴡᴀɴsʜɪ")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NoxxNetwork").info("➤\n Must Join @ShrutiBots on Telegram")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
