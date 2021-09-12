from dispatcher import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext

import keyboards
from handlers.callback_factory import cb
from states import ProcessStates
from get_date import get_week_day, get_week_num
from text.schedule import schedule


@dp.callback_query_handler(cb.filter(), state='*')
async def select_helper(query: types.CallbackQuery, callback_data: dict, state=FSMContext):

    # Callback handler
    await bot.answer_callback_query(query.id)
    id = callback_data['id']

    if id == 'schedule':
        await bot.send_message(query['message']['chat']['id'], 'Функции расписания', reply_markup=keyboards.schedule_func_kb)

    elif id == 'tomorrow':
        await ProcessStates.TOMORROW.set()
        await bot.send_message(query['message']['chat']['id'], 'Выберите группу', reply_markup=keyboards.group_keyboard)

    elif id == 'today':
        await ProcessStates.TODAY.set()
        await bot.send_message(query['message']['chat']['id'], 'Выберите свою группу', reply_markup=keyboards.group_keyboard)
    
    elif id == 'arbitary':
        await bot.send_message(query['message']['chat']['id'], 'Выберите день недели:', reply_markup=keyboards.arb_kb)
        await ProcessStates.ARB_GP.set()

    elif id == '1':
        await state.update_data(arbitary_day = '1')
        await bot.send_message(query['message']['chat']['id'], 'Выберите свою группу', reply_markup=keyboards.group_keyboard)
        await ProcessStates.ARB_GP.set()

    elif id == '2':
        await state.update_data(arbitary_day = '2')
        await bot.send_message(query['message']['chat']['id'], 'Выберите свою группу', reply_markup=keyboards.group_keyboard)
        await ProcessStates.ARB_GP.set()

    elif id == '3':
        await state.update_data(arbitary_day = '3')
        await bot.send_message(query['message']['chat']['id'], 'Выберите свою группу', reply_markup=keyboards.group_keyboard)
        await ProcessStates.ARB_GP.set()

    elif id == '4':
        await state.update_data(arbitary_day = '4')
        await bot.send_message(query['message']['chat']['id'], 'Выберите свою группу', reply_markup=keyboards.group_keyboard)
        await ProcessStates.ARB_GP.set()

    elif id == '5':
        await state.update_data(arbitary_day = '5')
        await bot.send_message(query['message']['chat']['id'], 'Выберите свою группу', reply_markup=keyboards.group_keyboard)
        await ProcessStates.ARB_GP.set()

