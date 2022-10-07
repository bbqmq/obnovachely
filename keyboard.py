from aiogram import types

apanel = types.InlineKeyboardMarkup(row_width=3)
apanel.add(types.InlineKeyboardButton(text='📢 Рассылка', callback_data='rass'))
apanel.add(types.InlineKeyboardButton(text='📊 Статистика', callback_data='stats'))
apanel.add(types.InlineKeyboardButton(text='💎 Восстановить роль "Владельца"', callback_data='owner'))
apanel.add(types.InlineKeyboardButton(text='👑 Скачать базу данных', callback_data='getdb'))

click_menu = types.InlineKeyboardMarkup(row_width=3)
click_menu.add(types.InlineKeyboardButton(text='👇 Кликер', callback_data='click_menu'))

help_menu = types.InlineKeyboardMarkup(row_width=3)
help_menu.add(types.InlineKeyboardButton(text='💡 Основные', callback_data='main'), types.InlineKeyboardButton(text='🎲 Игры', callback_data='games'))
help_menu.add(types.InlineKeyboardButton(text='💥 Развлекательное', callback_data='entertainment'), types.InlineKeyboardButton(text='🏠 Имущество', callback_data='property'))

help_cmd = types.InlineKeyboardMarkup(row_width=3)
help_cmd.add(types.InlineKeyboardButton(text='🕹 Добавить бота', url="https://telegram.me/bgbgame_bot?startgroup=new")) 
help_cmd.add(types.InlineKeyboardButton(text='🆘 Помощь', callback_data='help'))

channel = types.InlineKeyboardMarkup(row_width=3)
channel.add(types.InlineKeyboardButton(text='📢 Подписаться', url="https://t.me/bgbinfo")) 
channel.add(types.InlineKeyboardButton(text='✅ Проверить', callback_data='check'))

button_marry = types.InlineKeyboardMarkup(row_width=3)
button_marry.add(types.InlineKeyboardButton(text='❤️ Согласиться', callback_data='button_marry_y'), types.InlineKeyboardButton(text='💔 Отказаться', callback_data='button_marry_n'))
button_divorce = types.InlineKeyboardMarkup(row_width=3)
button_divorce.add(types.InlineKeyboardButton(text='💔 Согласиться', callback_data='button_divorce_y'), types.InlineKeyboardButton(text='❤ Отказаться', callback_data='button_divorce_n'))

gender = types.InlineKeyboardMarkup(row_width=3)
gender.add(types.InlineKeyboardButton(text='👩 Женский', callback_data='women'), types.InlineKeyboardButton(text='👨 Мужской', callback_data='men'))

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(types.KeyboardButton('Отмена'))

click_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
click_back.add(types.KeyboardButton('👇 Клик'))
click_back.add(types.KeyboardButton('Отмена'))