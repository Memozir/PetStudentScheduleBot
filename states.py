from aiogram.dispatcher.filters.state import State, StatesGroup


class ProcessStates(StatesGroup):

    SCHEDULE_PROCESS = State()