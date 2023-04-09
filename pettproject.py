import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
logging.basicConfig(level=logging.INFO)
TOKEN = '6036420526:AAGQmeS2I2EQi_m0LCAFIOtQc1O_xY6iLmw'
echobot = Bot(token=TOKEN)
dp = Dispatcher(echobot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply('хеееей')

@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
