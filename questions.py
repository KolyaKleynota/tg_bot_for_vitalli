import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data import answer_tmp, question_tmp, correct_tmp


def get_random_data():
    for_random = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(for_random)

    answer = []
    question = []
    correct = []
    for i in range(10):
        answer.append(answer_tmp[for_random[i]])
        question.append(question_tmp[for_random[i]])
        correct.append(correct_tmp[for_random[i]])

    inline_keyboard_array = []

    for i in range(10):
        inline_keyboard_tmp = InlineKeyboardMarkup(row_width=2)

        first_button = InlineKeyboardButton(text=answer[i][0],
                                            callback_data="0")

        second_button = InlineKeyboardButton(text=answer[i][1],
                                               callback_data="1")

        third_button = InlineKeyboardButton(text=answer[i][2],
                                                callback_data="2")

        fourth_button = InlineKeyboardButton(text=answer[i][3],
                                            callback_data="3")

        inline_keyboard_tmp.add(first_button, second_button, third_button, fourth_button)
        inline_keyboard_array.append(inline_keyboard_tmp)
    return[question, correct, inline_keyboard_array]


if __name__ == "__main__":
    print(get_random_data())

