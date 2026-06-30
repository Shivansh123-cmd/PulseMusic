from pyrogram import filters
from pyrogram.types import Message, CallbackQuery

from Pulse import app, YouTube

from Pulse.utils.inline.play import stream_markup

@app.on_message(filters.command(["autoplay"]) & filters.group)
async def autoplay_cmd(client, message: Message):
    chat_id = message.chat.id
    new_state = not YouTube.is_autoplay_on(chat_id)
    YouTube.set_autoplay(chat_id, new_state)
    if new_state:
        await message.reply_text("<blockquote><emoji id='5397733426654626788'>✨</emoji> <b>𝐀ᴜᴛᴏᴘʟᴀʏ ιs ηᴏᴡ 𝐎𝐍</b></blockquote>")
    else:
        await message.reply_text("<blockquote><emoji id='6152069270269334526'>💔</emoji> <b>𝐀ᴜᴛᴏᴘʟᴀʏ ιs ηᴏᴡ 𝐎𝐅𝐅</b></blockquote>")

@app.on_callback_query(filters.regex(r"^Autoplay_Toggle\|(.+)"))
async def autoplay_cb(client, CallbackQuery):
    chat_id = int(CallbackQuery.matches[0].group(1))
    new_state = not YouTube.is_autoplay_on(chat_id)
    YouTube.set_autoplay(chat_id, new_state)
    
    await CallbackQuery.answer(
        f"Autoplay is now {'ON' if new_state else 'OFF'}", show_alert=True
    )
    
    # Optionally update the player buttons
    try:
        from Pulse.utils.formatters import get_string
        from Pulse.misc import db
        # We need _ but we can just skip updating if it's too complex or just let it be.
        # But for premium experience, let's update it!
        language = "en"
        _ = get_string(language)
        buttons = stream_markup(_, chat_id)
        await CallbackQuery.message.edit_reply_markup(reply_markup=buttons)
    except Exception as e:
        pass

