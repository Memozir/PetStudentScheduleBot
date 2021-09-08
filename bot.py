from aiogram import executor
from dispatcher import dp, shutdow
import logging
import handlers


logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdow)