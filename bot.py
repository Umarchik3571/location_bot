import logging

from aiogram import Bot ,Dispatcher ,executor ,types
from btn import start_menu
from geopy.geocoders import Nominatim

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "5623693354:AAFnm9zV80f9ZiElx4lcnLl48HKSa3vrcIM"

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)



@dp.message_handler(commands=["start"])
async def start_bot(message :types.Message):
    menu_btn = await start_menu()
    await message.answer("SALOM BOTAKAY", reply_markup=menu_btn)


@dp.message_handler(content_types=['contact'])
async def get_contact(message:types.Message):
    await message.answer(message.contact.first_name)
    await message.answer(message.contact.phone_number)

@dp.message_handler(content_types=['location'])
async def get_location(message:types.Message):
    await message.answer(message.location)
    lat=message.location.latitude
    long=message.location.longitude
    geo = Nominatim(user_agent="Gogle")
    location = geo.reverse(f"{lat},{long}")
    await message.answer(location)

    import requests


if __name__ == "__main__":
    executor.start_polling(dp)