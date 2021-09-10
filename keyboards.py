from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

from handlers.callback_factory import cb

helpers_list_kb = InlineKeyboardMarkup(row_width=1)
schedule_all_btn = InlineKeyboardButton(text='Расписание', callback_data=cb.new(id='schedule'))
helpers_list_kb.add(schedule_all_btn)

schedule_func_kb = InlineKeyboardMarkup(row_width=1)
today_btn = InlineKeyboardButton(text='На сегодня', callback_data=cb.new(id='today'))
tomorrow_btn = InlineKeyboardButton(text='На следующий учебный день', callback_data=cb.new(id='tomorrow'))
schedule_func_kb.add(today_btn, tomorrow_btn)

show_helpers_kb = ReplyKeyboardMarkup(resize_keyboard=True)
show_helpers_btn1 = KeyboardButton('Показать функции')
show_helpers_kb.add(show_helpers_btn1)

group_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
vt_120 = KeyboardButton('120')
vt_220 = KeyboardButton('220')
group_keyboard.add(vt_120, vt_220)

# get_schedule = ReplyKeyboardMarkup(resize_keyboard=True)
# btn_sch = KeyboardButton('Расписание')
# get_schedule.add(btn_sch)