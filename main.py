from handlers import dp
from aiogram import executor

async def on_start(_):
    print('Бот запущен')

async def on_shut(_):
    print('Бот выключен')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start, on_shutdown=on_shut)
