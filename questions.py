import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


question_1 = "1.Що таке ООП?"
answer_1 = ["Об'єктно-орієнтоване програмування", "Одноразове оголошення програми",
            "Остання обробка помилок", "Обмеження доступу до даних"]
correct_1 = "0"


question_2 = "2.Що таке клас в Python?"
answer_2 = ["Функція для створення об'єкту", "Перелік зарезервованих слів",
            "Коротка назва для програми", "Шаблон для створення об'єктів"]
correct_2 = "3"


question_3 = "3.Що таке об'єкт в контексті ООП?"
answer_3 = ["Вихідний код програми", "Функція зі стандартної бібліотеки Python",
            "Екземпляр класу з властивостями і методами", "Збірник математичних формул "]
correct_3 = "2"


question_4 = "4.Що таке спадкування (наслідування) в ООП?"
answer_4 = ["Процес передачі специфічних властивостей від одного класу до іншого", "Поетапне виконання програми",
            "Опис поведінки програми", "Перетворення даних у числа"]
correct_4 = "0"


question_5 = "5.Що таке поліморфізм в ООП?"
answer_5 = ["Можливість класу мати багато екземплярів",
            "Застосування одного і того ж методу для об'єктів різних класів",
            "Отримання доступу до закритих властивостей класу", "Збереження даних на жорсткому диску"]
correct_5 = "1"


question_6 = "6.Що таке інкапсуляція в ООП?"
answer_6 = ["Видалення класу з пам'яті", "Захист даних і методів класу від прямого доступу",
            "Переміщення об'єкта між класами", "Перевірка синтаксичних помилок"]
correct_6 = "1"


question_7 = "7.Що таке атрибут класу в Python?"
answer_7 = ["Файл з розширенням .py", "Змінна, яка належить класу, а не його екземплярам",
            "Код програми виконується почергово", "Словник зі значеннями змінних"]
correct_7 = "1"


question_8 = "8.Як створити екземпляр класу в Python?"
answer_8 = ["Записати клас у файл", "Викликати функцію з назвою класу",
            "Використовувати ключове слово new", "Викликати конструктор класу з допомогою назви класу"]
correct_8 = "3"


question_9 = "9.Яке ключове слово використовується для наслідування в Python?"
answer_9 = ["inherit", "inherit from",
            "extends", "class"]
correct_9 = "2"


question_10 = "10.Як називається метод, який викликається автоматично під час створення нового об'єкту класу?"
answer_10 = ["constructor", "destructor",
             "init", "create"]
correct_10 = "2"


answer_tmp = [answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9, answer_10]
question_tmp = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8,
                question_9, question_10]
correct_tmp = [correct_1, correct_2, correct_3, correct_4, correct_5, correct_6, correct_7, correct_8,
               correct_9, correct_10]


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

