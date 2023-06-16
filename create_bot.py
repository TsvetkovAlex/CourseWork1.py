from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


storage = MemoryStorage()

bot = Bot(token='6132100459:AAE3zGmjHjwwNuT3aLRgyUKRqgsvJbn6QKs')
ADMINS_CHAT_ID = -1001962943242

dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())
