from aiogram import Bot, Dispatcher
from config import TELEGRAM_BOT_API

bot = Bot(TELEGRAM_BOT_API)
dp = Dispatcher(bot)