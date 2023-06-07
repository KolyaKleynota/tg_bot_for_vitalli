from aiogram import Bot, Dispatcher, executor, types
from questions import get_random_data

from config import TOKEN

import time
import datetime

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

result = []
question = []
correct = []
inline_keyboard_array = []

start_time = ""
end_time = ""


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    global result
    result = []
    global question, correct, inline_keyboard_array
    question, correct, inline_keyboard_array = get_random_data()
    global start_time
    start_time = time.time()

    await message.answer(text="розпочнемо наш тест\n")
    await bot.send_message(chat_id=message.chat.id, text=question[0], reply_markup=inline_keyboard_array[0])


@dp.callback_query_handler()
async def reply_callback(callback: types.CallbackQuery):
    result.append(callback.data)
    if len(result) < 10:
        await ask_question(callback.message, len(result))
    else:
        await check_result(callback.message)


async def ask_question(message: types.Message, it):
    await bot.send_message(chat_id=message.chat.id, text=question[it], reply_markup=inline_keyboard_array[it])


async def check_result(message: types.Message):
    points = 0
    for i in range(10):
        if result[i] == correct[i]:
            points += 1
    global end_time
    end_time = time.time()
    minute = 0
    second = 0
    time_of_test = end_time - start_time
    minute = time_of_test // 60
    second = time_of_test % 60

    current_date = datetime.date.today().strftime("%d.%m.%Y")
    await bot.send_message(message.chat.id, f"Ви набрали {points} балів\nдата тесту {current_date}")
    await bot.send_message(message.chat.id, f"Тест тривав {minute} хвилин і {second:.2f} секунд")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



