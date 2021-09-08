from dispatcher import dp, Bot
from aiogram import types
from aiogram.dispatcher import FSMContext

from get_date import get_date


@dp.message_handler(commands='start', state='*')
async def bot_start(message: types.Message):
    await message.answer("Вас привыетствует бот для помощи студентам")


@dp.message_handler(commands='get_date', state='*')
async def send_current_date(message: types.Message):
    date = get_date()

    await message.answer(date)

