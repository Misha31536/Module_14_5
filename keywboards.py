from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

err_age = 'Введите число от 0 до 100!'
err_number = 'Введите число!'


# Стартовая клавиатура
key_start = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='start')
button2 = KeyboardButton(text='info')
key_start.add(button1, button2)

# Клавиатура выбора принадлежности к полу
key_gender = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text='Мужской', callback_data='5')
button4 = InlineKeyboardButton(text='Женский', callback_data="-161")
key_gender.add(button3)
key_gender.add(button4)

# Клавиатура расчета калорий
key_setting = InlineKeyboardMarkup(resize_keyboard=True)
button5 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button6 = InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
key_setting.add(button5)
key_setting.add(button6)

# Клавиатура выбора степени активности
key_activ = InlineKeyboardMarkup(resize_keyboard=True)
button7 = InlineKeyboardButton(text='1 - минимальная активность;', callback_data='1.2')
button8 = InlineKeyboardButton(text='2 – слабый уровень активности;', callback_data='1.375')
button9 = InlineKeyboardButton(text='3 – умеренный уровень активности;', callback_data='1.55')
button10 = InlineKeyboardButton(text='4 – тяжелая или трудоемкая активность;', callback_data='1.7')
button11 = InlineKeyboardButton(text='5 – экстремальный уровень.', callback_data='1.9')
key_activ.add(button7)
key_activ.add(button8)
key_activ.add(button9)
key_activ.add(button10)
key_activ.add(button11)

# Клавиатура выбора режимов
key_menu = ReplyKeyboardMarkup(resize_keyboard=True)
button12 = KeyboardButton(text='Калории')
button13 = KeyboardButton(text='Купить')
key_menu.add(button12, button13)

# Стартовая клавиатура
key_register = ReplyKeyboardMarkup(resize_keyboard=True)
reg1 = KeyboardButton(text='Регистрация')
key_register.add(reg1)
