from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware


storage = MemoryStorage()

bot = Bot(token='6052705571:AAGCexmk6Y7ix-pzMJdL-tev2QGb2O7uUSo')
ADMINS_CHAT_ID = -1001962943242

dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())
