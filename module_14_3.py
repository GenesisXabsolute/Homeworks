from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = '7492498449:AAHZt8SbNHInFKvk2-3nH2e1NdC8zaNTHYI'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать')
button2 = KeyboardButton('Информация')
button3 = KeyboardButton('Купить')
kb.add(button1, button2, button3)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
button2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
kb2.add(button1, button2)

kb3 = InlineKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton('Кубик рубик', callback_data='product_buying')
button2 = InlineKeyboardButton('Маска', callback_data='product_buying')
button3 = InlineKeyboardButton('Плеер', callback_data='product_buying')
button4 = InlineKeyboardButton('Книга', callback_data='product_buying')
kb3.add(button1, button2, button3, button4)


class UserStates(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(msg):
    await msg.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    with open('Cube.png', 'rb') as f:
        await message.answer_photo(f, 'Название: Кубик рубик')
    with open('Mask.png', 'rb') as f:
        await message.answer_photo(f, 'Название: Маска')
    with open('mp3_player.png', 'rb') as f:
        await message.answer_photo(f, 'Название: Плеер')
    with open('Book.png', 'rb') as f:
        await message.answer_photo(f, 'Название: Книга')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb3)


@dp.callback_query_handler(text=['product_buying'])
async def end_confirm_message(call):
    await call.message.answer('Вы успешно приобрели товар')
    await call.answer()


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=kb2)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer('Формулы расчёта:\n'
                              '1. Норма калорий = 10 * вес + 6.25 * рост - 5 * возраст + 5\n'
                              )
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await call.answer()
    await UserStates.age.set()


@dp.message_handler(state=[UserStates.age])
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост')
    await UserStates.growth.set()


@dp.message_handler(state=[UserStates.growth])
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес')
    await UserStates.weight.set()


@dp.message_handler(state=[UserStates.weight])
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(
        f"Ваша норма калорий {(10 * int(data['weight'])) + (6.25 * int(data['growth'])) - (5 * int(data['age'])) + 5}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
