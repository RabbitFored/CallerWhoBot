from pyrogram import Client, filters
from datetime import datetime, timedelta

from bot import CONFIG, strings
from bot.core import filters as fltr
from bot.core.utils import get_target_user
from bot.core import database as db

@Client.on_message(fltr.cmd(["test"]))
async def test(client, message):
    user = await client.get_stars_transactions()
    await message.reply("Limits: " + str(user))