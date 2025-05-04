from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from NoxxNetwork import app
from config import BOT_USERNAME
from NoxxNetwork.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sʜʀᴜᴛɪ ʙᴏᴛs ✰
 
✰ ʙᴀᴋɪɪ ᴛᴜᴍ ᴏᴡɴᴇʀ sᴇ ᴘᴜᴄʜʜ sᴀᴋᴛᴇ ʜᴏ

✰ || @TMZEROO ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇᴇʜ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/ShrutiBots"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/NoxxOP/NoxxMusic"),
          ],
               [
                InlineKeyboardButton("ᴏᴜʀ ᴀʟʟ ʙᴏᴛs", url=f"https://t.me/NoxxNetwork/15"),
],
[
InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ʙᴏᴛ", url=f"https://t.me/NyCreation_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/2oj1vp.webp",
        caption=start_txt,
        reply_markup=reply_markup
    )
