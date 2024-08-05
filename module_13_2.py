from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = '7492498449:AAHZt8SbNHInFKvk2-3nH2e1NdC8zaNTHYI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(msg):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')












if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
