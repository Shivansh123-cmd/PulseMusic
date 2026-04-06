from pyrogram.types import InlineKeyboardButton

import config
from Zayan import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="🎧", url="https://t.me/ll_Bot_Promotion_ll"),
            InlineKeyboardButton(text="🫦", url="https://t.me/ll_Bot_Promotion_ll"),
        ],
        [
            InlineKeyboardButton("𝑭𝑹𝑬𝑬 𝑷𝑹𝑶𝑴𝑶𝑻𝑰𝑶𝑵 📢", url="https://t.me/ll_Bot_Promotion_ll")            
        ],
        [
            InlineKeyboardButton("• ʙᴏᴛ ɪɴғᴏ •", callback_data="bot_info_data"),
        ],
    ]
    return buttons
