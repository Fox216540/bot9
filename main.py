from aiogram import types, Bot, executor
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ContentType

import classes

import markup

admin1 = #user id первого админа
admin2 = #user id второго админа

bot = Bot(token="")#Token
# Диспетчер
dp = Dispatcher(bot,storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Добро', reply_markup=markup.markup)

@dp.message_handler()
async def number(message: types.Message):
    if message.text == 'Поддержка':
        await message.answer('Контакты: @Frein_package')
    elif message.text == 'Предложка':
        await message.answer('Опишите проблему')
        await classes.Message.text.set()

@dp.message_handler(state=classes.Message.text)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    text = await state.get_data()
    await state.finish()
    try:
        text ='@'+ message.from_user.username+"\n" +text['text']
    except:
        text = '@'+message.from_user.first_name + "\n" + text['text']
    await message.answer('Сообщение отправлено')
    await bot.send_message(admin1, text)
    await bot.send_message(admin2, text)

@dp.message_handler(content_types=ContentType.PHOTO, state=classes.Message.text)
async def handle_photo(message: types.Message, state: FSMContext):
    # Получаем наибольшее по размеру фото (фото передаются в нескольких размерах)
    photo = message.photo[-1]
    await state.update_data(text=message.caption)
    text = await state.get_data()
    await state.finish()
    await message.answer('Сообщение отправлено')
    try:
        text = '@'+ message.from_user.username+"\n" +text['text']
    except:
        text = '@'+ message.from_user.first_name +"\n" + text['text']
    await bot.send_photo(admin1, photo=photo.file_id ,caption=text)
    await bot.send_photo(admin2, photo=photo.file_id, caption=text)



executor.start_polling(dp,skip_updates=True)