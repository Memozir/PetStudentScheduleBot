from dispatcher import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards import group_keyboard
from handlers.callback_factory import cb
from states import ProcessStates


@dp.callback_query_handler(cb.filter(), state="*")
async def select_helper(query: types.CallbackQuery, callback_data: dict, state: FSMContext):

    await bot.answer_callback_query(query.id)

    id = callback_data['id']

    if id == 'schedule':
        await bot.send_message(query['message']['chat']['id'], 'Выберите свою группу', reply_markup=group_keyboard)
        await ProcessStates.SCHEDULE_PROCESS.set()