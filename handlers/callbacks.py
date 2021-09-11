from dispatcher import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext

import keyboards
from handlers.callback_factory import cb
from states import ProcessStates
from get_date import get_week_day, get_week_num
from text.schedule import schedule


@dp.callback_query_handler(cb.filter(), state='*')
async def select_helper(query: types.CallbackQuery, callback_data: dict):

    # Callback handler
    await bot.answer_callback_query(query.id)
    id = callback_data['id']

    if id == 'schedule':
        await bot.send_message(query['message']['chat']['id'], 'Функции расписания', reply_markup=keyboards.schedule_func_kb)
        await ProcessStates.TODAY.set()

    elif id == 'tomorrow':
        await ProcessStates.TOMORROW.set()
        await bot.send_message(query['message']['chat']['id'], 'Выберите группу', reply_markup=keyboards.group_keyboard)

    elif id == 'today':
        await ProcessStates.TODAY.set()
        await bot.send_message(query['message']['chat']['id'], 'Выберите свою группу', reply_markup=keyboards.group_keyboard)
