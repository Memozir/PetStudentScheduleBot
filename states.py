from aiogram.dispatcher.filters.state import State, StatesGroup


class ProcessStates(StatesGroup):
    
    TODAY = State()
    TOMORROW = State()
    ARB_GP = State()
    SHOW_FUNC = State()