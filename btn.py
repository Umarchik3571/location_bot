from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def start_menu():
    btn = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn.add(
        KeyboardButton("location",request_location=True),
        KeyboardButton("phone number:",request_contact=True)
    )
    return btn