import game
from loader import dp
from aiogram.types import Message

# ввод количества конфет для начала игры
@dp.message_handler(commands=['set'])
async def mes_start(message: Message):
    count = int(message.text.split()[1])
    my_game = [message.from_user.id, message.from_user.first_name, count]
    game.total.append(my_game)
    await message.answer(f'В начале игры установлено значение в {count} конфет. \n'
                         'Введи число от 1 до 28.')
