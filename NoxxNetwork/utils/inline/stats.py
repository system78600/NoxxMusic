from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def stats_buttons():
    buttons = [
        [
            InlineKeyboardButton(
                text="📊 Bot Stats",
                callback_data="bot_stats"
            )
        ]
    ]
    return InlineKeyboardMarkup(buttons)


def back_stats_buttons():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔙 Back",
                callback_data="stats_back"
            )
        ]
    ]
    return InlineKeyboardMarkup(buttons)
