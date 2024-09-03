from pyrogram import Client, filters

from bot import logger
from bot.core import filters as fltr, database as db
from pyrogram.enums import MessageEntityType
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .eyecon import eyecon_search
import phonenumbers 
from phonenumbers import geocoder
import phonenumbers.carrier
import phonenumbers.timezone
import urllib.parse
from bot.core.utils import generate_keyboard

new_line = "\n"

def get_text_number(message):
  number = None
  if message.entities:
    for entity in message.entities:
      if entity.type == MessageEntityType.PHONE_NUMBER:
        number = message.text[entity.offset:entity.offset +
                              entity.length].replace(" ", "")
        break
  return number
  
async def ph_match(_, __, m):
  number = get_text_number(m)
  if number:
    return True
  return False
phone_filter = filters.create(ph_match)

@Client.on_message(phone_filter)
async def truth(client, message):
  try:
    parsed_number = phonenumbers.parse(get_text_number(message))
    phone_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
    response = eyecon_search(phone_number.replace("+", ""))

    name, is_spam = None, None
    
    if response.status_code == 200:
        data = response.json()
        if not len(data) == 0:
           name = data[0].get("name", "N/A")
           is_spam = data[0].get("suspicious_spam", False)

    geo = phonenumbers.geocoder.description_for_number(parsed_number,  
           'en')
    carrier = phonenumbers.carrier.name_for_number(parsed_number, 
          'en')
    timezone = phonenumbers.timezone.time_zones_for_number(parsed_number)

    text = f'''
**🔍 Search result for** `{phone_number}` {new_line + new_line + '⚠️ __Spammer alert!!!__' if is_spam else ''}

**Name:** `{name if name else 'n/a'}`{new_line + '**is-spam:** `' + str(is_spam) + '`' if is_spam else ''}
{new_line + '**Country:** `' + geo + '`' if geo else ''}{new_line+ '**Time Zone:** `' + ', '.join(timezone) + '`' if timezone else ''}{new_line+ '**Carrier:** `' + carrier + '`' if carrier else ''}

[Whatsapp](https://wa.me/{phone_number}) | [Telegram](https://t.me/{phone_number})
         '''
    await message.reply(text,quote= True, disable_web_page_preview =True, reply_markup = generate_keyboard(f"[Locate](url::{'https://www.google.com/maps/place/'+ urllib.parse.quote(geo)})"))
    await db.inc_stat("search", 1)
  except Exception as e:
    logger.exception(e)
    await message.reply(
      "Something went wrong, Contact support @ostrichdiscussion",
      reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("Support Group",
                             url="https://t.me/ostrichdiscussion")
      ]]))
