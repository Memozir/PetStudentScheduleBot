from dispatcher import dp, Bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import IDFilter

import config
from keyboards import show_helpers_kb, helpers_list_kb
from get_date import get_week_num, get_week_day
from text.schedule import schedule
from states import ProcessStates


@dp.message_handler(IDFilter(user_id=config.ADMIN_IDS), commands=['load'], state='*')
async def load_new_schedule(message: types.Message):
    await message.answer('Здравствуйте, админ!')


@dp.message_handler(commands='start', state='*')
async def bot_start(message: types.Message):
    await message.answer("Вас приветствует бот для помощи студентам", reply_markup=show_helpers_kb)
    await ProcessStates.SHOW_FUNC.set()


@dp.message_handler(state=ProcessStates.TODAY)
async def schedule_process(message: types.Message, state: FSMContext):

    await ProcessStates.SHOW_FUNC.set()

    week_number = get_week_num()
    week_day = get_week_day()

    if message.text.lower() == '120':

        if (week_number % 2) == 1:
            if week_day < 6:
                await message.answer(schedule['120'][f'{week_day}']['bottom'], reply_markup=show_helpers_kb)
            else:
                await message.answer('Сегодня выходной', reply_markup=show_helpers_kb)
        else:
            if week_day < 6:
                await message.answer(schedule['120'][f'{week_day}']['top'], reply_markup=show_helpers_kb)
            else:
                await message.answer('Сегодня выходной', reply_markup=helpers_list_kb)
    

    elif message.text.lower() == '220':

        if (week_number % 2) == 1:
            if week_day < 6:
                await message.answer(schedule['220'][f'{week_day}']['bottom'], reply_markup=show_helpers_kb)
            else:
                await message.answer('Сегодня выходной', reply_markup=show_helpers_kb)
        else:
            if week_day < 6:
                await message.answer(schedule['220'][f'{week_day}']['top'], reply_markup=show_helpers_kb)
            else:
                await message.answer('Сегодня выходной', reply_markup=show_helpers_kb)
    
    await ProcessStates.SHOW_FUNC.set()


@dp.message_handler(state=ProcessStates.TOMORROW)
async def select_helper(message: types.Message):

    if message.text == '120':

        day = get_week_day()
        week_number = get_week_num()
        
        if day < 5:
            day += 1

            if (week_number % 2) == 0:
                await message.answer(schedule['120'][f'{day}']['top'], reply_markup=show_helpers_kb)
                
            else:
                await message.answer(schedule['120'][f'{day}']['bottom'], reply_markup=show_helpers_kb)
        
        else:
            if (week_number % 2) == 0:
                await message.answer(schedule['120']['1']['bottom'], reply_markup=show_helpers_kb)

            else:
                await message.answer(schedule['120']['1']['top'], reply_markup=show_helpers_kb)

    
    if message.text == '220':

        day = get_week_day()
        week_number = get_week_num()
    
        if day < 5:
            day += 1

            if (week_number % 2) == 0:
                await message.answer(schedule['220'][f'{day}']['top'], reply_markup=show_helpers_kb)

            else:
                await message.answer(schedule['220'][f'{day}']['bottom'], reply_markup=show_helpers_kb)
        
        else:
            if (week_number % 2) == 0:
                await message.answer(schedule['220']['1']['bottom'], reply_markup=show_helpers_kb)
            else:
                await message.answer(schedule['220']['1']['top'], reply_markup=show_helpers_kb)
    
    await ProcessStates.SHOW_FUNC.set()


@dp.message_handler(state=ProcessStates.ARB_GP)
async def arbitary_day(message: types.Message, state: FSMContext):

    # current_state = await state.get_state()

    await ProcessStates.SHOW_FUNC.set()

    week_number = get_week_num()
    data_day = await state.get_data()

    if message.text == '120':

        if (week_number % 2) == 0:
            await message.answer(schedule['120'][data_day['arbitary_day']]['top'], reply_markup=show_helpers_kb)

        else:
            await message.answer(schedule['120'][data_day['arbitary_day']]['bottom'], reply_markup=show_helpers_kb)

    elif message.text == '220':

        if (week_number % 2) == 0:
            await message.answer(schedule['220'][data_day['arbitary_day']]['top'], reply_markup=show_helpers_kb)

        else:
            await message.answer(schedule['220'][data_day['arbitary_day']]['bottom'], reply_markup=show_helpers_kb)

    await state.reset_data()
    await ProcessStates.SHOW_FUNC.set()


@dp.message_handler(state=ProcessStates.SHOW_FUNC)
async def show_helpers(message: types.Message, state: FSMContext):
    if message.text.lower() == 'показать функции':
        await message.answer('Список доступных функций:', reply_markup=helpers_list_kb)
        await ProcessStates.SHOW_FUNC.set()
