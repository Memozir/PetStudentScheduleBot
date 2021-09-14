from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN


bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def shutdown(dispatcher: Dispatcher):
	await dispatcher.storage.close()
	await dispatcher.storage.wait_closed()
