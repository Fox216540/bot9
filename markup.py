from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

markup = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = [
        KeyboardButton(text="Поддержка"),
        KeyboardButton(text="Предложка"),
        ]
markup.add(*buttons)

