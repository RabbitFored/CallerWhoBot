from pyrogram import Client, filters
from datetime import datetime, timedelta

from bot import CONFIG, strings
from bot.core import filters as fltr
from bot.core.utils import generate_keyboard
from bot.core import database as db

@Client.on_message(fltr.cmd(["settings"]))
async def user_settings(client, message):
    user = await db.get_user(message.from_user.id)
    use_credits = user.settings.get("use_credits", False)
    text = "**Your settings:**"
    btn = f"[Use Credits](data::wht_credits) [{'yes ✔️' if use_credits else 'no ❌'}](data::{'credits_off' if use_credits else 'credits_on'})"
    
    await message.reply(text, reply_markup=generate_keyboard(btn))


@Client.on_callback_query(fltr.on_marker("credits"))
async def toggle_credits(client, query):
   d = query.data.split("_")[-1]
   if d == "on":
       await db.update_user(query.from_user.id, userdata={"settings.use_credits": True})
       await query.answer("Credits enabled")
   else:
       await db.update_user(query.from_user.id , userdata={"settings.use_credits": False})
       await query.answer("Credits disable")