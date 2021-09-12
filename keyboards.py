from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

from handlers.callback_factory import cb

# Main Functions
helpers_list_kb = InlineKeyboardMarkup(row_width=1)
schedule_all_btn = InlineKeyboardButton(text='Расписание', callback_data=cb.new(id='schedule'))
helpers_list_kb.add(schedule_all_btn)

# Sub Functions
schedule_func_kb = InlineKeyboardMarkup(row_width=1)
today_btn = InlineKeyboardButton(text='На сегодня', callback_data=cb.new(id='today'))
tomorrow_btn = InlineKeyboardButton(text='На следующий учебный день', callback_data=cb.new(id='tomorrow'))
arbitary_day_btn = InlineKeyboardButton(text='Произвольный день', callback_data=cb.new(id='arbitary'))
schedule_func_kb.add(today_btn, tomorrow_btn, arbitary_day_btn)

# Arbitary keyboard
arb_kb = InlineKeyboardMarkup(row_width=1)
monday_btn = InlineKeyboardButton(text='Понедельник', callback_data=cb.new(id='1'))
tuesday_btn = InlineKeyboardButton(text='Вторник', callback_data=cb.new(id='2'))
wendnesday_btn = InlineKeyboardButton(text='Среда', callback_data=cb.new(id='3'))
thorsday_btn = InlineKeyboardButton(text='Четверг', callback_data=cb.new(id='4'))
friday_btn = InlineKeyboardButton(text='Пятница', callback_data=cb.new(id='5'))
arb_kb.add(monday_btn, tuesday_btn, wendnesday_btn, thorsday_btn, friday_btn)

# Show Main Functions
show_helpers_kb = ReplyKeyboardMarkup(resize_keyboard=True)
show_helpers_btn1 = KeyboardButton('Показать функции')
show_helpers_kb.add(show_helpers_btn1)

# Choose study group
group_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
vt_120 = KeyboardButton('120')
vt_220 = KeyboardButton('220')
group_keyboard.add(vt_120, vt_220)

