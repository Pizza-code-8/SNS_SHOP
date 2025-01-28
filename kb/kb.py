from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

#Главная клаиватура
def main_menu_kb():
    kb = [
        [
            KeyboardButton(text="🏠"),
            KeyboardButton(text="🛍"),
            KeyboardButton(text="🛒"),
            KeyboardButton(text="🗂")
        ]
    ]

    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard