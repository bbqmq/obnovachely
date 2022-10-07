 # -*- coding: utf-8 -*-
import logging
import sqlite3
import requests
import json
import random, time, asyncio
import zipfile
from config import admin, logchat, globallog, TOKEN
from aiogram import Bot, Dispatcher, executor, types
from datetime import datetime, timedelta
from aiogram.utils.markdown import quote_html
from time import gmtime, strptime, strftime
from decimal import Decimal
from filters import IsAdminFilter
import keyboard as kb
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import Throttled
from aiogram import types
import emoji as emo
import os

# logging
logging.basicConfig(level=logging.INFO)

# storage
storage = MemoryStorage()

# btc
url = "https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC"

# class info
class info(StatesGroup):
  name = State()
  rasst = State()
  click = State()

# bot init
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

# admin filters
dp.filters_factory.bind(IsAdminFilter)

# datebase
connect = sqlite3.connect("users.db")
cursor = connect.cursor()
connect2 = sqlite3.connect("sticker.db")
cursor2 = connect2.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    balance INT,
    bank BIGINT,
    rating BIGINT,
    bitcoin BIGINT,
    expe BIGINT,
    last_stavka INT,
    last_bonus INT,
    car1 INT,
    car2 INT,
    car3 INT,
    car4 INT,
    car5 INT,
    car6 INT,
    car7 INT,
    car8 INT,
    car9 INT,
    car10 INT,
    car11 INT,
    user_name STRING,
    case1 INT,
    case2 INT,
    case3 INT,
    user_status STRING,
    cart INT,
    stavka INT,
    game INT,
    last_grab INT,
    pet1 INT,
    pet2 INT,
    pet3 INT,
    pet4 INT,
    pet5 INT,
    pet6 INT,
    pet7 INT,
    pet8 INT,
    pet9 INT,
    pet_name STRING,
    pet_hp INT,
    pet_eat INT,
    pet_mood INT,
    games INT,
    registr_time INT,
    last_work INT,
    checking INT,
    checking1 INT,
    checking2 INT,
    checking3 INT,
    pet10 INT,
    status STRING,
    car12 INT,
    case4 INT,
    snow INT,
    last_snow INT,
    promo1 INT,
    promo2 INT,
    promo3 INT,
    promo4 INT,
    promo5 INT,
    promo6 INT,
    promo7 INT,
    promo8 INT,
    promo9 INT,
    promo10 INT,
    promo11 INT,
    promo12 INT,
    promo13 INT,
    promo14 INT,
    promo15 INT,
    promo16 INT,
    promo17 INT,
    promo18 INT,
    promo19 INT,
    promo20 INT,
    promo21 INT,
    promo22 INT,
    promo23 INT,
    promo24 INT,
    suprise INT,
    reputation INT,
    click INT,
    kitstart INT,
    id BIGINT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS bot(
    chat_id INT,
    last_stavka INT,
    curs INT, 
    last_curs INT,
    ivent INT,
    promo1 INT,
    promo2 INT,
    promo3 INT,
    promo4 INT,
    promo5 INT,
    promo6 INT,
    promo7 INT,
    promo8 INT,
    promo9 INT,
    promo10 INT,
    promo11 INT,
    promo12 INT,
    promo13 INT,
    promo14 INT,
    promo15 INT,
    promo16 INT,
    promo17 INT,
    promo18 INT,
    promo19 INT,
    promo20 INT,
    promo21 INT,
    promo22 INT,
    promo23 INT,
    promo24 INT,
    cazna INT,
    group_name STRING,
    group_time INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS chats(
    chat_id INT,
    cazna INT,
    group_name STRING,
    group_time INT
)
""")

marry_me = []
marry_rep = []
divorce_me = []
divorce_rep = []
user_me = []
user_rep = []

interval = 3600

async def farm():
    while True:
        base = cursor.execute(f"SELECT * FROM users").fetchall()
        num2 = 0
        for user in base:
            if user[83] == 1:
               cursor.execute(f'UPDATE users SET farm_coin = {user[88] + (user[89] * 1)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[84] == 1:
               cursor.execute(f'UPDATE users SET farm_coin = {user[88] + (user[89] * 5)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[85] == 1:
               cursor.execute(f'UPDATE users SET farm_coin = {user[88] + (user[89] * 25)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[86] == 1:
               cursor.execute(f'UPDATE users SET farm_coin = {user[88] + (user[89] * 450)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[87] == 1:
               cursor.execute(f'UPDATE users SET farm_coin = {user[88] + (user[89] * 3000)} WHERE user_id = {base[num2][0]}')
               connect.commit()    
            num2 += 1

        await asyncio.sleep(interval)

interval2 = 600

async def energy():
    while True:
        base = cursor.execute(f"SELECT * FROM users").fetchall()
        num2 = 0
        for user in base:
            if user[95] < 10:
               cursor.execute(f'UPDATE users SET ener = {user[95] + 1} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            num2 += 1

        await asyncio.sleep(interval2)

interval3 = 3600

async def farmcoin_start():
    while True:
        base = cursor.execute(f"SELECT * FROM users").fetchall()
        num2 = 0
        for user in base:
            if user[106] == 1:
               cursor.execute(f'UPDATE users SET bitmaning = {user[111] + (user[112] * 4)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[107] == 1:
               cursor.execute(f'UPDATE users SET bitmaning = {user[111] + (user[112] * 12)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[108] == 1:
               cursor.execute(f'UPDATE users SET bitmaning = {user[111] + (user[112] * 64)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[109] == 1:
               cursor.execute(f'UPDATE users SET bitmaning = {user[111] + (user[112] * 650)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[110] == 1:
               cursor.execute(f'UPDATE users SET bitmaning = {user[111] + (user[112] * 3500)} WHERE user_id = {base[num2][0]}')
               connect.commit()    
            num2 += 1

        await asyncio.sleep(interval3)

interval4 = 3600

async def business():
    while True:
        base = cursor.execute(f"SELECT * FROM users").fetchall()
        num2 = 0
        for user in base:
            if user[114] == 1:
               cursor.execute(f'UPDATE users SET busscash = {user[124] + 1000 + (user[123] * 100000)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[115] == 1:
               cursor.execute(f'UPDATE users SET busscash = {user[124] + 10000 + (user[123] * 100000)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[116] == 1:
               cursor.execute(f'UPDATE users SET busscash = {user[124] + 40000 + (user[123] * 100000)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[117] == 1:
               cursor.execute(f'UPDATE users SET busscash = {user[124] + 50000 + (user[123] * 100000)} WHERE user_id = {base[num2][0]}')
               connect.commit()  
            if user[118] == 1:
               cursor.execute(f'UPDATE users SET busscash = {user[124] + 75000 + (user[123] * 100000)} WHERE user_id = {base[num2][0]}')
               connect.commit()    
            if user[119] == 1:
               cursor.execute(f'UPDATE users SET busscash = {user[124] + 150000 + (user[123] * 100000)} WHERE user_id = {base[num2][0]}')
               connect.commit()
            if user[120] == 1:
               cursor.execute(f'UPDATE users SET busscash = {user[124] + 200000 + (user[123] * 100000)} WHERE user_id = {base[num2][0]}')
               connect.commit()
            if user[121] == 1:
               cursor.execute(f'UPDATE users SET busscash = {user[124] + 400000 + (user[123] * 100000)} WHERE user_id = {base[num2][0]}')
               connect.commit()
            if user[122] == 1:
               cursor.execute(f'UPDATE users SET busscash = {user[124] + 800000 + (user[123] * 100000)} WHERE user_id = {base[num2][0]}')
               connect.commit()
            num2 += 1

        await asyncio.sleep(interval4)

interval5 = 86400
async def limit_st():
    while True:
        cursor.execute(f'UPDATE users SET limit_trans = {0}')
        connect.commit() 
        await asyncio.sleep(interval5)

async def get_marry(message: types.Message):
    user = message.from_user
    marry = cursor.execute("SELECT marry FROM users WHERE user_id=?", (user.id,)).fetchall()
    return marry

async def get_rang(message: types.Message):
    user = message.from_user
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user.id,))
    data = cursor.fetchone()
    return data

async def reply_get_rang(message: types.Message):
    reply = message.reply_to_message
    replyuser = reply.from_user
    cursor.execute("SELECT * FROM users WHERE user_id=?", (replyuser.id,))
    data = cursor.fetchone()
    return data

async def anti_flood(*args, **kwargs):
    m = args[0]
    return

@dp.message_handler(commands=['start_energy'])
async def start_energy(message: types.Message):
    await bot.send_message(message.chat.id, f"Energy starting!")
    await energy()

@dp.message_handler(commands=['start_farm_saikawa'])
async def start_farm(message: types.Message):
    await bot.send_message(message.chat.id, f"Farm starting!")
    await farm()

@dp.message_handler(commands=['start_farmcoin'])
async def start_farmcoin(message: types.Message):
    await bot.send_message(message.chat.id, f"FarmCoin starting!")
    await farmcoin_start()

@dp.message_handler(commands=['start_business'])
async def start_business(message: types.Message):
    await bot.send_message(message.chat.id, f"Business starting!")
    await business()

@dp.message_handler(commands=['start_limit'])
async def start_limit(message: types.Message):
    await bot.send_message(message.chat.id, f"Business starting!")
    await limit_st()

###########################################СТАРТОВАЯ КОМАНДА###########################################
@dp.message_handler(commands=['ping'])
@dp.throttled(rate=2)
async def send_ping(message: types.Message):
    a = 5
    r = message.get_args()
    if r and r[0].isdigit():
        a = int(r[0])
    ping_msg = []
    ping_data = []
    for _ in range(a):
        start = datetime.now()
        msg = await bot.send_message(logchat, "ping")
        end = datetime.now()
        duration = (end - start).microseconds / 1000
        ping_data.append(duration)
        ping_msg.append(msg)
    ping = sum(ping_data) / len(ping_data)
    await message.reply(f"🏓 Пинг: {str(ping)[0:5]} ms.")
    for i in ping_msg:
        await i.delete()

# start command
@dp.message_handler(commands=['start'])
@dp.throttled(anti_flood, rate=1)
async def start_cmd(message):
    msg = message
    user_id = msg.from_user.id
    user_name = "Игрок"
    user_status = "Player"
    pet_name = "name"
    status = "Игрок"
    gender = "Не выбран"
    list1 = cursor.execute(f"SELECT * FROM users ORDER BY id DESC")
    uid = 10000
    for user in list1:
        uid += 1
    chat_id = message.chat.id
    group_name = message.chat.full_name
    cursor.execute(f"SELECT chat_id FROM bot WHERE chat_id = '{chat_id}'")
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
       cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (user_id, 5000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, user_name, 0, 0, 0, user_status, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, pet_name, 100, 100, 100, 0, datetime.now(), 0, 0, 0, 0, 0, 0, status, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, uid, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, gender, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
       cursor.execute("INSERT INTO bot VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (chat_id, 0, 50000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, group_name, datetime.now()))
       connect.commit()
    else:
       cursor.execute("INSERT INTO bot VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (chat_id, 0, 50000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, group_name, datetime.now()))
       connect.commit()

    photo = open('start.jpg', 'rb')
    name1 = message.from_user.get_mention(as_html=True)
    await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'👋 Привет, {name1} \nЯ бот для игры в различные игры.\nТебе выдан подарок в размере 5000$.\nТак же ты можешь добавить меня в беседу для игры с друзьями.\n🆘 Чтобы узнать все команды введи "Помощь"\n\n↘️ Чтобы добавить меня в свою группу нажмите кнопку ниже.', parse_mode='html', reply_markup=kb.help_cmd)

@dp.message_handler(commands=['kitstart'])
@dp.throttled(anti_flood, rate=1)
async def kitstart_cmd(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = user_name[0]
    kitstart = cursor.execute("SELECT kitstart from users where user_id = ?",(message.from_user.id,)).fetchone()
    kitstart = int(kitstart[0])
    car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
    car1 = int(car1[0])
    pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
    pet1 = int(pet1[0])
    balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
    balance = int(balance[0])
    rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
    rating = int(rating[0])
    photo = open('start.jpg', 'rb')
    if kitstart == 0:
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно забрали kitstart!\n📦 Получено:\n1. 🐥 Цыплёнок\n2. 🚗 ВАЗ 2107\n3. 💰 1.000.000$", parse_mode='html')
       cursor.execute(f'UPDATE users SET car1 = {1}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet1 = {1}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car2 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car3 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car4 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car5 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car6 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car7 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car8 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car9 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car10 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car11 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET car12 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet2 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet3 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet4 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet5 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet6 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet7 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet8 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet9 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET pet10 = {0}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET balance = {balance + 1000000}  WHERE user_id = ?', (user_id,))
       cursor.execute(f'UPDATE users SET kitstart = {1}  WHERE user_id = ?', (user_id,))
       connect.commit()
       return
    if kitstart == 1:
       await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы уже получали kitstart!", parse_mode='html')
       return

@dp.message_handler(commands=['bind'])
@dp.throttled(anti_flood, rate=1)
async def bind_cmd(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    group_name = message.chat.full_name
    cursor.execute(f"SELECT chat_id FROM chats WHERE chat_id = '{chat_id}'")
    if user_id == chat_id:
       print("Не могу зарегистрировать чат!")
       return 

    if cursor.fetchone() is None:
       cursor.execute("INSERT INTO chats VALUES(?, ?, ?, ?);", (chat_id, 0, group_name, datetime.now()))
       connect.commit()
    else:
       return
    photo = open('start.jpg', 'rb')
    await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f'🔗 | Чат "{group_name}" успешно зарегистрирован!', parse_mode='html')

@dp.message_handler(commands=['admin'])
async def adminstration(message: types.Message):
   if message.from_user.id == admin:
     await message.answer('Добро пожаловать в админ панель.', reply_markup=kb.apanel)
   else:
     await message.answer('Вы не являетесь создателем бота!')

# start command
@dp.message_handler(commands=['sticker'])
@dp.throttled(anti_flood, rate=0.5)
async def sticker_cmd(message):
    random_sticker = cursor2.execute("SELECT sticker_id FROM stickers ORDER BY RANDOM() LIMIT 1;").fetchall()
    random_sticker = str(random_sticker[0][0])
    await message.answer_sticker(sticker=random_sticker)

@dp.message_handler(commands=['send'])
@dp.throttled(anti_flood, rate=1)
async def send_cmd(message: types.Message):
    args = message.get_args()
    user_id = message.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(user_id,)).fetchone()
    user_name = user_name[0] 
    if len(args) >= 0 and args[0] == '':
       await message.reply("ℹ️ | Введите ваше сообщение после команды")
       return
    chat_message = -1001667057597
    await bot.send_message(chat_message, f"💭 Сообщение от: <a href='tg://user?id={user_id}'>{user_name}</a>\n💭 Текст сообщения: {args}", parse_mode='html')
    await bot.send_message(message.chat.id, f'💭 Ваше сообщение успешно отправлено администрации!')

@dp.callback_query_handler(lambda c: c.data == "rass")
async def rass(callback_query: types.CallbackQuery):
   usid = callback_query.from_user.id
   if usid == admin:
      await bot.send_message(callback_query.message.chat.id, f'Введите фото/текст для рассылки.\n\nДля отмены нажмите кнопку ниже 👇', reply_markup=kb.back)
      await info.rasst.set()



@dp.callback_query_handler(lambda c: c.data == "getdb")
async def getdb(callback_query: types.CallbackQuery):
   usid = callback_query.from_user.id
   if usid == admin:
      newzip = zipfile.ZipFile('users.zip', 'w')
      newzip.write('users.db', compress_type=zipfile.ZIP_DEFLATED)
      get_db = open(f'users.zip', 'rb')
      await bot.send_document(chat_id=callback_query.message.chat.id, document=get_db, caption=f'<b>🚀 Держи!</b>', parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "stats")
async def stats(callback_query: types.CallbackQuery):
   cursor.execute(f"SELECT user_id FROM users")
   users = cursor.fetchall()
   cursor.execute(f"SELECT chat_id FROM chats")
   chats = cursor.fetchall()
   cursor.execute(f"SELECT chat_id FROM bot")
   message = cursor.fetchall()
   cursor2.execute(f"SELECT sticker_id FROM stickers")
   stickers = cursor2.fetchall()
   usid = callback_query.from_user.id
   list = cursor.execute(f"SELECT * FROM users")
   num = 0
   for user in list:
       num += user[1]
   num2 = '{0:,}'.format(num).replace(',', '.')
   if usid == admin:
      await bot.send_message(callback_query.message.chat.id, f'📊 Пользователей в боте: {str(len(users))}\n📊 Чатов в боте: {str(len(chats))}\n📊 Обработано сообщений: {str(len(message))}\n📊 Игровой валюты: {num2}$\n📊 Стикеров: {str(len(stickers))}')

@dp.callback_query_handler(lambda c: c.data == "owner")
async def owner(callback_query: types.CallbackQuery):
   usid = callback_query.from_user.id
   user_status = "Owner"
   if usid == admin:
      await bot.send_message(callback_query.message.chat.id, f'💎 Вы успешно восстановили роль "Владельца"')
      cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{usid}"')
      connect.commit()

@dp.callback_query_handler(lambda call: call.data.startswith('click_menu'))    
async def click_menu(call):
    await call.message.answer('Чтобы начать зарабатывать нажимай на кнопку: 👇 Клик.\n\nДля отмены нажмите на кнопку: Отмена', reply_markup=kb.click_back)
    await info.click.set()

@dp.callback_query_handler(lambda c: c.data == "help")
async def help(callback_query: types.CallbackQuery):
    usid = callback_query.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
    user_name = user_name[0] 
    await bot.send_message(callback_query.message.chat.id, f"<a href='tg://user?id={usid}'>{user_name}</a>, выберите категорию:\n   1️⃣ Основное\n   2️⃣ Игры\n   3️⃣ Развлекательные\n   4️⃣ Имущество\n\n💬 Так же у нас есть <a href='https://t.me/Rave_chatt'>общая беседа</a>\n🆘 По всем вопросам - <a href='tg://user?id=5361352348'>Rave</a>", parse_mode='html', reply_markup=kb.help_menu)

@dp.callback_query_handler(lambda c: c.data == "main")
async def main(callback_query: types.CallbackQuery):
    usid = callback_query.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
    user_name = user_name[0] 
    await bot.send_message(callback_query.message.chat.id, f"<a href='tg://user?id={usid}'>{user_name}</a>, основные команды:\n   📒 Профиль\n   💸 Б/Баланс\n   👨 Ник - узнать ник\n   📦 Инвентарь\n   📊 Курс руды\n   ⛏ Шахта\n   ✏️ Cменить ник [ник]\n   👑 Рейтинг/купить/продать [сумма]\n   🏦 Банк/снять/положить [сумма]\n   💰 Казна положить [сумма]\n   ℹ️ Инфо - информация о чате\n   🤝 Дать [сумма] [команда работает ответом на сообщение]\n   🤝 Передать [сумма] [ID]\n   💎 Топ\n   💎 Топ чатов\n   🌐 Биткоин/продать/купить/курс[кол-во]\n   💈 Ежедневный бонус\n   🎁 Задание\n   🛢 Заправка\n   💻 Работать\n   💭 !Беседа - беседа бота\n   ❤️ !Сайт - наш сайт", parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "games")
async def games(callback_query: types.CallbackQuery):
    usid = callback_query.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
    user_name = user_name[0] 
    await bot.send_message(callback_query.message.chat.id, f"<a href='tg://user?id={usid}'>{user_name}</a>, игровые команды:\n   🎮 Спин [ставка]\n   🎰 Казино [ставка]\n   🎲 Кубик [1-6] [ставка]\n   🏎 Гонки [ставка]\n   ⚔️ Бой [ставка]\n   📦 Кейсы", parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "entertainment")
async def entertainment(callback_query: types.CallbackQuery):
    usid = callback_query.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
    user_name = user_name[0] 
    await bot.send_message(callback_query.message.chat.id, f"<a href='tg://user?id={usid}'>{user_name}</a>, развлекательные команды:\n   🔮 Шар\n   🧿 Шанс\n   👤 Выбрать пол\n   💖 Брак\n         💔Развод\n\n   💭 РП-команды - вывести список РП-команд", parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "men")
async def men(callback_query: types.CallbackQuery):
    usid = callback_query.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
    user_name = user_name[0] 
    gender = "Мужской"
    await callback_query.message.delete()
    await bot.send_message(callback_query.message.chat.id, f"👤 | <a href='tg://user?id={usid}'>{user_name}</a>, вы успешно выбрали мужской пол!", parse_mode='html')
    cursor.execute(f'UPDATE users SET gender = \"{gender}\"  WHERE user_id = ?', (usid,))
    connect.commit()  

@dp.callback_query_handler(lambda c: c.data == "women")
async def women(callback_query: types.CallbackQuery):
    usid = callback_query.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
    user_name = user_name[0] 
    gender = "Женский"
    await callback_query.message.delete()
    await bot.send_message(callback_query.message.chat.id, f"👤 | <a href='tg://user?id={usid}'>{user_name}</a>, вы успешно выбрали женский пол!", parse_mode='html')
    cursor.execute(f'UPDATE users SET gender = \"{gender}\"  WHERE user_id = ?', (usid,))
    connect.commit()  

@dp.callback_query_handler(lambda c: c.data == "property")
async def property(callback_query: types.CallbackQuery):
    usid = callback_query.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
    user_name = user_name[0] 
    await bot.send_message(callback_query.message.chat.id, f"<a href='tg://user?id={usid}'>{user_name}</a>, доступное имущество:\n   🎡 Электростанции\n        🎡 Моя электростанция\n        💸 Купить электростанцию [номер]\n        🔌 Купить турбины [кол-во]\n        💰 Продать электростанцию\n         💳 Продать турбины [кол-во]\n         💵 Электростанция снять [кол-во]\n\n   🧰 Фермы\n        🔋 Моя ферма\n        💸 Купить ферму [номер]\n        🔌 Купить видеокарту [кол-во]\n        💰 Продать ферму\n        💳 Продать видеокарту [кол-во]\n        💵 Ферма снять [кол-во]\n\n   🗄 Бизнесы\n         💰 Мой бизнес\n         💵 Купить бизнес [номер]\n         👷 Купить рабочих [кол-во]\n         💸 Продать бизнес\n         💲 Бизнес снять [кол-во]\n\n   🚗 Машины\n         🚗 Моя машина - узнать о своей машине\n\n   🐶 Питомцы\n        ✏️ Питомец имя [имя]\n        ❤️ Вылечить питомца\n        🍗 Покормить питомца\n        🌳 Выгулять питомца\n        🐶 Мой питомец - узнать о своём питомце", parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "check")
async def channel(callback_query: types.CallbackQuery):
    usid = callback_query.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
    user_name = user_name[0] 
    balance = cursor.execute("SELECT balance from users where user_id = ?",(usid,)).fetchone()
    balance = int(balance[0])
    check_channel = cursor.execute("SELECT check_channel from users where user_id = ?",(usid,)).fetchone()
    check_channel = check_channel[0]
    some_var = await bot.get_chat_member(-10017182440277, usid)
    check_channel = cursor.execute("SELECT check_channel FROM users WHERE user_id = ?",(usid,)).fetchone()
    check_channel = int(check_channel[0])
    if check_channel == 1:
       await bot.send_message(callback_query.message.chat.id, f"ℹ️ | <a href='tg://user?id={usid}'>{user_name}</a>, вы не можете выполнить задание повторно!", parse_mode='html')
       return

    if some_var.status == 'member' or some_var.status == 'administrator' or some_var.status == 'creator':
       await bot.send_message(callback_query.message.chat.id, f"✅ | <a href='tg://user?id={usid}'>{user_name}</a>, вы успешно выполнили задание! \n🎁 | На ваш баланс зачислено: 10.000.000.000$", parse_mode='html')
       cursor.execute(f'UPDATE users SET balance = {balance + 10000000000}  WHERE user_id = ?', (usid,))
       cursor.execute(f'UPDATE users SET check_channel = {1}  WHERE user_id = ?', (usid,))
       connect.commit()            
    else:
       await bot.send_message(callback_query.message.chat.id, f"🚫 | <a href='tg://user?id={usid}'>{user_name}</a>, вы не подписались на наш канал!", parse_mode='html')             

@dp.message_handler(state=info.click)
async def process_name(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
       await message.answer('Отмена! Возвращаю в главное меню.')
       await state.finish()
    if message.text == '👇 Клик':
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       click = cursor.execute("SELECT click from users where user_id = ?",(message.from_user.id,)).fetchone()
       click = int(click[0])
       chat_id = message.chat.id
       if chat_id == -1001590519834:
          await message.answer('В этой беседе запрещено кликать!')
          return
       if chat_id == -1001478520848:
          await message.answer('В этой беседе запрещено кликать!')
          return

       await message.answer('+500.000$', reply_markup=kb.click_back)
       cursor.execute(f'UPDATE users SET balance = {balance + 500000}  WHERE user_id = ?', (message.from_user.id,))
       cursor.execute(f'UPDATE users SET click = {click + 1}  WHERE user_id = ?', (message.from_user.id,))
       connect.commit()

@dp.message_handler(content_types=types.ContentType.ANY, state=info.rasst)
async def rass(message: types.Message, state: FSMContext):
    cursor.execute(f'SELECT user_id FROM users')
    row = cursor.fetchall()
    connect.commit()
    users = [user[0] for user in row] 
    if message.text == 'Отмена':
       await message.answer('Отмена! Возвращаю в главное меню.', reply_markup=types.ReplyKeyboardRemove())
       await state.finish()
    else:
       await message.answer('Начинаю рассылку...')
       for i in users:
           try:
              await message.copy_to(i)
           except:
              pass

       await message.answer('Рассылка завершена.', reply_markup=types.ReplyKeyboardRemove())
       await state.finish()

@dp.message_handler(content_types=["sticker"])
async def add_sticker(message: types.Message):
    if message.chat.id == -699801632:
       file_id = message.sticker.file_id
       cursor2.execute(f"SELECT sticker_id FROM stickers WHERE sticker_id = '{file_id}'")
       if cursor2.fetchone() is None:      
          cursor2.execute("INSERT INTO stickers VALUES(?);", (file_id,))
          connect2.commit()
       else:
          return
    else:
       return

@dp.message_handler(commands=['мут', 'mute'], commands_prefix='!?./', is_chat_admin=True)
async def mute(message):
   msg = message
   user_name = message.from_user.full_name
   ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
   user_id = msg.from_user.id
   ruser_name = message.reply_to_message.from_user.full_name
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   try:
      muteint = int(message.text.split()[1])
      mutetype = message.text.split()[2]
   except IndexError:
      await message.reply('ℹ | Не хватает аргументов!\nПример:  /mute 1 ч')
      return
   if mutetype == "ч" or mutetype == "часов" or mutetype == "час":
      dt = datetime.now() + timedelta(hours=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f"Администратор <a href='tg://user?id={user_id}'>{user_name}</a> выдал затычку пользователю <a href='tg://user?id={message.reply_to_message.from_user.id}'>{ruser_name}</a> на {muteint} {mutetype}",  parse_mode='html')
   if mutetype == "м" or mutetype == "минут" or mutetype == "минуты":
      dt = datetime.now() + timedelta(minutes=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f"Администратор <a href='tg://user?id={user_id}'>{user_name}</a> выдал затычку пользователю <a href='tg://user?id={message.reply_to_message.from_user.id}'>{ruser_name}</a> на {muteint} {mutetype}",  parse_mode='html')
   if mutetype == "д" or mutetype == "дней" or mutetype == "день":
      dt = datetime.now() + timedelta(days=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f"Администратор <a href='tg://user?id={user_id}'>{user_name}</a> выдал затычку пользователю <a href='tg://user?id={message.reply_to_message.from_user.id}'>{ruser_name}</a> на {muteint} {mutetype}",  parse_mode='html')

@dp.message_handler(commands=['размут', 'unmute'], commands_prefix='!?./', is_chat_admin=True)
async def unmute(message):
   msg = message
   user_name = message.from_user.full_name
   ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
   user_id = msg.from_user.id
   ruser_name = message.reply_to_message.from_user.full_name
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
   await message.reply(f"Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> разрешил говорить пользователю <a href='tg://user?id={message.reply_to_message.from_user.id}'>{ruser_name}</a>",  parse_mode='html')

@dp.message_handler(commands=['ban', 'бан', 'кик', 'kick'], commands_prefix='!?./', is_chat_admin=True)
async def ban(message):
   msg = message
   user_name = message.from_user.full_name
   ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
   user_id = msg.from_user.id
   ruser_name = message.reply_to_message.from_user.full_name
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
   await message.reply(f"Администратор <a href='tg://user?id={user_id}'>{user_name}</a> забанил пользователя <a href='tg://user?id={message.reply_to_message.from_user.id}'>{ruser_name}</a> навсегда",  parse_mode='html')

@dp.message_handler(commands=['разбан', 'unban'], commands_prefix='!?./', is_chat_admin=True)
async def unban(message):
   msg = message
   user_name = message.from_user.full_name
   ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
   user_id = msg.from_user.id
   ruser_name = message.reply_to_message.from_user.full_name
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
   await message.reply(f"Администратор: <a href='tg://user?id={user_id}'>{user_name}</a> разбанил пользователя <a href='tg://user?id={message.reply_to_message.from_user.id}'>{ruser_name}</a>",  parse_mode='html')

@dp.callback_query_handler(lambda c: c.data == "button_marry_y")
async def callback_marry_y(callback_query: types.CallbackQuery):
    user = await bot.get_chat(str(marry_me[0]))
    replyuser = await bot.get_chat(str(marry_rep[0]))
    usid = user.id
    rid = replyuser.id
    ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(rid,)).fetchone()
    ruser_name = ruser_name[0] 
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
    user_name = user_name[0] 
    if callback_query.from_user.id == replyuser.id:
        cursor.execute(f'UPDATE users SET marry=? WHERE user_id=?', (replyuser.id, user.id,))
        cursor.execute(f'UPDATE users SET marry_time=? WHERE user_id=?', (time.time(), user.id,))
        cursor.execute(f'UPDATE users SET marry_date=? WHERE user_id=?', (datetime.now(), user.id,))

        cursor.execute(f'UPDATE users SET marry=? WHERE user_id=?', (user.id, replyuser.id,))
        cursor.execute(f'UPDATE users SET marry_time=? WHERE user_id=?', (time.time(), replyuser.id,))
        cursor.execute(f'UPDATE users SET marry_date=? WHERE user_id=?', (datetime.now(), replyuser.id,))
        connect.commit()

        marry_me.clear()
        marry_rep.clear() 
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"💍 Вы приняли предложение о браке.\n👰‍♀️👨‍⚖️ С сегодняшего дня <a href='tg://user?id={usid}'>{user_name}</a> и <a href='tg://user?id={rid}'>{ruser_name}</a> состоят в браке.\n✨ Давайте поздравим молодожён!",  parse_mode='html')
    else:
        await bot.answer_callback_query(callback_query.id, show_alert=False, text="⚠️ Не твоё, не трогай!")

@dp.callback_query_handler(lambda c: c.data == "button_marry_n")
async def callback_marry_n(callback_query: types.CallbackQuery):
    user = await bot.get_chat(str(marry_me[0]))
    replyuser = await bot.get_chat(str(marry_rep[0]))
    if callback_query.from_user.id == replyuser.id:
       usid = user.id 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
       user_name = user_name[0]
       marry_me.clear()
       marry_rep.clear()
       await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
       await bot.send_message(callback_query.message.chat.id, f"💔 | <a href='tg://user?id={usid}'>{user_name}</a>, сожалеем, но вам отказали",  parse_mode='html')
    else:
       await bot.answer_callback_query(callback_query.id, show_alert=False, text="⚠️ Не твоё, не трогай!")

@dp.callback_query_handler(lambda c: c.data == "button_divorce_y")
async def callback_divorce_y(callback_query: types.CallbackQuery):
    user = await bot.get_chat(str(divorce_me[0]))
    if callback_query.from_user.id == user.id:
        replyuser = await bot.get_chat(str(divorce_rep[0]))
        usid = user.id
        rid = replyuser.id
        ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(rid,)).fetchone()
        ruser_name = ruser_name[0] 
        user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
        user_name = user_name[0]
        get = cursor.execute("SELECT marry_time FROM users WHERE user_id=?", (user.id,)).fetchall()
        mtime = f"{int(get[0][0])}"
        marry_time = time.time() - float(mtime)
        vremya = strftime("%j дней %H часов %M минут", gmtime(marry_time))


        cursor.execute(f'UPDATE users SET marry=? WHERE user_id=?', (0, user.id,))
        cursor.execute(f'UPDATE users SET marry_time=? WHERE user_id=?', (0, user.id,))
        cursor.execute(f'UPDATE users SET marry_date=? WHERE user_id=?', (0, user.id,))

        cursor.execute(f'UPDATE users SET marry=? WHERE user_id=?', (0, replyuser.id,))
        cursor.execute(f'UPDATE users SET marry_time=? WHERE user_id=?', (0, replyuser.id,))
        cursor.execute(f'UPDATE users SET marry_date=? WHERE user_id=?', (0, replyuser.id,))
        connect.commit()
        divorce_me.clear()
        divorce_rep.clear()
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"💔 Брак между <a href='tg://user?id={usid}'>{user_name}</a> и <a href='tg://user?id={rid}'>{ruser_name}</a> расторгнут.\n"
                                                               f"Он просуществовал {vremya}",  parse_mode='html')
    else:
        await bot.answer_callback_query(callback_query.id, show_alert=False, text="⚠️ Не твоё, не трогай!")

@dp.callback_query_handler(lambda c: c.data == "button_divorce_n")
async def callback_divorce_n(callback_query: types.CallbackQuery):
    user = await bot.get_chat(str(divorce_me[0]))
    if callback_query.from_user.id == user.id:
        divorce_me.clear()
        divorce_rep.clear()
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
    else:
        await bot.answer_callback_query(callback_query.id, show_alert=False, text="⚠️ Не твоё, не трогай!") 


# prof_user
@dp.message_handler()
@dp.throttled(anti_flood, rate=0.8)
async def users(message: types.Message):
###########################################ОСНОВНЫЕ КОМАНДЫ###########################################
    if message.forward_from != None:
       return
    else:
       pass
    
    if message.from_user.id == 136817688:
       print("channel/group")
       print(message.from_user.id)
       return
    else:
       print("user")
       print(message.from_user.id)
       pass
    
    msg = message
    chat_id = message.chat.id
    user_id = message.from_user.id
    cursor.execute(f"SELECT chat_id FROM bot WHERE chat_id = '{chat_id}'")
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
       msg = message
       user_id = msg.from_user.id
       user_name = "Игрок"
       user_status = "Player"
       pet_name = "name"
       status = "Игрок"
       list1 = cursor.execute(f"SELECT * FROM users ORDER BY id DESC")
       uid = 10000
       for user in list1:
           uid += 1
       chat_id = message.chat.id
       gender = "Не выбран"
       group_name = message.chat.full_name
       cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (user_id, 5000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, user_name, 0, 0, 0, user_status, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, pet_name, 100, 100, 100, 0, datetime.now(), 0, 0, 0, 0, 0, 0, status, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, uid, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, gender, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
       cursor.execute("INSERT INTO bot VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (chat_id, 0, 50000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, group_name, datetime.now()))
       connect.commit()
       #start_photo = open('start.jpg', 'rb')
       #name1 = message.from_user.get_mention(as_html=True)
       #await message.bot.send_photo(chat_id=message.chat.id, photo=start_photo, caption=f'👋 Привет, {name1} \nЯ бот для игры в различные игры.\nТебе выдан подарок в размере 5000$.\nТак же ты можешь добавить меня в беседу для игры с друзьями.\n🆘 Чтобы узнать все команды введи "Помощь"', parse_mode='html', reply_markup=kb.help_cmd)
    else:
       chat_id = message.chat.id
       group_name = message.chat.full_name
       cursor.execute("INSERT INTO bot VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (chat_id, 0, 50000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, group_name, datetime.now()))
       connect.commit()
    

    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    if user_status[0] == "Blocked":
       try:
           return
       except TypeError:
           return
    else:
       pass
    
    user_name = cursor.execute("SELECT user_name FROM users WHERE user_id = ?",(message.from_user.id,)).fetchone()
    user_name = user_name[0]
    win = ['🙂', '😋', '😄', '🤑', '😃']
    rwin = random.choice(win)
    loser = ['😔', '😕', '😣', '😞', '😢']
    rloser = random.choice(loser)
    ivent = cursor.execute("SELECT ivent from bot").fetchone()
    ivent = int(ivent[0])
    egg = cursor.execute("SELECT egg from users where user_id = ?",(message.from_user.id,)).fetchone()
    egg = int(egg[0])
    period = 86400
    get = cursor.execute("SELECT last_snow FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
    last_snow = f"{int(get[0])}"
    snowtime = time.time() - float(last_snow)
    if ivent == 1:
       if snowtime > period:
          await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={message.from_user.id}'>{user_name}</a>, вы успешно собрали 9 яиц! {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET egg = {egg + 9} WHERE user_id = "{message.from_user.id}"') 
          cursor.execute(f'UPDATE users SET last_snow=? WHERE user_id=?', (time.time(), message.from_user.id,))
       else:
          pass
    if ivent == 0:
       pass
    
    
    #text = message.text
    #user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    #user_name = user_name[0]
    #user_id = message.from_user.id
    #chat_id = message.chat.id
    #usgroup_name = message.chat.username
    #group_name = message.chat.full_name
    #await bot.send_message(globallog, f"💭 Сообщение: {text} \n👤 От пользователя: <a href='tg://user?id={user_id}'>{user_name}</a>\n🔊 Чат: <a href='https://t.me/{usgroup_name}'>{group_name}</a>", parse_mode='html')

    if "https" in message.text:
       duration = 5
       dt = datetime.now() + timedelta(minutes=duration)
       timestamp = dt.timestamp()
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name FROM users WHERE user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await message.bot.restrict_chat_member(message.chat.id, message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы замучены на 5 минут за отправку ссылок!", parse_mode='html')
       await message.delete()
       return

    if "http" in message.text:
       duration = 5
       dt = datetime.now() + timedelta(minutes=duration)
       timestamp = dt.timestamp()
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name FROM users WHERE user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await message.bot.restrict_chat_member(message.chat.id, message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы замучены на 5 минут за отправку ссылок!", parse_mode='html')
       await message.delete()
       return

    if "t.me" in message.text:
       duration = 5
       dt = datetime.now() + timedelta(minutes=duration)
       timestamp = dt.timestamp()
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name FROM users WHERE user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await message.bot.restrict_chat_member(message.chat.id, message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы замучены на 5 минут за отправку ссылок!", parse_mode='html')
       await message.delete()
       return

    if message.text.lower() in ["+", "жиза"]:
       if message.from_user.id == message.reply_to_message.from_user.id:
          await message.reply("Вы не можете голосовать за самого себя")
          return
       else:       
          reply_user_id = message.reply_to_message.from_user.id
          ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(reply_user_id,)).fetchone()
          ruser_name = ruser_name[0] 
          reputation = cursor.execute("SELECT reputation from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
          reputation = round(reputation[0]) 
          cursor.execute(f'UPDATE users SET reputation = {reputation + 1} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
  
          await message.reply(f"Вы повысили репутацию игроку: <a href='tg://user?id={reply_user_id}'>{ruser_name}</a>", parse_mode='html')
          
    if message.text.lower() in ["-"]:
       if message.from_user.id == message.reply_to_message.from_user.id:
          await message.reply("Вы не можете голосовать за самого себя")
          return
       reply_user_id = message.reply_to_message.from_user.id
       ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(reply_user_id,)).fetchone()
       ruser_name = ruser_name[0] 
       reputation = cursor.execute("SELECT reputation from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       reputation = round(reputation[0])  
       await message.reply(f"Вы понизили репутацию игроку: <a href='tg://user?id={reply_user_id}'>{ruser_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET reputation = {reputation - 1} WHERE user_id = "{reply_user_id}"')
       connect.commit() 

    # money
    if message.text.lower() in ["кликер", "Кликер"]:
       chat_id = message.chat.id
       if chat_id == -1001590519834:
          await message.answer('В этой беседе запрещено кликать!')
          return
       if chat_id == -1001478520848:
          await message.answer('В этой беседе запрещено кликать!')
          return
       await message.answer('👇 Вы зашли в мини-игру кликер. Для продолжения нажмите кнопку ниже', reply_markup=kb.click_menu)
    
    if message.text.lower() in ["!беседа", "!Беседа"]:
       await bot.send_message(message.chat.id, f"💭 <a href='https://t.me/gbtgame_chat'>Общая беседа #1</a>", parse_mode='html')
    
    if message.text.lower() in ["!сайт", "!Сайт"]:
       await bot.set_chat_menu_button(message.chat.id, types.MenuButtonWebApp(text="❤️ Наш сайт", web_app=types.WebAppInfo(url=f"https://senpay701.github.io/saikawa/index.html")))
       await bot.send_message(text="↘️ Для перехода к нашему сайту нажмите кнопку ниже.", chat_id=message.chat.id, reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="❤️ Наш сайт", web_app=types.WebAppInfo(url=f"https://senpay701.github.io/saikawa/index.html"))]]))

    if message.text.lower() in ["Задание", "задание"]: 
       msg = message
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name FROM users WHERE user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       check_channel = cursor.execute("SELECT check_channel FROM users WHERE user_id = ?",(message.from_user.id,)).fetchone()
       check_channel = int(check_channel[0])
       if check_channel == 0:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, за подписку на наш канал вы получите 10.000.000.000$ на свой баланс!", parse_mode='html', reply_markup=kb.channel)
       if check_channel == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете выполнить задание повторно!", parse_mode='html')


    if message.text.lower() in ["баланс", "Баланс", "Б", "б"]:
       msg = message
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       balance2 = '{0:,}'.format(balance).replace(',', '.')
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{0:,}'.format(bank).replace(',', '.')
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitcoin = round(int(bitcoin[0]))
       bitcoin2 = '{0:,}'.format(bitcoin).replace(',', '.')
       c = 999999999999999999999999
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{0:,}'.format(balance).replace(',', '.')
       else:
        pass
       if bank >= 999999999999999999999999:
          bank = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bank2 = '{0:,}'.format(bank).replace(',', '.')
       else:
        pass
       if bitcoin >= 999999999999999999999999:
          bitcoin = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bitcoin2 = '{0:,}'.format(bitcoin).replace(',', '.')
       else:
        pass
       await bot.send_message(message.chat.id, f"👫Ник: {user_name} \n💰Деньги: {balance2}$ \n🏦Банк: {bank2}$\n💽 Биткоины: {bitcoin2}฿")
    # nick
    if message.text.lower() in ["ник", "Ник"]:
       msg = message 
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await bot.send_message(message.chat.id, f"🗂 Ваш ник - {user_name}")

    if message.text.lower() in ["банк", "Банк"]:
       msg = message 
       user_id = msg.from_user.id
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       if bank >= 999999999999999999999999:
          bank = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bank2 = '{0:,}'.format(bank).replace(',', '.')
       else:
        pass
       msg = message 
       bank2 = '{0:,}'.format(bank).replace(',', '.')
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, ваш банковский счёт:\n👫 Владелец: {user_name}\n💰 Деньги в банке: {bank2}$", parse_mode='html')

    if message.text.lower() in ["Инфо", "инфо", "информация", "Информация"]: 
       chat_id = message.chat.id
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       group_name = message.chat.full_name
       cazna = cursor.execute("SELECT cazna from chats where chat_id = ?",(chat_id,)).fetchone()
       cazna = round(int(cazna[0]))
       cazna2 = '{0:,}'.format(cazna).replace(',', '.')
       get = cursor.execute("SELECT group_time FROM chats WHERE chat_id = ?", (chat_id,)).fetchall()
       date_time = datetime.fromisoformat(get[0][0])
       times = date_time.strftime( "%d.%m.%Y %H:%M:%S" ) 
       photo = open('chat_info.png', 'rb')
       await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о чате:\n 🔎 ID: {chat_id}\n 🗂 Ник чата: {group_name}\n 💰 Казна: {cazna2}$\n 📅 Дата регистрации беседы: {times}", parse_mode='html')

    if message.text.startswith("казна положить"):
       await asyncio.sleep(1)   
       chat_id = message.chat.id
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       group_name = message.chat.full_name
       cazna = cursor.execute("SELECT cazna from chats where chat_id = ?",(chat_id,)).fetchone()
       cazna = round(int(cazna[0]))
       cazna2 = '{0:,}'.format(cazna).replace(',', '.')
       summ = int(message.text.split()[2])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(user_id,)).fetchone()
       balance = round(int(balance[0]))
       c = Decimal(summ)
       c2 = round(c)
       c2 = '{0:,}'.format(c2).replace(',', '.')
       if summ > 0:
          if balance >= summ:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно положили {c2}$ в казну чата!", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE chats SET cazna = {cazna + summ} WHERE chat_id = "{chat_id}"')
             connect.commit() 
          elif int(balance) <= int(summ):
             await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       elif summ <= 0:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя положить в казну отрицательное число! {rloser}", parse_mode='html')                                                       
  
    if message.text.startswith("Казна положить"): 
       await asyncio.sleep(1)  
       chat_id = message.chat.id
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       group_name = message.chat.full_name
       cazna = cursor.execute("SELECT cazna from chats where chat_id = ?",(chat_id,)).fetchone()
       cazna = round(int(cazna[0]))
       cazna2 = '{0:,}'.format(cazna).replace(',', '.')
       summ = int(message.text.split()[2])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(user_id,)).fetchone()
       balance = round(int(balance[0]))
       c = Decimal(summ)
       c2 = round(c)
       c2 = '{0:,}'.format(c2).replace(',', '.')
       if summ > 0:
          if balance >= summ:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно положили {c2}$ в казну чата!", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE chats SET cazna = {cazna + summ} WHERE chat_id = "{chat_id}"')
             connect.commit() 
          elif int(balance) <= int(summ):
             await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       elif summ <= 0:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя положить в казну отрицательное число! {rloser}", parse_mode='html')                                                       

    if message.text.lower() in ["рейтинг", "Рейтинг"]: 
       msg = message 
       user_id = msg.from_user.id
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = round(int(rating[0]))
       if rating >= 999999999999999999999999:
          rating = 999999999999999999999999
          cursor.execute(f'UPDATE users SET rating = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          rating2 = '{0:,}'.format(rating).replace(',', '.')
       else:
        pass
       msg = message 
       rating2 = '{0:,}'.format(rating).replace(',', '.')
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, ваш рейтинг {rating2}👑", parse_mode='html')

    if message.text.lower() in ["биткоин", "Биткоин"]: 
       msg = message 
       user_id = msg.from_user.id
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitcoin = round(int(bitcoin[0]))
       if bitcoin >= 999999999999999999999999:
          bitcoin = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bitcoin2 = '{0:,}'.format(bitcoin).replace(',', '.')
       else:
        pass
       msg = message 
       bitcoin2 = '{0:,}'.format(bitcoin).replace(',', '.')
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, на вашем счету {bitcoin2} BTC", parse_mode='html')

    if message.text.lower() in ["профиль", "Профиль"]:
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       uid = cursor.execute("SELECT id from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       games = cursor.execute("SELECT games from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       rep = cursor.execute("SELECT reputation from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone()
       gender = cursor.execute("SELECT gender from users where user_id = ?",(message.from_user.id,)).fetchone()
       flower = cursor.execute("SELECT flower from users where user_id = ?",(message.from_user.id,)).fetchone()
       scoin = cursor.execute("SELECT scoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       egg = cursor.execute("SELECT egg from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       games = int(games[0])
       bank = int(bank[0])
       bitcoin = int(bitcoin[0])
       expe = int(expe[0])
       rep = int(rep[0])
       rating = int(rating[0])
       uid = int(uid[0])
       energy = int(energy[0])
       gender = str(gender[0])
       flower = int(flower[0])
       scoin = int(scoin[0])
       egg = int(egg[0])
       scoin2 = '{0:,}'.format(scoin).replace(',', '.')
       egg2 = '{0:,}'.format(egg).replace(',', '.')
       status = cursor.execute("SELECT status from users where user_id = ?",(message.from_user.id,)).fetchone()
       status = str(status[0])
       click = cursor.execute("SELECT click from users where user_id = ?",(message.from_user.id,)).fetchone()
       click = int(click[0])
       c = 999999999999999999999999
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit() 
       else:
        pass
       if int(balance) in range(0, 1000):
          balance3 = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
          balance3 = int(balance3[0])
       if int(balance) in range(1000, 999999):
          balance1 = balance / 1000
          balance2 = round(balance1)
          balance3 = f'{balance2} тыс'
       if int(balance) in range(1000000, 999999999):
          balance1 = balance / 1000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млн'
       if int(balance) in range(1000000000, 999999999999):
          balance1 = balance / 1000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млрд'
       if int(balance) in range(1000000000000, 999999999999999):
          balance1 = balance / 1000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} трлн'
       if int(balance) in range(1000000000000000, 999999999999999999):
          balance1 = balance / 1000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квдр'
       if int(balance) in range(1000000000000000000, 999999999999999999999):
          balance1 = balance / 1000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квнт'
       if int(balance) in range(1000000000000000000000, 999999999999999999999999):
          balance1 = balance / 1000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} скст'
       if bank >= 999999999999999999999999:
          bank = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()   
       else:
        pass
       if int(bank) in range(0, 1000):
          bank3 = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
          bank3 = int(bank3[0])
       if int(bank) in range(1000, 999999):
          bank1 = bank / 1000
          bank2 = round(bank1)
          bank3 = f'{bank2} тыс'
       if int(bank) in range(1000000, 999999999):
          bank1 = bank / 1000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млн'
       if int(bank) in range(1000000000, 999999999999):
          bank1 = bank / 1000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млрд'
       if int(bank) in range(1000000000000, 999999999999999):
          bank1 = bank / 1000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} трлн'
       if int(bank) in range(1000000000000000, 999999999999999999):
          bank1 = bank / 1000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квдр'
       if int(bank) in range(1000000000000000000, 999999999999999999999):
          bank1 = bank / 1000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квнт'
       if int(bank) in range(1000000000000000000000, 999999999999999999999999):
          bank1 = bank / 1000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} скст'
       if bitcoin >= 999999999999999999999999:
          bitcoin = 999999999999999999999999
          cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()   
       else:
        pass
       if int(bitcoin) in range(0, 1000):
          bitcoin3 = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
          bitcoin3 = int(bitcoin3[0])
       if int(bitcoin) in range(1000, 999999):
          bitcoin1 = bitcoin / 1000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} тыс'
       if int(bitcoin) in range(1000000, 999999999):
          bitcoin1 = bitcoin / 1000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} млн'
       if int(bitcoin) in range(1000000000, 999999999999):
          bitcoin1 = bitcoin / 1000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} млрд'
       if int(bitcoin) in range(1000000000000, 999999999999999):
          bitcoin1 = bitcoin / 1000000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} трлн'
       if int(bitcoin) in range(1000000000000000, 999999999999999999):
          bitcoin1 = bitcoin / 1000000000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} квдр'
       if int(bitcoin) in range(1000000000000000000, 999999999999999999999):
          bitcoin1 = bitcoin / 1000000000000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} квнт'
       if int(bitcoin) in range(1000000000000000000000, 999999999999999999999999):
          bitcoin1 = bitcoin / 1000000000000000000000
          bitcoin2 = round(bitcoin1)
          bitcoin3 = f'{bitcoin2} скст'
       if expe >= 999999999999999999999999:
          expe = 999999999999999999999999
          cursor.execute(f'UPDATE users SET expe = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
       else:
        pass
       if int(expe) in range(0, 1000):
          expe3 = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
          expe3 = int(expe3[0])
       if int(expe) in range(1000, 999999):
          expe1 = expe / 1000
          expe2 = round(expe1)
          expe3 = f'{expe2} тыс'
       if int(expe) in range(1000000, 999999999):
          expe1 = expe / 1000000
          expe2 = round(expe1)
          expe3 = f'{expe2} млн'
       if int(expe) in range(1000000000, 999999999999):
          expe1 = expe / 1000000000
          expe2 = round(expe1) 
          expe3 = f'{expe2} млрд'
       if int(expe) in range(1000000000000, 999999999999999):
          expe1 = expe / 1000000000000
          expe2 = round(expe1)
          expe3 = f'{expe2} трлн'
       if int(expe) in range(1000000000000000, 999999999999999999):
          expe1 = expe / 1000000000000000
          expe2 = round(expe1)
          expe3 = f'{expe2} квдр'
       if int(expe) in range(1000000000000000000, 999999999999999999999):
          expe1 = expe / 1000000000000000000
          expe2 = round(expe1)
          expe3 = f'{expe2} квнт'
       if int(expe) in range(1000000000000000000000, 999999999999999999999999):
          expe1 = expe / 1000000000000000000000
          expe2 = round(expe1)
          expe3 = f'{expe2} скст'
       if rating >= 999999999999999999999999:
          rating = 999999999999999999999999
          cursor.execute(f'UPDATE users SET rating = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
       else:
        pass
       if int(rating) in range(0, 1000):
          rating3 = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
          rating3 = int(rating3[0])
       if int(rating) in range(1000, 999999):
          rating1 = rating / 1000
          rating2 = round(rating1)
          rating3 = f'{rating2} тыс'
       if int(rating) in range(1000000, 999999999):
          rating1 = rating / 1000000
          rating2 = round(rating1)
          rating3 = f'{rating2} млн'
       if int(rating) in range(1000000000, 999999999999):
          rating1 = rating / 1000000000
          rating2 = round(rating1) 
          rating3 = f'{rating2} млрд'
       if int(rating) in range(1000000000000, 999999999999999):
          rating1 = rating / 1000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} трлн'
       if int(rating) in range(1000000000000000, 999999999999999999):
          rating1 = rating / 1000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квдр'
       if int(rating) in range(1000000000000000000, 999999999999999999999):
          rating1 = rating / 1000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квнт'
       if int(rating) in range(1000000000000000000000, 999999999999999999999999):
          rating1 = rating / 1000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} скст'

       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pets = int(pet1) + int(pet2) + int(pet3) + int(pet4) + int(pet5) + int(pet6) + int(pet7) + int(pet8) + int(pet9) + int(pet11)
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       if pet1 == 1:
          p = "    🐥 Питомец - Цыплёнок\n"
       if pet2 == 1:
          p = "    🐈 Питомец - Кот\n"
       if pet3 == 1:
          p = "    🐕 Питомец - Пёс\n"
       if pet4 == 1:
          p = "    🦜 Питомец - Попугай\n"
       if pet5 == 1:
          p = "    🦄 Питомец - Единорог\n"
       if pet6 == 1:
          p = "    🐒 Питомец - Обезьяна\n"
       if pet7 == 1:
          p = "    🐬 Питомец - Дельфин\n"
       if pet8 == 1:
          p = "    🐅 Питомец - Тигр\n"
       if pet9 == 1:
          p = "    🐉 Питомец - Дракон\n"
       if pet11 == 1:
          p = "    🐰 Питомец - Пасхальный кролик\n"
       if pets == 0:
          p = ""
       
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       farms = farm1 + farm2 + farm3 + farm4 + farm5 
       if farm1 == 1:
          f = "    🎡 Электростанция - Grand Coulee\n"
       if farm2 == 1:
          f = "    🎡 Электростанция - Xiluodu\n"
       if farm3 == 1:
          f = "    🎡 Электростанция - Three Gorges Dam\n"
       if farm4 == 1:
          f = "    🎡 Электростанция - Xiangjiaba\n"
       if farm5 == 1:
          f = "    🎡 Электростанция - Itaipu Dam\n"
       if farms == 0:
          f = ""
       
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])

       cars = int(car1) + int(car2) + int(car3) + int(car4) + int(car5) + int(car6) + int(car7) + int(car8) + int(car9) + int(car10) + int(car12)
       if car1 == 1:
          m1 = "    🚗 Машина - ВАЗ 2107\n"
       if car2 == 1:
          m1 = "    🚗 Машина - Lada Vesta\n"
       if car3 == 1:
          m1 = "    🚗 Машина - Lada XRAY Cross\n"
       if car4 == 1:
          m1 = "    🚗 Машина - Audi Q7\n"
       if car5 == 1:
          m1 = "    🚗 Машина - BMW X6\n"
       if car6 == 1:
          m1 = "    🚗 Машина - Hyundai Solaris\n"
       if car7 == 1:
          m1 = "    🚗 Машина - Toyota Supra\n"
       if car8 == 1:
          m1 = "    🚗 Машина - Lamborghini Veneno\n"
       if car9 == 1:
          m1 = "    🚗 Машина - Bugatti Veyron \n"
       if car10 == 1:
          m1 = "    🚗 Машина - Tesla Roadster\n"
       if car12 == 1:
          m1 = "    🚗 Машина - Сани Деда Мороза \n"
       if cars == 0:
          m1 = ""

       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       farmcoins = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5 
       if farm1 == 1:
          mf = "    🧰 Майнинг-ферма - TI-Miner\n"
       if farm2 == 1:
          mf = "    🧰 Майнинг-ферма - Saturn\n"
       if farm3 == 1:
          mf = "    🧰 Майнинг-ферма - Calisto\n"
       if farm4 == 1:
          mf = "    🧰 Майнинг-ферма - HashMiner\n"
       if farm5 == 1:
          mf = "    🧰 Майнинг-ферма - MegaWatt\n"
       if farmcoins == 0:
          mf = ""
       
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if business1 == 1:
          b = "    🌯 Бизнес - Шаурмечная\n"
       if business2 == 1:
          b = "    🕺 Бизнес - Ночной клуб\n"
       if business3 == 1:
          b = "    🚬 Бизнес - Кальянная\n"
       if business4 == 1:
          b = "    ⛽️ Бизнес - АЗС\n"
       if business5 == 1:
          b = "    🏩 Бизнес - Порностудия\n"
       if business6 == 1:
          b = "    🏢 Бизнес - Маленький офис\n"
       if business7 == 1:
          b = "    🛢 Бизнес - Нефтевышка\n"
       if business8 == 1:
          b = "    👩 Бизнес - Космическое агентство\n"
       if business9 == 1:
          b = "    🚀 Бизнес - Межпланетный экспресс\n"
       if businesses == 0:
          b = ""

       im = pets + cars + farms + farmcoins + businesses
       if im >= 1:
          invent = f"{m1}{p}{f}{mf}{b}"
       if im == 0:
          invent = f"    😔 У вас нету имущества!\n"

       get = cursor.execute("SELECT registr_time FROM users WHERE user_id=?", (message.from_user.id,)).fetchall()
       date_time = datetime.fromisoformat(get[0][0])
       times = date_time.strftime( "%d.%m.%Y %H:%M:%S" ) 
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, ваш профиль: \n 🔎 ID: {uid} \n 💰 Деньги: {balance3}$ \n 🏦 В банке: {bank3}$ \n 👑 Рейтинг: {rating3} \n 🌟 Опыт: {expe3} \n 🥚 Яиц: {egg2} \n 🏋️ Энергия: {energy} \n 💳 S-Coins: {scoin2} \n ✨ Репутация: {rep}\n 👇 Клики: {click} \n 👤 Пол: {gender}\n 💽 Биткоины: {bitcoin3}฿ \n 🔮 Ваш статус: {status} \n 🎲 Всего сыграно игр: {games} \n 📦 Имущество:\n {invent} \n 📅 Дата регистрации: {times}",  parse_mode='html')   
    # top
    if message.text.lower() in ["топ", "Топ"]:
       list = cursor.execute(f"SELECT * FROM users ORDER BY rating DESC").fetchmany(10)
       top_list = []
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       num = 0
       for user in list:
           if user[3] >= 999999999999999999999999:
              c6 = 999999999999999999999999
           else:
              c6 = user[3]
           num += 1
           c = Decimal(c6)
           c2 = '{0:,}'.format(c).replace(',', '.')
           
           if num == 1:
              num1 = "1️⃣"
           if num == 2:
              num1 = "2️⃣"
           if num == 3:
              num1 = "3️⃣"
           if num == 4:
              num1 = "4️⃣"
           if num == 5:
              num1 = "5️⃣"
           if num == 6:
              num1 = "6️⃣"
           if num == 7:
              num1 = "7️⃣"
           if num == 8:
              num1 = "8️⃣"
           if num == 9:
              num1 = "9️⃣"
           if num == 10:
              num1 = "🔟"
           
           if int(user[1]) in range(0, 1000):
              balance3 = user[1]

           if int(user[1]) in range(1000, 999999):
              balance1 = user[1] / 1000
              balance2 = round(balance1)
              balance3 = f'{balance2} тыс'

           if int(user[1]) in range(1000000, 999999999):
              balance1 = user[1] / 1000000
              balance2 = round(balance1)
              balance3 = f'{balance2} млн'

           if int(user[1]) in range(1000000000, 999999999999):
              balance1 = user[1] / 1000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} млрд'

           if int(user[1]) in range(1000000000000, 999999999999999):
              balance1 = user[1] / 1000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} трлн'

           if int(user[1]) in range(1000000000000000, 999999999999999999):
              balance1 = user[1] / 1000000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} квдр'

           if int(user[1]) in range(1000000000000000000, 999999999999999999999):
              balance1 = user[1] / 1000000000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} квнт'

           if int(user[1]) in range(1000000000000000000000, 999999999999999999999999):
              balance1 = user[1] / 1000000000000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} скст'

           top_list.append(f"{num1} {user[19]}  — 👑{c2} | ${balance3}")
       top = "\n".join(top_list)
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, топ 10 игроков бота:\n" + top, parse_mode='html')

    if message.text.lower() in ["топ чатов", "Топ чатов"]: 
       list = cursor.execute(f"SELECT * FROM chats ORDER BY cazna DESC").fetchmany(20)
       top_list = []
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       num = 0
       for user in list:
           if user[1] >= 999999999999999999999999:
              c6 = 999999999999999999999999
           else:
              c6 = user[1]
           num += 1
           c = Decimal(c6)
           c2 = '{0:,}'.format(c).replace(',', '.')
           if num == 1:
              num1 = "1️⃣"
           if num == 2:
              num1 = "2️⃣"
           if num == 3:
              num1 = "3️⃣"
           if num == 4:
              num1 = "4️⃣"
           if num == 5:
              num1 = "5️⃣"
           if num == 6:
              num1 = "6️⃣"
           if num == 7:
              num1 = "7️⃣"
           if num == 8:
              num1 = "8️⃣"
           if num == 9:
              num1 = "9️⃣"
           if num == 10:
              num1 = "🔟"
           if num == 11:
              num1 = "1️⃣1️⃣"
           if num == 12:
              num1 = "1️⃣2️⃣"
           if num == 13:
              num1 = "1️⃣3️⃣"
           if num == 14:
              num1 = "1️⃣4️⃣"
           if num == 15:
              num1 = "1️⃣5️⃣"
           if num == 16:
              num1 = "1️⃣6️⃣"
           if num == 17:
              num1 = "1️⃣7️⃣"
           if num == 18:
              num1 = "1️⃣8️⃣"
           if num == 19:
              num1 = "1️⃣9️⃣"
           if num == 20:
              num1 = "2️⃣0️⃣"
           top_list.append(f"{num1} {user[2]}  — {c2}$")
       top = "\n".join(top_list)
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, топ 20 чатов бота:\n" + top , parse_mode='html')

    if message.text.lower() in ["ежедневный бонус", "Ежедневный бонус"]:         
        msg = message       
        chat_id = message.chat.id      
        user_id = msg.from_user.id       
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)       
        loser = ['😔', '😕', '😣', '😞', '😢']       
        rloser = random.choice(loser)      
        period = 86400       
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()        
        balance = int(balance[0])      
        get = cursor.execute("SELECT last_bonus FROM users WHERE user_id=?", (user_id,)).fetchall()
        last_bonus = f"{int(get[0][0])}"
        bonustime = time.time() - float(last_bonus)
        user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
        user_name = user_name[0]
        money_bonus = random.randint(1000000, 3000000)
        money_bonus2 = '{0:,}'.format(money_bonus).replace(',', '.')
        if balance >= 999999999999999999999999:
           balance = 999999999999999999999999
           cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
           connect.commit()
           balance2 = '{0:,}'.format(balance).replace(',', '.')
        if bonustime > period:
            cursor.execute(f'UPDATE users SET balance = {balance + money_bonus}  WHERE user_id = ?', (user_id,))
            cursor.execute(f'UPDATE users SET last_bonus=? WHERE user_id=?', (time.time(), user_id,))
            connect.commit()  
            await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты получил бонус в размере {str(money_bonus2)}$ {rwin}", parse_mode='html')
        else:
            await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, ты уже получал сегодня бонус! {rloser}", parse_mode='html')

    if message.text.lower() in ["помощь", "Помощь"]:
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       user_id = message.from_user.id
       await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, выберите категорию:\n   1️⃣ Основное\n   2️⃣ Игры\n   3️⃣ Развлекательные\n   4️⃣ Имущество\n\n💬 Так же у нас есть <a href='https://t.me/rave_chatt'>общая беседа</a>\n🆘 По всем вопросам - <a href='tg://user?id=5592294018'>Nexxlf</a>", parse_mode='html', reply_markup=kb.help_menu)

    if message.text.startswith("шар"):
       chat_id = message.chat.id
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       x = [f'я думаю - "да"','мой ответ - "нет"','я думаю - "нет"','мой ответ - "да"','может быть']
       rx = random.choice(x)
       args = message.get_args()
       user_id = message.from_user.id
       await bot.send_message(chat_id, f"🎱 | <a href='tg://user?id={user_id}'>{user_name}</a>, {rx}", parse_mode='html')

    if message.text.startswith("шанс"):
       chat_id = message.chat.id
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       args = message.get_args()
       x = random.randint(0,100)
       user_id = message.from_user.id
       await bot.send_message(chat_id, f"🎰 | <a href='tg://user?id={user_id}'>{user_name}</a>, шанс этого: {x}%", parse_mode='html')

    if message.text.startswith("Шар"):
       chat_id = message.chat.id
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       x = [f'я думаю - "да"','мой ответ - "нет"','я думаю - "нет"','мой ответ - "да"','может быть']
       rx = random.choice(x)
       args = message.get_args()
       await bot.send_message(chat_id, f"🎱 | <a href='tg://user?id={user_id}'>{user_name}</a>, {rx}", parse_mode='html')

    if message.text.startswith("Шанс"):
       chat_id = message.chat.id
       msg = message
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       args = message.get_args()
       x = random.randint(0,100)
       await bot.send_message(chat_id, f"🎰 | <a href='tg://user?id={user_id}'>{user_name}</a>, шанс этого: {x}%", parse_mode='html')

    if message.text.startswith("сменить ник"): 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id
       user_id = message.from_user.id
       name = " ".join(message.text.split()[2:])
       if len(name) <= 20:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно поменяли свое имя на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_name = \"{name}\" WHERE user_id = "{user_id}"')
       else: 
          await bot.send_message(message.chat.id, f"ℹ️️ | <a href='tg://user?id={user_id}'>{user_name}</a> , ваш ник не может быть длинее 20 символов!", parse_mode='html')

    if message.text.startswith("Сменить ник"): 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id
       user_id = message.from_user.id
       name = " ".join(message.text.split()[2:])
       if len(name) <= 20:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно поменяли свое имя на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_name = \"{name}\" WHERE user_id = "{user_id}"')
       else: 
          await bot.send_message(message.chat.id, f"ℹ️️ | <a href='tg://user?id={user_id}'>{user_name}</a> , ваш ник не может быть длинее 20 символов!", parse_mode='html')

###########################################ИГРЫ###########################################
    # casino
    if message.text.startswith("казино"): 
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id

       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rx = random.randint(0,120)
       rand = random.randint(1,4)
       rwin = random.choice(win)
       rloser = random.choice(loser)

       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[1])

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{0:,}'.format(balance).replace(',', '.') 
       period = 5
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return

       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(rx) in range(0,9):
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы проиграли {c2}$ (x0) {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()                            
                if int(rx) in range(10,28):
                   c = Decimal(summ - summ * 0.25)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы проиграли {c2}$ (x0.25) {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()  
                if int(rx) in range(29,50):
                   c = Decimal(summ * 0.5)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы проиграли {c2}$ (x0.5) {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit() 
                if int(rx) in range(51,67):
                   c = Decimal(summ - summ * 0.75)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы проиграли {c2}$ (x0.75) {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()  
                if int(rx) in range(68, 77):
                   c = summ * 1
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, ваши деньги остаются при вас! (x1) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   connect.commit()
                if int(rx) in range(78,88):
                   c = Decimal(summ * 1.25)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x1.25) {rwin}", parse_mode='html')   
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()           
                if int(rx) in range(89,95):
                   c = Decimal(summ * 1.5)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x1.5) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()
                if int(rx) in range(96,105):
                   c = Decimal(summ * 1.75)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x1.75) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()  
                if int(rx) in range(106,114):
                   c = Decimal(summ * 2)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x2) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))                   
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()                 
                if int(rx) in range(115,118):
                   c = Decimal(summ * 3)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x3) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit() 
                if int(rx) == 119:
                   c = Decimal(summ * 5)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x5) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit() 
                if int(rx) == 120:
                   c = Decimal(summ * 10)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x10) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                      
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
           await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')
       
    if message.text.startswith("Казино"):  
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id

       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rx = random.randint(0,120)
       rand = random.randint(1,4)
       rwin = random.choice(win)
       rloser = random.choice(loser)

       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[1])

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{0:,}'.format(balance).replace(',', '.')
       period = 5
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return

       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(rx) in range(0,9):
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы проиграли {c2}$ (x0) {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()                            
                if int(rx) in range(10,28):
                   c = Decimal(summ - summ * 0.25)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы проиграли {c2}$ (x0.25) {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()  
                if int(rx) in range(29,50):
                   c = Decimal(summ * 0.5)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы проиграли {c2}$ (x0.5) {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit() 
                if int(rx) in range(51,67):
                   c = Decimal(summ - summ * 0.75)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы проиграли {c2}$ (x0.75) {rloser}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()  
                if int(rx) in range(68, 77):
                   c = summ * 1
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, ваши деньги остаются при вас! (x1) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   connect.commit()
                if int(rx) in range(78,88):
                   c = Decimal(summ * 1.25)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x1.25) {rwin}", parse_mode='html')   
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()           
                if int(rx) in range(89,95):
                   c = Decimal(summ * 1.5)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x1.5) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()
                if int(rx) in range(96,105):
                   c = Decimal(summ * 1.75)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x1.75) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()  
                if int(rx) in range(106,114):
                   c = Decimal(summ * 2)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x2) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()                 
                if int(rx) in range(115,118):
                   c = Decimal(summ * 3)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x3) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit() 
                if int(rx) == 119:
                   c = Decimal(summ * 5)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x5) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit() 
                if int(rx) == 120:
                   c = Decimal(summ * 10)
                   c2 = round(c)
                   c2 = '{0:,}'.format(c2).replace(',', '.')
                   await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы выиграли {c2}$ (x10) {rwin}", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + c} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                   cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                   connect.commit()
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                      
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
           await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')
    # spin
    if message.text.startswith("спин"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       emoji = ['🖕','🍋','🍒','🥃','💎','🍓', '🖕', '🖕']
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       rwin = random.choice(win)
       re1 = random.choice(emoji)
       re2 =  random.choice(emoji)
       re3 =  random.choice(emoji)

       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[1])

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return

       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if str(re3) == str(re2) == str(re1):
                   if str(re1) == '🖕':  #проигрыш
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,)) 
                               connect.commit() 
                               return
                   if str(re2) == '🖕':
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,)) 
                               connect.commit() 
                               return
                    
                   if str(re3) == '🖕':       
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,)) 
                               connect.commit() 
                               return

                   else:       
                               c = Decimal(summ * 50)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| ДЖЕКПОТ! Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 50)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re1) == '🖕':  #проигрыш
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re2) == '🖕': 
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit()
                               return
                  
                if str(re3) == '🖕':                                
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               сursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               connect.commit() 
                               return
 
                if str(re1) == '🍋': #выигрыш 1
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍋':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
                if str(re3) == '🍋':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re1) == '🍒': #выигрыш 2
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍒':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re3) == '🍒':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re1) == '🥃': #выигрыш 3
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
                if str(re2) == '🥃':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
  
                if str(re3) == '🥃':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.') 
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re1) == '💎': #выигрыш 4
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re2) == '💎':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               connect.commit() 
                               return
                if str(re3) == '💎':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re1) == '🍓': #выигрыш 5
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍓':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
                if str(re3) == '🍓':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.') 
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                    
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
           await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')

    if message.text.startswith("Спин"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       emoji = ['🖕','🍋','🍒','🥃','💎','🍓', '🖕', '🖕']
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       rwin = random.choice(win)
       re1 = random.choice(emoji)
       re2 =  random.choice(emoji)
       re3 =  random.choice(emoji)

       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[1])

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return

       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if str(re3) == str(re2) == str(re1):
                   if str(re1) == '🖕':  #проигрыш
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
                   if str(re2) == '🖕':
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
                    
                   if str(re3) == '🖕':       
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,)) 
                               connect.commit() 
                               return

                   else:       
                               c = Decimal(summ * 50)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| ДЖЕКПОТ! Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 50)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,)) 
                               connect.commit() 
                               return

                if str(re1) == '🖕':  #проигрыш
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re2) == '🖕': 
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit()
                               return
                  
                if str(re3) == '🖕':                                
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}|  Удача не на твоей стороне. Выигрыш: 0$ {rloser}", parse_mode='html')
                               сursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               connect.commit() 
                               return
 
                if str(re1) == '🍋': #выигрыш 1
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,)) 
                               connect.commit() 
                               return

                if str(re2) == '🍋':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
                if str(re3) == '🍋':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re1) == '🍒': #выигрыш 2
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍒':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re3) == '🍒':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re1) == '🥃': #выигрыш 3
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
                if str(re2) == '🥃':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.') 
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
  
                if str(re3) == '🥃':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re1) == '💎': #выигрыш 4
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re2) == '💎':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
                if str(re3) == '💎':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.') 
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re1) == '🍓': #выигрыш 5
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return

                if str(re2) == '🍓':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
                if str(re3) == '🍓':
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a> \n|{re1}|{re2}|{re3}| Выигрыш: {c2}$ {rwin}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,)) 
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit() 
                               return
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                    
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
           await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')

    if message.text.startswith("Кубик"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       cub = int(msg.text.split()[1])
       summ = int(msg.text.split()[2])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return

       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if cub in [1, 2, 3, 4, 5, 6]:
                   dice_message = await bot.send_dice(chat_id)
                   value = dice_message.dice.value
                   if value == cub:
                      c = Decimal(summ * 3)
                      c2 = round(c)
                      c2 = '{0:,}'.format(c2).replace(',', '.')
                      await message.answer(f"Поздравляю! Вы угадали число. Ваш выигрыш составил - {c2}$ {rwin}", parse_mode='html')
                      cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 3)} WHERE user_id = "{user_id}"')
                      cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                      cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                      cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                      connect.commit() 
                      return
                   else:
                      c = Decimal(summ)
                      c2 = round(c)
                      c2 = '{0:,}'.format(c2).replace(',', '.')
                      await message.answer(f"К сожалению вы не угадали число. Ваш выигрыш - 0$ {rloser}", parse_mode='html')
                      cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                      cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                      cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                      cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                      connect.commit()  
                      return 
                else:
                   await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, выберите число от 1 до 6! {rloser}", parse_mode='html')                                 
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
           await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')
           return

    if message.text.startswith("кубик"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       cub = int(msg.text.split()[1])
       summ = int(msg.text.split()[2])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return

       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if cub in [1, 2, 3, 4, 5, 6]:
                   dice_message = await bot.send_dice(chat_id)
                   value = dice_message.dice.value
                   if value == cub:
                      c = Decimal(summ * 3)
                      c2 = round(c)
                      c2 = '{0:,}'.format(c2).replace(',', '.')
                      await message.answer(f"Поздравляю! Вы угадали число. Ваш выигрыш составил - {c2}$ {rwin}", parse_mode='html')
                      cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 3)} WHERE user_id = "{user_id}"')
                      cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                      cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                      cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                      connect.commit() 
                      return
                   else:
                      c = Decimal(summ)
                      c2 = round(c)
                      c2 = '{0:,}'.format(c2).replace(',', '.')
                      await message.answer(f"К сожалению вы не угадали число. Ваш выигрыш - 0$ {rloser}", parse_mode='html')
                      cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                      cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                      cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                      cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                      connect.commit()  
                      return 
                else:
                   await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, выберите число от 1 до 6! {rloser}", parse_mode='html')                                 
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                       
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
           await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')
           return

    if message.text.startswith("гонки"):
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])

       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])

       сars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car12 + car10

       msg = message
       summ = int(msg.text.split()[1])
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
       game = int(game[0])
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       coff = random.randint(1,3)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return

       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(сars) >= 1:
                   if cart >= 1:
                      if coff == 1:
                         c = Decimal(summ * 1.45)
                         c2 = round(c)
                         c2 = '{0:,}'.format(c2).replace(',', '.')
                         await bot.send_message(chat_id, f"🎉 | <a href='tg://user?id={user_id}'>{user_name}</a>, Вы победили в гонке! Ваш выигрыш: {c2} {rwin}", parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET cart = {cart - 20} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                         cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                         cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                         cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                         connect.commit() 
                         return 
                      else:
                         c = Decimal(summ)
                         c2 = round(c)
                         c2 = '{0:,}'.format(c2).replace(',', '.')
                         await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, Вы проиграли в гонке! Ваш проигрыш: {c2} {rloser}", parse_mode='html')
                         cursor.execute(f'UPDATE users SET cart = {cart - 20} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                         cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                         cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                         cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"') 
                         connect.commit()
                   if cart == 0:
                      await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас закончилось топливо! {rloser}", parse_mode='html')
                if int(сars) == 0:
                   await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету машины! {rloser}", parse_mode='html') 
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                  
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
        await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')
       
    if message.text.startswith("Гонки"):  
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])

       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])

       сars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car12 + car10

       msg = message
       summ = int(msg.text.split()[1])
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[1])
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
       game = int(game[0])
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       coff = random.randint(1,3)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return

       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(сars) >= 1:
                   if cart >= 1: 
                      if coff == 1:
                         c = Decimal(summ * 1.45)
                         c2 = round(c)
                         c2 = '{0:,}'.format(c2).replace(',', '.')
                         await bot.send_message(chat_id, f"🎉 | <a href='tg://user?id={user_id}'>{user_name}</a>, Вы победили в гонке! Ваш выигрыш: {c2} {rwin}", parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET cart = {cart - 20} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                         cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                         cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                         cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                         connect.commit() 
                         return 
                      else:
                         c = Decimal(summ)
                         c2 = round(c)
                         c2 = '{0:,}'.format(c2).replace(',', '.')
                         await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, Вы проиграли в гонке! Ваш проигрыш: {c2} {rloser}", parse_mode='html')
                         cursor.execute(f'UPDATE users SET cart = {cart - 20} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                         cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                         cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                         cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                         cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"') 
                         connect.commit()
                   if cart == 0:
                      await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас закончилось топливо! {rloser}", parse_mode='html')
                if int(сars) == 0:
                   await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету машины! {rloser}", parse_mode='html') 
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                  
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
        await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')

       
    if message.text.lower() in ["заправка", "Заправка"]:
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])
       сars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10 + car12
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       if int(сars) >= 1:
          await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, курс топлива: 2.000$ за 1% \n🛠 Чтобы заправить машину , введите: Заправить машину", parse_mode='html') 
       if int(сars) == 0:
          await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету машины! {rloser}", parse_mode='html') 
            
    if message.text.lower() in ["заправить машину", "Заправить машину"]:
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car12 + car10
       c = Decimal((100 - cart) * 2000)
       c2 = round(c)
       c2 = '{0:,}'.format(c2).replace(',', '.')
       c3 = 100 - cart
       c4 = (100 - cart) * 2000
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{0:,}'.format(balance).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(cars) == 0:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету автомобиля! {rloser}", parse_mode='html') 
          return
       await asyncio.sleep(1)
       if int(car1) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно заправили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html') 
       if int(car2) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно заправили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html')  
       if int(car3) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно заправили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html')  
       if int(car4) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно заправили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html')  
       if int(car5) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно заправили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html')  
       if int(car6) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно заправили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html')  
       if int(car7) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно заправили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html')  
       if int(car8) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно заправили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html')  
       if int(car9) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно заправили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html')  
       if int(car10) == 1:
          if cart < 100:
             if c <= balance:
                await bot.send_message(chat_id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно зарядили свой автомобиль за {c2}!", parse_mode='html') 
                cursor.execute(f'UPDATE users SET balance = {balance - c4} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {cart + c3} WHERE user_id = "{user_id}"')
                return
             if c >= balance:
                await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html') 
          if cart == 100:
             await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашей машины полный бак! {rloser}", parse_mode='html')  


    if message.text.startswith("бой"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10 + pet11

       summ = int(msg.text.split()[1])
       period = 5
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
       game = int(game[0])
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       rhp = random.randint(10, 20)
       reat = random.randint(10, 20)
       rmood = random.randint(10, 20)
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       coff = random.randint(1,3)
       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(pets) >= 1:
                   if pet_hp >= 20:
                      if pet_eat >= 20:
                         if pet_mood >= 20:  
                            if coff == 1:
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"🎉 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец победил в сражении! Ваш выигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               connect.commit() 
                               return 
                            else:
                               c = Decimal(summ)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец проиграл в сражении! Ваш проигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit()
                         if pet_mood == 0:
                            await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашего питомца нету настроения! {rloser}", parse_mode='html')
                      if pet_eat == 0:
                         await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец голоден! {rloser}", parse_mode='html')
                   if pet_hp == 0:
                      await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашего питомца недостаточно здоровья! {rloser}", parse_mode='html')
                if int(pets) == 0:
                   await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету питомца! {rloser}", parse_mode='html') 
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                    
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
        await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')

    if message.text.startswith("Бой"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10 + pet11

       summ = int(msg.text.split()[1])
       period = 5
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       games = cursor.execute("SELECT games from users where user_id = ?", (message.from_user.id,)).fetchone()
       games = round(int(games[0]))
       game = cursor.execute("SELECT game from users where user_id = ?",(message.from_user.id,)).fetchone()
       game = int(game[0])
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       rhp = random.randint(10, 20)
       reat = random.randint(10, 20)
       rmood = random.randint(10, 20)
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       coff = random.randint(1,3)
       period1 = 5
       get1 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get1[0]))
       stavkatime1 = data_bank + period1

       if time.time() >= stavkatime1:
          pass
       else:
          return

       period2 = 5
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          return

       period3 = 5
       get3 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get3[0]))
       stavkatime3 = data_bitcoin + period3

       if time.time() >= stavkatime3:
          pass
       else:
          return
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(pets) >= 1:
                   if pet_hp >= 20:
                      if pet_eat >= 20:
                         if pet_mood >= 20:  
                            if coff == 1:
                               c = Decimal(summ * 1.45)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"🎉 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец победил в сражении! Ваш выигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ + (summ * 1.45)} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               connect.commit() 
                               return 
                            else:
                               c = Decimal(summ)
                               c2 = round(c)
                               c2 = '{0:,}'.format(c2).replace(',', '.')
                               await bot.send_message(chat_id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец проиграл в сражении! Ваш проигрыш: {c2}\n❤️ | ХП: -{rhp}\n🍗 | Сытость: -{reat}\n☀️ | Настроение: -{rmood}", parse_mode='html')
                               cursor.execute(f'UPDATE users SET pet_hp = {pet_hp - rhp} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_eat = {pet_eat - reat} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET pet_mood = {pet_mood - rmood} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE users SET game = {game - 1} WHERE user_id = "{user_id}"') 
                               cursor.execute(f'UPDATE users SET games = {games + 1} WHERE user_id = "{user_id}"')
                               cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                               cursor.execute(f'UPDATE users SET last_stavka=? WHERE user_id=?', (time.time(), user_id,))
                               connect.commit()
                         if pet_mood == 0:
                            await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашего питомца нету настроения! {rloser}", parse_mode='html')
                      if pet_eat == 0:
                         await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец голоден! {rloser}", parse_mode='html')
                   if pet_hp == 0:
                      await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вашего питомца недостаточно здоровья! {rloser}", parse_mode='html')
                if int(pets) == 0:
                   await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету питомца! {rloser}", parse_mode='html') 
             elif summ <= 0:
                  await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя ставить отрицательное число! {rloser}", parse_mode='html')                                                    
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
       else:
        await bot.send_message(chat_id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно каждые 5 секунд! {rloser}", parse_mode='html')

###########################################ЭКОНОМИКА###########################################
    # perevod        
    if message.text.startswith("дать"):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       ruser_name = ruser_name[0] 
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = int(msg.text.split()[1])
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       admin_id = 5592294018

       if not message.reply_to_message:
          await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'ℹ | Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period = 10
       get = cursor.execute("SELECT datatrans FROM users WHERE user_id = ?", (reply_user_id,)).fetchone()
       datatrans = round(int(get[0]))
       stavkatime = datatrans + period

       if time.time() >= stavkatime:
          pass
       else:
          return
      
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (user_id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if perevod > 0:
          if balance >= perevod: 
             if user_status[0] == "Admin":
                await message.reply_to_message.reply(f"💸 | Вы передали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{ruser_name}</a> {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), reply_user_id,))
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), user_id,))
                connect.commit()  
                await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a> передал {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{ruser_name}</a> {rwin}", parse_mode='html')
             else:
                await message.reply_to_message.reply(f"💸 | Вы передали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{ruser_name}</a> {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET limit_trans = {limit_trans + perevod} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), reply_user_id,))
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), user_id,))
                connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"') 
             connect.commit()

       if perevod <= 0:
          await message.reply( f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя перевести отрицательное число! {rloser}", parse_mode='html') 
          cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"') 
          connect.commit()

    if message.text.startswith("Дать"):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       ruser_name = ruser_name[0] 
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = int(msg.text.split()[1])
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))

       if not message.reply_to_message:
          await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'ℹ | Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       
       period = 10
       get = cursor.execute("SELECT datatrans FROM users WHERE user_id = ?", (reply_user_id,)).fetchone()
       datatrans = round(int(get[0]))
       stavkatime = datatrans + period

       if time.time() >= stavkatime:
          pass
       else:
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (user_id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return
       
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       admin_id = 5592294018
       if perevod > 0:
          if balance >= perevod: 
             if user_status[0] == "Admin":
                await message.reply_to_message.reply(f"💸 | Вы передали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{ruser_name}</a> {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), reply_user_id,))
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), user_id,))
                connect.commit()  
                await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a> передал {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{ruser_name}</a> {rwin}", parse_mode='html')
             else:
                await message.reply_to_message.reply(f"💸 | Вы передали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{ruser_name}</a> {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), reply_user_id,))
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), user_id,))
                connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"') 
             connect.commit()

       if perevod <= 0:
          await message.reply( f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя перевести отрицательное число! {rloser}", parse_mode='html') 
          
    if message.text.startswith("передать"): 
       msg = message
       user_id = cursor.execute("SELECT id from users where user_id = ?",(message.from_user.id,)).fetchone()
       chat_id = message.chat.id
       user_id = int(user_id[0])
       idtg = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_id = int(msg.text.split()[2])
       reply_idtg = cursor.execute("SELECT user_id from users where id = ?",(reply_user_id,)).fetchone()
       reply_idtg = int(reply_idtg[0])
       ruser_name = cursor.execute("SELECT user_name from users where id = ?",(reply_user_id,)).fetchone()
       ruser_name = ruser_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       admin_id = 5592294018
       perevod = int(msg.text.split()[1])
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where id = ?", (reply_user_id,)).fetchone()
       balance2 = round(balance2[0])
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       
       if reply_user_id == user_id:
          await bot.send_message(chat_id, f'ℹ | Вы не можете передать деньги самому себе! {rloser}', parse_mode='html')
          return

       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       
       period = 10
       get = cursor.execute("SELECT datatrans FROM users WHERE user_id = ?", (reply_idtg,)).fetchone()
       datatrans = round(int(get[0]))
       stavkatime = datatrans + period

       if time.time() >= stavkatime:
          pass
       else:
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return
    
       if perevod > 0:
          if balance >= perevod: 
             if user_status[0] == "Admin":
                await bot.send_message(message.chat.id, f"💸 | Вы передали {perevod2}$ игроку <a href='tg://user?id={reply_idtg}'>{ruser_name}</a> {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{idtg}"') 
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_idtg}"')
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), reply_idtg,))
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), idtg,))
                connect.commit()  
                await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={idtg}'>{user_name}</a> передал {perevod2}$ игроку <a href='tg://user?id={reply_idtg}'>{ruser_name}</a> {rwin}", parse_mode='html')
             else:
                await bot.send_message(message.chat.id, f"💸 | Вы передали {perevod2}$ игроку <a href='tg://user?id={reply_idtg}'>{ruser_name}</a> {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{idtg}"') 
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_idtg}"')
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), reply_idtg,))
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), idtg,))
                connect.commit()     
   
          elif int(balance) <= int(perevod):
             await message.reply( f"💰 | <a href='tg://user?id={idtg}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
             connect.commit()

       if perevod <= 0:
          await message.reply( f"ℹ | <a href='tg://user?id={idtg}'>{user_name}</a>, нельзя перевести отрицательное число! {rloser}", parse_mode='html')  
          cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"') 
          connect.commit()

    if message.text.startswith("Передать"): 
       msg = message
       user_id = cursor.execute("SELECT id from users where user_id = ?",(message.from_user.id,)).fetchone()
       chat_id = message.chat.id
       user_id = int(user_id[0])
       idtg = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_id = int(msg.text.split()[2])
       reply_idtg = cursor.execute("SELECT user_id from users where id = ?",(reply_user_id,)).fetchone()
       reply_idtg = int(reply_idtg[0])
       ruser_name = cursor.execute("SELECT user_name from users where id = ?",(reply_user_id,)).fetchone()
       ruser_name = ruser_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = int(msg.text.split()[1])
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       admin_id = 5592294018

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where id = ?", (reply_user_id,)).fetchone()
       balance2 = round(balance2[0])
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       
       if reply_user_id == user_id:
          await bot.send_message(chat_id, f'ℹ | Вы не можете передать деньги самому себе! {rloser}', parse_mode='html')
          return

       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period = 10
       get = cursor.execute("SELECT datatrans FROM users WHERE user_id = ?", (reply_idtg,)).fetchone()
       datatrans = round(int(get[0]))
       stavkatime = datatrans + period

       if time.time() >= stavkatime:
          pass
       else:
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if perevod > 0:
          if balance >= perevod: 
             if user_status[0] == "Admin":
                await bot.send_message(message.chat.id, f"💸 | Вы передали {perevod2}$ игроку <a href='tg://user?id={reply_idtg}'>{ruser_name}</a> {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{idtg}"') 
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_idtg}"')
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), reply_idtg,))
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), idtg,))    
                connect.commit()  
                await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={idtg}'>{user_name}</a> передал {perevod2}$ игроку <a href='tg://user?id={reply_idtg}'>{ruser_name}</a> {rwin}", parse_mode='html')
             else:
                await bot.send_message(message.chat.id, f"💸 | Вы передали {perevod2}$ игроку <a href='tg://user?id={reply_idtg}'>{ruser_name}</a> {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{idtg}"')  
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_idtg}"')
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), reply_idtg,))
                cursor.execute(f'UPDATE users SET datatrans=? WHERE user_id=?', (time.time(), idtg,))
                connect.commit()     
   
          elif int(balance) <= int(perevod):
             await message.reply( f"💰 | <a href='tg://user?id={idtg}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"')
             connect.commit()

       if perevod <= 0:
          await message.reply( f"ℹ | <a href='tg://user?id={idtg}'>{user_name}</a>, нельзя перевести отрицательное число! {rloser}", parse_mode='html')  
          cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{user_id}"') 
          connect.commit()

    # bank
    if message.text.startswith("банк положить"): 
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]

       bank_p = int(msg.text.split()[2])

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{0:,}'.format(bank_p).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       
       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if bank_p > 0:
          if balance >= bank_p:  
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно положили в банк {bank2}$ {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET data_bank=? WHERE user_id=?', (time.time(), message.from_user.id,))
             connect.commit()    
   
          elif int(balance) < int(bank_p):
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')

       if bank_p <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя положить в банк отрицательное число! {rloser}", parse_mode='html')  

    if message.text.startswith("банк снять"):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]

       bank_s = int(msg.text.split()[2])

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{0:,}'.format(bank_s).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if bank_s > 0:
          if bank >= bank_s:  
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли с банковского счёта {bank2}$ {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET data_bank=? WHERE user_id=?', (time.time(), message.from_user.id,))
             connect.commit()    
   
          elif int(bank) < int(bank_s):
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств на банковском счету! {rloser}", parse_mode='html')

       if bank_s <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя снять с банка отрицательное число! {rloser}", parse_mode='html')  

    if message.text.startswith("Банк положить"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]

       bank_p = int(msg.text.split()[2])

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{0:,}'.format(bank_p).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if bank_p > 0:
          if balance >= bank_p:  

             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно положили в банк {bank2}$ {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET data_bank=? WHERE user_id=?', (time.time(), message.from_user.id,))
             connect.commit()    
   
          elif int(balance) < int(bank_p):
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')

       if bank_p <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя положить в банк отрицательное число! {rloser}", parse_mode='html')  

    if message.text.startswith("Банк снять"): 
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]

       bank_s = int(msg.text.split()[2])

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{0:,}'.format(bank_s).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       
       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if bank_s > 0:
          if bank >= bank_s: 
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли с банковского счёта {bank2}$ {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET data_bank=? WHERE user_id=?', (time.time(), message.from_user.id,))
             connect.commit()    
   
          elif int(bank) < int(bank_s):
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств на банковском счету! {rloser}", parse_mode='html')

       if bank_s <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя снять с банка отрицательное число! {rloser}", parse_mode='html')  

    # rating
    if message.text.startswith("рейтинг купить"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[2])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       rating2 = '{0:,}'.format(summ).replace(',', '.')
       c = summ * 150000000
       c2 = '{0:,}'.format(c).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if summ > 0:
        if int(balance) >= int(summ * 150000000):
          await asyncio.sleep(1)
          await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы повысили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET data_rating=? WHERE user_id=?', (time.time(), message.from_user.id,))
          connect.commit()

 
        if int(balance) < int(summ * 150000000):
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')

       if summ <= 0:
         await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')
    
    if message.text.startswith("рейтинг продать"): 
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[2])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * 100000000
       c2 = '{0:,}'.format(c).replace(',', '.')
       rating2 = '{0:,}'.format(summ).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if summ > 0:
        if int(rating) >= int(summ):
          await asyncio.sleep(1)
          await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы понизили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET data_rating=? WHERE user_id=?', (time.time(), message.from_user.id,))
          connect.commit()

        if int(rating) < int(summ):
          await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас недостаточно рейтинга для его продажи! {rloser}", parse_mode='html')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя продать отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("Рейтинг купить"): 
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[2])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       rating2 = '{0:,}'.format(summ).replace(',', '.')
       c = summ * 150000000
       c2 = '{0:,}'.format(c).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if summ > 0:
        if int(balance) >= int(summ * 150000000):
          await asyncio.sleep(1)
          await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы повысили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET data_rating=? WHERE user_id=?', (time.time(), message.from_user.id,))
          connect.commit()

 
        if int(balance) < int(summ * 150000000):
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')

       if summ <= 0:
         await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')
    
    if message.text.startswith("Рейтинг продать"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       summ = int(msg.text.split()[2])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * 100000000
       c2 = '{0:,}'.format(c).replace(',', '.')
       rating2 = '{0:,}'.format(summ).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if summ > 0:
        if int(rating) >= int(summ):
          await asyncio.sleep(1)
          await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы понизили количество вашего рейтинга на {rating2}👑 за {c2}$! {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET data_rating=? WHERE user_id=?', (time.time(), message.from_user.id,))
          connect.commit()

        if int(rating) < int(summ):
          await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас недостаточно рейтинга для его продажи! {rloser}", parse_mode='html')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя продать отрицательное число! {rloser}", parse_mode='html')

    if message.text.lower() in ["Биткоин курс", "биткоин курс"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       chat_id = message.chat.id
       j = requests.get(url)
       data = json.loads(j.text)
       get = round(data['result']['Ask'])
       price = '{0:,}'.format(get).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, на данный момент курс 1 BTC составляет - {price}$", parse_mode='html') 
          
    if message.text.startswith("биткоин купить"): 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       j = requests.get(url)
       data = json.loads(j.text)
       price = round(data['result']['Ask'])
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?", (message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * price
       c2 = '{0:,}'.format(c).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       
       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if summ > 0:
          if balance >= c:
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} BTC за {c2}$! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET data_bitcoin=? WHERE user_id=?', (time.time(), message.from_user.id,))
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостачно средств! {rloser}", parse_mode='html')
       if summ <= 0:
          await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("биткоин продать"): 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       summ = int(msg.text.split()[2])
       j = requests.get(url)
       data = json.loads(j.text)
       price = round(data['result']['Ask'])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?", (message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * price
       c2 = '{0:,}'.format(c).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
      
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if summ > 0:
          if bitcoin >= summ:
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ2} BTC за {c2}$! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin - summ} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET data_bitcoin=? WHERE user_id=?', (time.time(), message.from_user.id,))
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостачно BTC! {rloser}", parse_mode='html')
       if summ <= 0:
          await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, нельзя продать отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("Биткоин купить"): 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       j = requests.get(url)
       data = json.loads(j.text)
       price = round(data['result']['Ask'])
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?", (message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * price
       c2 = '{0:,}'.format(c).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       
       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if summ > 0:
          if balance >= c:
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} BTC за {c2}$! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET data_bitcoin=? WHERE user_id=?', (time.time(), message.from_user.id,))
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостачно средств! {rloser}", parse_mode='html')
       if summ <= 0:
          await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("Биткоин продать"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       summ = int(msg.text.split()[2])
       j = requests.get(url)
       data = json.loads(j.text)
       price = round(data['result']['Ask'])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?", (message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       if balance >= 999999999999999999999999:
          balance = 999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       c = summ * price
       c2 = '{0:,}'.format(c).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return

       period1 = 25
       get1 = cursor.execute("SELECT data_bitcoin FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bitcoin = round(int(get1[0]))
       stavkatime1 = data_bitcoin + period1

       if time.time() >= stavkatime1:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period2 = 25
       get2 = cursor.execute("SELECT data_rating FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_rating = round(int(get2[0]))
       stavkatime2 = data_rating + period2

       if time.time() >= stavkatime2:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return

       period3 = 25
       get3 = cursor.execute("SELECT data_bank FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       data_bank = round(int(get3[0]))
       stavkatime3 = data_bank + period3

       if time.time() >= stavkatime3:
          pass
       else:
          await bot.send_message(chat_id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, совершать транзакции можно лишь раз в 25 секунд! {rloser}", parse_mode='html') 
          return
       
       period6 = 5
       get6 = cursor.execute("SELECT last_stavka FROM users WHERE user_id = ?", (message.from_user.id,)).fetchone()
       datatrans6 = round(int(get6[0]))
       stavkatime6 = datatrans6 + period6

       if time.time() >= stavkatime6:
          pass
       else:
          return

       if summ > 0:
          if bitcoin >= summ:
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ2} BTC за {c2}$! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin - summ} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET data_bitcoin=? WHERE user_id=?', (time.time(), message.from_user.id,))
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостачно BTC! {rloser}", parse_mode='html')
       if summ <= 0:
          await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, нельзя продать отрицательное число! {rloser}", parse_mode='html')


###########################################АВТОМОБИЛИ###########################################
    if message.text.lower() in ["машины", "Машины"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id
       user_id = message.from_user.id
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, доступные машины:\n🚗 1. ВАЗ 2107 - 5.000.000.000$\n🚗 2. Lada Vesta - 50.000.000.000$\n🚗 3. Lada XRAY Cross - 100.000.000.000$\n🚗 4. Audi Q7 - 500.000.000.000$\n🚗 5. BMW X6 - 750.000.000.000$\n🚗 6. Hyundai Solaris - 1.000.000.000.000$\n🚗 7. Toyota Supra - 1.500.000.000.000$\n🚗 8. Lamborghini Veneno - 3.000.000.000.000$\n🚗 9. Bugatti Veyron - 10.000.000.000.000$ \n🚗 10. Tesla Roadster - 50.000.000.000.000$ \n\n🛒 Для покупки машины введите: Купить машину [номер]\nℹ Для просмотра информации о своей машине: Моя машина", parse_mode='html')

    if message.text.lower() in ["купить машину 1", "Купить машину 1"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 5000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car1 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили ВАЗ 2107 за 5.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car1 = {car1 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car1 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить машину 2", "Купить машину 2"]:  
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 50000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car2 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Lada Vesta за 50.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car2 = {car2 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car2 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')   

    if message.text.lower() in ["купить машину 3", "Купить машину 3"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 100000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car3 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Lada XRAY Cross за 100.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car3 = {car3 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car3 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')            

    if message.text.lower() in ["купить машину 4", "Купить машину 4"]:  
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 500000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car4 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Audi Q7 за 500.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car4 = {car4 + c} WHERE user_id = "{user_id}"')
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"')  
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car4 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')

    if message.text.lower() in ["купить машину 5", "Купить машину 5"]:  
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 750000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car5 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили BMW X6 за 750.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car5 = {car5 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car5 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')              

    if message.text.lower() in ["купить машину 6", "Купить машину 6"]:  
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1000000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car6 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Hyundai Solaris за 1.000.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car6 = {car6 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car6 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')

    if message.text.lower() in ["купить машину 7", "Купить машину 7"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1500000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car7 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Toyota Supra за 1.500.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car7 = {car7 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car7 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')

    if message.text.lower() in ["купить машину 8", "Купить машину 8"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 3000000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car8 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Lamborghini Veneno за 3.000.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car8 = {car8 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car8 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')    

    if message.text.lower() in ["купить машину 9", "Купить машину 9"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 10000000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car9 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Bugatti Veyron за 10.000.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car9 = {car9 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car9 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')    

    if message.text.lower() in ["купить машину 10", "Купить машину 10"]:    
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 50000000000000
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if cars == 0:
          if car10 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🚗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Tesla Roadster за 50.000.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET car10 = {car10 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if car10 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
             return
       if cars == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть автомобиль! {rloser}", parse_mode='html')    
 
    if message.text.lower() in ["купить машину supra", "Купить машину Supra"]: 
       chat_id = message.chat.id  
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car11 = cursor.execute("SELECT car11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car11 = int(car11[0])
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       c = 1
       if car11 == 0:
          if int(balance) >= int(summ):
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Supra Legend за 1$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET car11 = {car11 + c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          else:
             await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             return
       if car11 == 1:
          await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный автомобиль! {rloser}", parse_mode='html')     
          return

    if message.text.lower() in ["Моя машина", "моя машина"]:  
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])
       user_id = message.from_user.id
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car12 + car10
       if cars == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету машины! {rloser}", parse_mode='html')
       if car1 == 1:
          photo = open('car1.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине ВАЗ 2107\n⛽️ | Макс.Скорость - 152 км/ч\n🐎 | Лошадиных сил - 140 л.с\n🛢 | Объем топливного бака - 39л\n🔋 | Топливо: {cart}%", parse_mode='html')
       if car2 == 1:
          photo = open('car2.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине Lada Vesta\n⛽️ | Макс.Скорость - 175 км/ч\n🐎 | Лошадиных сил - 106 л.с\n🛢 | Объем топливного бака - 55л\n🔋 | Топливо: {cart}%", parse_mode='html')
       if car3 == 1:
          photo = open('car3.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине Lada XRAY Cross\n⛽️ | Макс.Скорость - 162 км/ч\n🐎 | Лошадиных сил - 122 л.с\n🛢 | Объем топливного бака - 50л\n🔋 | Топливо: {cart}%", parse_mode='html')
       if car4 == 1:
          photo = open('car4.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине Audi Q7\n⛽️ | Макс.Скорость - 225 км/ч\n🐎 | Лошадиных сил - 249 л.с\n🛢 | Объем топливного бака - 70л\n🔋 | Топливо: {cart}%", parse_mode='html')
       if car5 == 1:
          photo = open('car5.jpeg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине BMW X6\n⛽️ | Макс.Скорость - 250 км/ч\n🐎 | Лошадиных сил - 400 л.с\n🛢 | Объем топливного бака - 85л\n🔋 | Топливо: {cart}%", parse_mode='html')
       if car6 == 1:
          photo = open('car6.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине Hyundai Solaris\n⛽️ | Макс.Скорость - 185 км/ч\n🐎 | Лошадиных сил - 100 л.с\n🛢 | Объем топливного бака - 50л\n🔋 | Топливо: {cart}%", parse_mode='html')
       if car7 == 1:
          photo = open('car7.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине Toyota Supra\n⛽️ | Макс.Скорость - 250 км/ч\n🐎 | Лошадиных сил - 340 л.с\n🛢 | Объем топливного бака - 50л\n🔋 | Топливо: {cart}%", parse_mode='html')
       if car8 == 1:
          photo = open('car8.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине Lamborghini Veneno\n⛽️ | Макс.Скорость - 357 км/ч\n🐎 | Лошадиных сил - 750 л.с\n🛢 |Объем топливного бака - 90л\n🔋 | Топливо: {cart}%", parse_mode='html')
       if car9 == 1:
          photo = open('car9.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине Bugatti Veyron\n⛽️ | Макс.Скорость - 407 км/ч\n🐎 | Лошадиных сил - 1001 л.с\n🛢 | Объем топливного бака - 100л\n🔋 | Топливо: {cart}%", parse_mode='html')
       if car10 == 1:
          photo = open('car10.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине Tesla Roadster\n⛽️ | Макс.Скорость - 400 км/ч\n🐎 | Лошадиных сил - 700 л.с\n🛢 | Объем топливного бака - ---\n🔋 | Заряд: {cart}%", parse_mode='html')
       if car12 == 1:
          photo = open('car12.png', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"<a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей машине Сани Деда Мороза\n⛽️ | Макс.Скорость - 9999 км/ч\n🐎 | Лошадиных сил - 9999 л.с\n🛢 | Объем топливного бака - 9999л\n🔋 | Топливо: {cart}%", parse_mode='html')

    if message.text.lower() in ["продать машину", "Продать машину"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       car1 = cursor.execute("SELECT car1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car1 = int(car1[0])
       car2 = cursor.execute("SELECT car2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car2 = int(car2[0])
       car3 = cursor.execute("SELECT car3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car3 = int(car3[0])
       car4 = cursor.execute("SELECT car4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car4 = int(car4[0])
       car5 = cursor.execute("SELECT car5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car5 = int(car5[0])
       car6 = cursor.execute("SELECT car6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car6 = int(car6[0])
       car7 = cursor.execute("SELECT car7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car7 = int(car7[0])
       car8 = cursor.execute("SELECT car8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car8 = int(car8[0])
       car9 = cursor.execute("SELECT car9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car9 = int(car9[0])
       car10 = cursor.execute("SELECT car10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car10 = int(car10[0])
       car12 = cursor.execute("SELECT car12 from users where user_id = ?",(message.from_user.id,)).fetchone()
       car12 = int(car12[0])
       cart = cursor.execute("SELECT cart from users where user_id = ?",(message.from_user.id,)).fetchone()
       cart = int(cart[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       cars = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car12 + car10
       c = 1
       await asyncio.sleep(1)
       if cars == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету машины! {rloser}", parse_mode='html')
       if car1 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 3.750.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 3750000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car1 = {car1 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if car2 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 37.500.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 37500000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car2 = {car2 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if car3 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 75.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 75000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car3 = {car3 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if car4 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 375.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 375000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car4 = {car4 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if car5 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 562.500.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 562500000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car5 = {car5 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if car6 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 750.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 750000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car6 = {car6 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if car7 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 1.125.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 1125000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car7 = {car7 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if car8 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 2.250.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 2250000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car8 = {car8 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if car9 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 7.500.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 7500000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car9 = {car9 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"')
          connect.commit() 
       if car10 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 37.500.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 37500000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car10 = {car10 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"')
          connect.commit() 
       if car12 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою машину за 22.000.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 22000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET car12 = {car12 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET cart = {100} WHERE user_id = "{user_id}"')
          connect.commit() 

###########################################АДМИН КОМАНДЫ###########################################
    if message.text.startswith("выдать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       admin_id = 5592294018
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы выдали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          await bot.send_message(admin_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html') 
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
          await message.send_message(admin_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html') 
       if user_status[0] == 'Admin_Donate':
          if check <= 100000000000000:
             await message.reply(f"💰 | Вы выдали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
             await bot.send_message(admin_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET limit = {limit + perevod} WHERE user_id = "{user_id}"')
             connect.commit() 
             await message.send_message(admin_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html') 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы выдали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          await bot.send_message(admin_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html') 
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.startswith("Выдать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       admin_id = 5592294018
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы выдали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          await bot.send_message(admin_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html') 
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы выдали {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          await bot.send_message(admin_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал {perevod2}$ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html') 
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html') 

    if message.text.lower() in ["Reset", "reset"]: 
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       status = "Player"
       if user_status[0] == 'Owner':
          cursor.execute(f"UPDATE users SET balance = {10000000}")
          cursor.execute(f"UPDATE users SET bank = {100000}")
          cursor.execute(f"UPDATE users SET rating = {0}")
          cursor.execute(f"UPDATE users SET expe = {0}")
          cursor.execute(f"UPDATE users SET bitcoin = {100}")
          cursor.execute(f"UPDATE users SET energy = {0}")
          cursor.execute(f"UPDATE users SET farm_coin = {0}")
          cursor.execute(f"UPDATE users SET farm1 = {0}")
          cursor.execute(f"UPDATE users SET farm2 = {0}")
          cursor.execute(f"UPDATE users SET farm3 = {0}")
          cursor.execute(f"UPDATE users SET farm4 = {0}")
          cursor.execute(f"UPDATE users SET farm5 = {0}")
          cursor.execute(f"UPDATE users SET generator = {0}")
          cursor.execute(f"UPDATE users SET car1 = {0}")
          cursor.execute(f"UPDATE users SET car2 = {0}")
          cursor.execute(f"UPDATE users SET car3 = {0}")
          cursor.execute(f"UPDATE users SET car4 = {0}")
          cursor.execute(f"UPDATE users SET car5 = {0}")
          cursor.execute(f"UPDATE users SET car6 = {0}")
          cursor.execute(f"UPDATE users SET car7 = {0}")
          cursor.execute(f"UPDATE users SET car8 = {0}")
          cursor.execute(f"UPDATE users SET car9 = {0}")
          cursor.execute(f"UPDATE users SET car10 = {0}")
          cursor.execute(f"UPDATE users SET car11 = {0}")
          cursor.execute(f"UPDATE users SET car12 = {0}")
          cursor.execute(f"UPDATE users SET pet1 = {0}")
          cursor.execute(f"UPDATE users SET pet2 = {0}")
          cursor.execute(f"UPDATE users SET pet3 = {0}")
          cursor.execute(f"UPDATE users SET pet4 = {0}")
          cursor.execute(f"UPDATE users SET pet5 = {0}")
          cursor.execute(f"UPDATE users SET pet6 = {0}")
          cursor.execute(f"UPDATE users SET pet7 = {0}")
          cursor.execute(f"UPDATE users SET pet8 = {0}")
          cursor.execute(f"UPDATE users SET pet9 = {0}")
          cursor.execute(f"UPDATE users SET case1 = {0}")
          cursor.execute(f"UPDATE users SET case2 = {0}")
          cursor.execute(f"UPDATE users SET case3 = {0}")
          cursor.execute(f"UPDATE users SET case4 = {0}")
          cursor.execute(f"UPDATE users SET egg = {0}")
          cursor.execute(f"UPDATE users SET checking = {0}")
          cursor.execute(f"UPDATE users SET checking1 = {0}")
          cursor.execute(f"UPDATE users SET checking2 = {0}")
          cursor.execute(f"UPDATE users SET checking3 = {0}")
          cursor.execute(f"UPDATE users SET suprise = {0}")
          cursor.execute(f"UPDATE users SET farmcoin1 = {0}")
          cursor.execute(f"UPDATE users SET farmcoin2 = {0}")
          cursor.execute(f"UPDATE users SET farmcoin3 = {0}")
          cursor.execute(f"UPDATE users SET ore1 = {0}")
          cursor.execute(f"UPDATE users SET ore2 = {0}")
          cursor.execute(f"UPDATE users SET ore3 = {0}")
          cursor.execute(f"UPDATE users SET ore4 = {0}")
          cursor.execute(f"UPDATE users SET ore5 = {0}")
          cursor.execute(f"UPDATE users SET ore6 = {0}")
          cursor.execute(f"UPDATE users SET ore7 = {0}")
          cursor.execute(f"UPDATE users SET ore8 = {0}")
          cursor.execute(f"UPDATE users SET farmcoin4 = {0}")
          cursor.execute(f"UPDATE users SET farmcoin5 = {0}")
          cursor.execute(f"UPDATE users SET business1 = {0}")
          cursor.execute(f"UPDATE users SET business2 = {0}")
          cursor.execute(f"UPDATE users SET business3 = {0}")
          cursor.execute(f"UPDATE users SET business4 = {0}")
          cursor.execute(f"UPDATE users SET business5 = {0}")
          cursor.execute(f"UPDATE users SET business6 = {0}")
          cursor.execute(f"UPDATE users SET business7 = {0}")
          cursor.execute(f"UPDATE users SET business8 = {0}")
          cursor.execute(f"UPDATE users SET business9 = {0}")
          cursor.execute(f"UPDATE users SET workers = {0}")
          cursor.execute(f"UPDATE users SET busscash = {0}")
          cursor.execute(f"UPDATE users SET vcard = {0}")
          cursor.execute(f"UPDATE users SET bitmaning = {0}")
          connect.commit()
          await message.reply(f"База данных изменена! {rwin}")

    if message.text.lower() in ["Set chat", "set chat"]: 
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == 'Owner':
          cursor.execute(f"UPDATE chats SET cazna = {0}")
          connect.commit()
          await message.reply(f"База данных изменена! {rwin}")
          print("База данных изменена!")
          
    if message.text.lower() in ["Check", "check"]: 
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == 'Owner':
          cursor.execute(f"UPDATE users SET checking = {0}")
          cursor.execute(f"UPDATE users SET checking1 = {0}")
          cursor.execute(f"UPDATE users SET checking2 = {0}")
          cursor.execute(f"UPDATE users SET checking3 = {0}")
          connect.commit()
          await message.reply(f"База данных изменена! {rwin}")
          print("База данных изменена!")

    if message.text.lower() in ["Create", "create"]: 
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == 'Owner':
          business1 = "limit_trans"
          cursor.execute("ALTER TABLE users ADD COLUMN '%s' INT" % business1)
          connect.commit()
          await message.reply(f"База данных изменена! {rwin}")
          print("База данных изменена!")

    if message.text.lower() in ["Update", "update"]: 
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == 'Owner':
          cursor.execute(f'UPDATE users SET limit_trans = {0}')
          connect.commit() 
          await message.reply(f"База данных изменена! {rwin}")

    if message.text.startswith("забрать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы забрали {perevod2}$ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы забрали {perevod2}$ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.startswith("Забрать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы забрали {perevod2}$ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы забрали {perevod2}$ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.lower() in ["обнулить", "Обнулить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы обнулили игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET checking = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET checking1 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET checking2 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET checking3 = {0} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы обнулили игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')
    
    if message.text.lower() in ["users", "Users"]:
       num = 0
       list = cursor.execute(f"SELECT * FROM users ORDER BY balance DESC").fetchmany(50)
       top_list = []
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       if user_status2[0] == "Owner":
          for user in list:
              num += 1     
              b2 = '{:,}'.format(user[1])    
              top_list.append(f"{num}. {user[19]}  —  {b2} (👑 Рейтинг: {user[3]}) (ID: {user[82]})")
          top = "\n".join(top_list)
          await message.reply(f"Список игроков в боте:\n" + top , parse_mode='html')
       if user_status2[0] == "Admin":
          for user in list:
              num += 1     
              b2 = '{:,}'.format(user[1])    
              top_list.append(f"{num}. {user[19]}  —  {b2} (👑 Рейтинг: {user[3]}) (ID: {user[82]})")
          top = "\n".join(top_list)
          await message.reply(f"Список игроков в боте:\n" + top , parse_mode='html')
       if user_status2[0] == "Player":
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')


    if message.text.lower() in ["admin panel", "Admin panel"]:
       await message.reply(f"⚙️ | Admin commands: \nЗабанить - (reply or ID)\n-------------------------------------\nРазбанить - (reply or ID)\n-------------------------------------\nОбнулить - (reply)\n-------------------------------------\nВыдать [сумма] - (reply)\n-------------------------------------\nПосмотреть баланс - (ID)\n-------------------------------------\nUsers - top players 50\n-------------------------------------\nЗабрать [сумма] - (reply)\n-------------------------------------" , parse_mode='html')

    if message.text.startswith("посмотреть баланс"):
       msg = message
       r_user_id = int(message.text.split()[2]) 
       reply_user_id = cursor.execute("SELECT user_id from users where id = ?",(r_user_id,)).fetchone()
       reply_user_id = int(reply_user_id[0])
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(reply_user_id,)).fetchone()
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       if user_status2[0] == "Admin":
          balance = cursor.execute("SELECT balance from users where user_id = ?",(reply_user_id,)).fetchone()
          balance = int(balance[0])
          balance2 = '{0:,}'.format(balance).replace(',', '.')
          bank = cursor.execute("SELECT bank from users where user_id = ?",(reply_user_id,)).fetchone()
          bank = round(int(bank[0]))
          bank2 = '{0:,}'.format(bank).replace(',', '.')
          bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(reply_user_id,)).fetchone()
          bitcoin = round(int(bitcoin[0]))
          bitcoin2 = '{0:,}'.format(perevod).replace(',', '.')
          c = 999999999999999999999999
          if balance >= 999999999999999999999999:
             balance = 999999999999999999999999
             cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             balance2 = '{:,}'.format(balance) 
          else:
             pass
          if bank >= 999999999999999999999999:
             bank = 999999999999999999999999
             cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             bank2 = '{:,}'.format(bank) 
          else:
           pass
          if bitcoin >= 999999999999999999999999:
             bitcoin = 999999999999999999999999
             cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             bitcoin2 = '{:,}'.format(bitcoin)
          else:
           pass
          await message.reply(f"🔗 | Баланс игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>\n\n👫Ник: {reply_user_name} \n💰Деньги: {balance2}$ \n🏦Банк: {bank2}$\n💽 Биткоины: {bitcoin2}฿", parse_mode='html')
       if user_status2[0] == "Owner":
          balance = cursor.execute("SELECT balance from users where user_id = ?",(reply_user_id,)).fetchone()
          balance = int(balance[0])
          balance2 = '{0:,}'.format(balance).replace(',', '.')
          bank = cursor.execute("SELECT bank from users where user_id = ?",(reply_user_id,)).fetchone()
          bank = round(int(bank[0]))
          bank2 = '{0:,}'.format(bank).replace(',', '.')
          bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(reply_user_id,)).fetchone()
          bitcoin = round(int(bitcoin[0]))
          bitcoin2 = '{0:,}'.format(bitcoin).replace(',', '.')
          c = 999999999999999999999999
          if balance >= 999999999999999999999999:
             balance = 999999999999999999999999
             cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             balance2 = '{:,}'.format(balance) 
          else:
             pass
          if bank >= 999999999999999999999999:
             bank = 999999999999999999999999
             cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             bank2 = '{:,}'.format(bank) 
          else:
           pass
          if bitcoin >= 999999999999999999999999:
             bitcoin = 999999999999999999999999
             cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             bitcoin2 = '{:,}'.format(bitcoin)
          else:
           pass
          await message.reply(f"🔗 | Баланс игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>\n\n👫Ник: {reply_user_name} \n💰Деньги: {balance2}$ \n🏦Банк: {bank2}$\n💽 Биткоины: {bitcoin2}฿", parse_mode='html')

    if message.text.startswith("id"):
       msg = message
       r_user_id = message.reply_to_message.from_user.id
       reply_user_id = cursor.execute("SELECT id from users where user_id = ?",(r_user_id,)).fetchone()
       reply_user_id = int(reply_user_id[0])
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(r_user_id,)).fetchone()
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       if user_status2[0] == "Admin":         
          await message.reply(f"🔎 ID игрока <a href='tg://user?id={r_user_id}'>{reply_user_name}</a> - {reply_user_id}", parse_mode='html')
       if user_status2[0] == "Owner":
          await message.reply(f"🔎 ID игрока <a href='tg://user?id={r_user_id}'>{reply_user_name}</a> - {reply_user_id}", parse_mode='html')

    if message.text.startswith("ID"):
       msg = message
       r_user_id = message.reply_to_message.from_user.id
       reply_user_id = cursor.execute("SELECT id from users where user_id = ?",(r_user_id,)).fetchone()
       reply_user_id = int(reply_user_id[0])
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(r_user_id,)).fetchone()
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       if user_status2[0] == "Admin":         
          await message.reply(f"🔎 ID игрока <a href='tg://user?id={r_user_id}'>{reply_user_name}</a> - {reply_user_id}", parse_mode='html')
       if user_status2[0] == "Owner":
          await message.reply(f"🔎 ID игрока <a href='tg://user?id={r_user_id}'>{reply_user_name}</a> - {reply_user_id}", parse_mode='html')

    if message.text.startswith("Посмотреть баланс"):
       msg = message
       r_user_id = int(message.text.split()[2]) 
       reply_user_id = cursor.execute("SELECT user_id from users where id = ?",(r_user_id,)).fetchone()
       reply_user_id = reply_user_id[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(reply_user_id,)).fetchone()
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       if user_status2[0] == "Admin":
          balance = cursor.execute("SELECT balance from users where user_id = ?",(reply_user_id,)).fetchone()
          balance = int(balance[0])
          balance2 = '{0:,}'.format(balance).replace(',', '.')
          bank = cursor.execute("SELECT bank from users where user_id = ?",(reply_user_id,)).fetchone()
          bank = round(int(bank[0]))
          bank2 = '{0:,}'.format(bank).replace(',', '.')
          bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(reply_user_id,)).fetchone()
          bitcoin = round(int(bitcoin[0]))
          bitcoin2 = '{0:,}'.format(bitcoin).replace(',', '.')
          c = 999999999999999999999999
          if balance >= 999999999999999999999999:
             balance = 999999999999999999999999
             cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             balance2 = '{:,}'.format(balance) 
          else:
             pass
          if bank >= 999999999999999999999999:
             bank = 999999999999999999999999
             cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             bank2 = '{:,}'.format(bank) 
          else:
           pass
          if bitcoin >= 999999999999999999999999:
             bitcoin = 999999999999999999999999
             cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             bitcoin2 = '{:,}'.format(bitcoin)
          else:
           pass
          await message.reply(f"🔗 | Баланс игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>\n\n👫Ник: {reply_user_name} \n💰Деньги: {balance2}$ \n🏦Банк: {bank2}$\n💽 Биткоины: {bitcoin2}฿", parse_mode='html')
       if user_status2[0] == "Owner":
          balance = cursor.execute("SELECT balance from users where user_id = ?",(reply_user_id,)).fetchone()
          balance = int(balance[0])
          balance2 = '{0:,}'.format(balance).replace(',', '.')
          bank = cursor.execute("SELECT bank from users where user_id = ?",(reply_user_id,)).fetchone()
          bank = round(int(bank[0]))
          bank2 = '{0:,}'.format(bank).replace(',', '.')
          bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(reply_user_id,)).fetchone()
          bitcoin = round(int(bitcoin[0]))
          bitcoin2 = '{0:,}'.format(bitcoin).replace(',', '.')
          c = 999999999999999999999999
          if balance >= 999999999999999999999999:
             balance = 999999999999999999999999
             cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             balance2 = '{:,}'.format(balance) 
          else:
             pass
          if bank >= 999999999999999999999999:
             bank = 999999999999999999999999
             cursor.execute(f'UPDATE users SET bank = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             bank2 = '{:,}'.format(bank) 
          else:
           pass
          if bitcoin >= 999999999999999999999999:
             bitcoin = 999999999999999999999999
             cursor.execute(f'UPDATE users SET bitcoin = {999999999999999999999999}  WHERE user_id = ?', (reply_user_id,))
             connect.commit()
             bitcoin2 = '{:,}'.format(bitcoin)
          else:
           pass
          await message.reply(f"🔗 | Баланс игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>\n\n👫Ник: {reply_user_name} \n💰Деньги: {balance2}$ \n🏦Банк: {bank2}$\n💽 Биткоины: {bitcoin2}฿", parse_mode='html')

    if message.text.startswith("забанить"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Blocked"
       if not message.reply_to_message: 
          r_user_id = int(msg.text.split()[1]) 
          reply_user_name = cursor.execute("SELECT user_name from users where id = ?",(r_user_id,)).fetchone()
          reply_user_name = reply_user_name[0]
          reply_user_id = cursor.execute("SELECT user_id from users where id = ?",(r_user_id,)).fetchone()
          reply_user_id = reply_user_id[0]
          if user_status2[0] == "Admin":
             await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == "Owner":
             await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == 'Player':
             await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

       if message.reply_to_message: 
          reply_user_id = msg.reply_to_message.from_user.id
          reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
          reply_user_name = reply_user_name[0]
          if user_status2[0] == "Admin":
             await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == "Owner":
             await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == 'Player':
             await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

    if message.text.startswith("Забанить"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Blocked"
       if not message.reply_to_message: 
          r_user_id = int(msg.text.split()[1]) 
          reply_user_name = cursor.execute("SELECT user_name from users where id = ?",(r_user_id,)).fetchone()
          reply_user_name = reply_user_name[0]
          reply_user_id = cursor.execute("SELECT user_id from users where id = ?",(r_user_id,)).fetchone()
          reply_user_id = reply_user_id[0]
          if user_status2[0] == "Admin":
             await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == "Owner":
             await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == 'Player':
             await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

       if message.reply_to_message: 
          reply_user_id = msg.reply_to_message.from_user.id
          reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
          reply_user_name = reply_user_name[0]
          if user_status2[0] == "Admin":
             await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == "Owner":
             await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET bitcoin = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET expe = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car10 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET car11 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet1 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet2 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet3 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet4 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet5 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet6 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet7 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet8 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET pet9 = {0} WHERE user_id = "{reply_user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == 'Player':
             await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

    if message.text.lower() in ["повысить", "Повысить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Admin"
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы выдали админа бота игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
          admin_id = 5592294018
          await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал роль (Админ) игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')

    if message.text.lower() in ["+owner", "+Owner"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Owner"
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы выдали создателя бота игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
          admin_id = 5592294018
          await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал роль (Владелец) игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')

    if message.text.startswith("изменить статус"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       status = " ".join(message.text.split()[2:])
       if user_status2[0] == "Owner":
          await message.reply(f"🔮 | Вы выдали статус - {status} - игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET status = \"{status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')

    if message.text.startswith("изменить id"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       newid = int(msg.text.split()[2])
       if user_status2[0] == "Owner":
          await message.reply(f"🔎 | Вы выдали ID - {newid} - игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET id = \"{newid}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
    
    if message.text.startswith("Изменить id"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       newid = int(msg.text.split()[2])
       if user_status2[0] == "Owner":
          await message.reply(f"🔎 | Вы выдали ID - {newid} - игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET id = \"{newid}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')

    if message.text.startswith("Изменить статус"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       status = " ".join(message.text.split()[2:])
       if user_status2[0] == "Owner":
          await message.reply(f"🔮 | Вы выдали статус - {status} - игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET status = \"{status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')

    if message.text.lower() in ["разжаловать", "Разжаловать"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Player"
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы забрали админа бота у игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       
    if message.text.startswith("разбанить"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       user_status = "Player"
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if not message.reply_to_message: 
          r_user_id = int(msg.text.split()[1]) 
          reply_user_id = cursor.execute("SELECT user_id from users where id = ?",(r_user_id,)).fetchone()
          reply_user_id = reply_user_id[0]
          reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(reply_user_id,)).fetchone()
          reply_user_name = reply_user_name[0]
          if user_status2[0] == "Admin":
             await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == "Owner":
             await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == 'Player':
             await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')
       if message.reply_to_message:
          reply_user_id = msg.reply_to_message.from_user.id
          reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(reply_user_id,)).fetchone()
          reply_user_name = reply_user_name[0]
          if user_status2[0] == "Admin":
             await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == "Owner":
             await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == 'Player':
             await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

    if message.text.startswith("Разбанить"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       user_status = "Player"
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if not message.reply_to_message: 
          r_user_id = int(msg.text.split()[1]) 
          reply_user_id = cursor.execute("SELECT user_id from users where id = ?",(r_user_id,)).fetchone()
          reply_user_id = reply_user_id[0]
          reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(reply_user_id,)).fetchone()
          reply_user_name = reply_user_name[0]
          if user_status2[0] == "Admin":
             await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == "Owner":
             await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == 'Player':
             await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')
       if message.reply_to_message:
          reply_user_id = msg.reply_to_message.from_user.id
          reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(reply_user_id,)).fetchone()
          reply_user_name = reply_user_name[0]
          if user_status2[0] == "Admin":
             await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == "Owner":
             await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
             connect.commit()
          if user_status2[0] == 'Player':
             await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')
       

######################################РП КОМАНДЫ#################################################
    if message.text.lower() in ["рп-команды", "РП-команды"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, список РП-команд:\n🤗 | Обнять\n🧊 | Ударить об лёд\n❄️ | Кинуть снежок\n👏 | Похлопать\n👨‍💻 | Заскамить\n☕️ | Пригласить на чай\n👉👌 | Изнасиловать\n🤝 | Взять за руку\n📱 | Подарить айфон\n✋ | Дать пять\n😬 | Укусить\n🤛 | Ударить\n🤲 | Прижать\n💋 | Чмок\n💋 | Поцеловать\n😼 | Кусь\n🤲 | Прижать\n🔪 | Убить\n🤜 | Уебать\n💰 | Украсть\n🔞 | Выебать\n👅 | Отсосать\n👅 | Отлизать\n🔞 | Трахнуть\n🔥 | Сжечь\n💐 | Подарить цветы", parse_mode='html')

    if message.text.lower() in ["чмок", "Чмок"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | <a href='tg://user?id={user_id}'>{user_name}</a> чмокнул(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["кусь", "Кусь"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😼 | <a href='tg://user?id={user_id}'>{user_name}</a> кусьнул(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["обнять", "Обнять"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤗 | <a href='tg://user?id={user_id}'>{user_name}</a> обнял(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["подарить цветы", "Подарить цветы"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💐 | <a href='tg://user?id={user_id}'>{user_name}</a> подарил(-а) цветы <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

    if message.text.lower() in ["поцеловать", "Поцеловать"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | <a href='tg://user?id={user_id}'>{user_name}</a> поцеловал(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["дать пять", "Дать пять"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"✋ | <a href='tg://user?id={user_id}'>{user_name}</a> дал(-а) пять <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["подарить айфон", "Подарить айфон"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"📱 | <a href='tg://user?id={user_id}'>{user_name}</a> подарил(-а) айфон <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["ударить об лед", "Ударить об лед", "Ударить об лёд", "ударить об лёд"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🧊 | <a href='tg://user?id={user_id}'>{user_name}</a> ударил(-а) головой об лёд <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["ударить", "Ударить"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤛 | <a href='tg://user?id={user_id}'>{user_name}</a> ударил(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["заскамить", "Заскамить"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👨‍💻 | <a href='tg://user?id={user_id}'>{user_name}</a> заскамил(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | <a href='tg://user?id={user_id}'>{user_name}</a> прижал(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["укусить", "Укусить"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😬 | <a href='tg://user?id={user_id}'>{user_name}</a> укусил(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["взять за руку", "Взять за руку"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤝 | <a href='tg://user?id={user_id}'>{user_name}</a> взял(-а) за руку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["кинуть снежок", "Кинуть снежок"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"❄️ | <a href='tg://user?id={user_id}'>{user_name}</a> кинул(-а) снежок в <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | <a href='tg://user?id={user_id}'>{user_name}</a> прижал(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["похлопать", "Похлопать"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👏 | <a href='tg://user?id={user_id}'>{user_name}</a> похлопал(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["изнасиловать", "Изнасиловать"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👉👌 | <a href='tg://user?id={user_id}'>{user_name}</a> изнасиловал(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["пригласить на чай", "Пригласить на чай"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"☕️ | <a href='tg://user?id={user_id}'>{user_name}</a> пригласил(-а) на чай <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["убить", "Убить"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔪 | <a href='tg://user?id={user_id}'>{user_name}</a> убил(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["уебать", "Уебать"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤜 | <a href='tg://user?id={user_id}'>{user_name}</a> уебал(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
    if message.text.lower() in ["украсть", "Украсть"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> украл(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

    if message.text.lower() in ["отсосать", "Отсосать"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | <a href='tg://user?id={user_id}'>{user_name}</a> отсосал(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

    if message.text.lower() in ["отлизать", "Отлизать"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | <a href='tg://user?id={user_id}'>{user_name}</a> отлизал(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

    if message.text.lower() in ["выебать", "Выебать"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | <a href='tg://user?id={user_id}'>{user_name}</a> выебал(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

    if message.text.lower() in ["сжечь", "Сжечь"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔥 | <a href='tg://user?id={user_id}'>{user_name}</a> сжёг <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

    if message.text.lower() in ["трахнуть", "Трахнуть"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply = message.reply_to_message
       user_id = message.from_user.id
       reply_user_id = message.reply_to_message.from_user.id
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | <a href='tg://user?id={user_id}'>{user_name}</a> трахнул(-а) <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')

######################################ПИТОМЦЫ#################################################
    if message.text.lower() in ["питомцы", "Питомцы"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id
       user_id = message.from_user.id
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, доступные питомцы:\n🐥 1. Цыплёнок - 1.000.000$\n🐈 2. Кот - 100.000.000$\n🐕 3. Пёс - 500.000.000$\n🦜 4. Попугай - 1.000.000.000$\n🦄 5. Единорог - 50.000.000.000$\n🐒 6. Обезьяна - 100.000.000.000$\n🐬 7. Дельфин - 500.000.000.000$\n🐅 8. Тигр - 10.000.000.000.000$\n🐉 9. Дракон - 100.000.000.000.000$\n\n🛒 Для покупки питомца введите: Купить питомца [номер]\nℹ Для просмотра информации о своем питомце введите: Мой питомец", parse_mode='html')

    if message.text.lower() in ["купить питомца 1", "Купить питомца 1"]:     
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet1 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🐥 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили цыплёнка за 1.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet1 = {pet1 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if pet1 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный питомец! {rloser}", parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть питомец! {rloser}", parse_mode='html')     

    if message.text.lower() in ["купить питомца 2", "Купить питомца 2"]:    
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 100000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet2 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🐈 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили кота за 100.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet2 = {pet2 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if pet2 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный питомец! {rloser}", parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть питомец! {rloser}", parse_mode='html')     

    if message.text.lower() in ["купить питомца 3", "Купить питомца 3"]:     
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 500000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet3 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🐕 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили пса за 500.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet3 = {pet3 + c} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if pet3 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный питомец! {rloser}", parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть питомец! {rloser}", parse_mode='html') 

    if message.text.lower() in ["купить питомца 4", "Купить питомца 4"]:   
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet4 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🦜 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили попугая за 1.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet4 = {pet4 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if pet4 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный питомец! {rloser}", parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть питомец! {rloser}", parse_mode='html') 

    if message.text.lower() in ["купить питомца 5", "Купить питомца 5"]:     
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 50000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet5 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🦄 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили единорога за 50.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet5 = {pet5 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if pet5 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный питомец! {rloser}", parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть питомец! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить питомца 6", "Купить питомца 6"]:      
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 100000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet6 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🐒 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили обезьяну за 100.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet6 = {pet6 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if pet6 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный питомец! {rloser}", parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть питомец! {rloser}", parse_mode='html')                        

    if message.text.lower() in ["купить питомца 7", "Купить питомца 7"]:    
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 500000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       print(pets)
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet7 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🐬 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили дельфина за 500.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet7 = {pet7 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if pet7 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный питомец! {rloser}", parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть питомец! {rloser}", parse_mode='html') 

    if message.text.lower() in ["купить питомца 8", "Купить питомца 8"]:     
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 10000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet8 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🐅 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили тигра за 10.000.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet8 = {pet8 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if pet8 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный питомец! {rloser}", parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть питомец! {rloser}", parse_mode='html') 

    if message.text.lower() in ["купить питомца 9", "Купить питомца 9"]:     
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 100000000000000
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if int(pets) == 0:
          if pet9 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🐉 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили дракона за 100.000.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet9 = {pet9 + c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if pet9 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный питомец! {rloser}", parse_mode='html')     
             return
       if pets == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть питомец! {rloser}", parse_mode='html') 

    if message.text.lower() in ["мой питомец", "Мой питомец"]:        
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10 + pet11
       if pets == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету питомца! {rloser}", parse_mode='html')    
       if pet1 == 1:
          photo = open('pet1.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🐥 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: цыплёнок \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')            
       if pet2 == 1:     
          photo = open('pet2.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🐈 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: кот \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                    
       if pet3 == 1:   
          photo = open('pet3.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🐕 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: пёс \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                            
       if pet4 == 1:           
          photo = open('pet4.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🦜 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: попугай \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                            
       if pet5 == 1:
          photo = open('pet5.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🦄 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: единорог \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                                       
       if pet6 == 1:
          photo = open('pet6.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🐒 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: обезьяна \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                                       
       if pet7 == 1:
          photo = open('lpet7.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🐬 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: дельфин \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                                       
       if pet8 == 1:
          photo = open('pet8.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🐅 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: тигр \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                                       
       if pet9 == 1: 
          photo = open('pet9.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🐉 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: дракон \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                                      
       if pet10 == 1:
          photo = open('pet10.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"☃️ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: снеговик \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                                       
       if pet11 == 1:
          photo = open('pet11.jpg', 'rb')
          await message.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=f"🐰  | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец: пасхальный кролик \n✏️ | Имя питомца: {pet_name}\n❤️ | ХП: {pet_hp} \n🍗 | Сытость: {pet_eat}\n☀️ | Настроение: {pet_mood} \n\n✏ | Питомец имя [имя] - изменить имя питомца\n❤ | Вылечить питомца - вылечить питомца\n🍗 | Покормить питомца - покормить питомца\n🌳 | Выгулять питомца - поднять настроение питомцу", parse_mode='html')                                       

    if message.text.lower() in ["вылечить питомца", "Вылечить питомца"]:   
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10 + pet11
       c = Decimal((100 - pet_hp) * 10000)
       c3 = '{0:,}'.format(c).replace(',', '.')
       c2 = (100 - pet_hp) * 10000
       hp = 100 - pet_hp
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if pets == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету питомца! {rloser}", parse_mode='html')  
       if pet1 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet2 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet3 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet4 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet5 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet6 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet7 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet8 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet9 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet10 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')
       if pet11 == 1:
          if pet_hp < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы вылечили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_hp = {pet_hp + hp} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_hp == 100:
             await bot.send_message(message.chat.id, f"❤ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не нуждается в лечении!", parse_mode='html')

    if message.text.lower() in ["покормить питомца", "Покормить питомца"]:   
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10 + pet11
       c = Decimal((100 - pet_eat) * 10000)
       c3 = '{0:,}'.format(c).replace(',', '.')
       c2 = (100 - pet_eat) * 10000
       eat = 100 - pet_eat
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if pets == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету питомца! {rloser}", parse_mode='html')  
       if pet1 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet2 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet3 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet4 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet5 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet6 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet7 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet8 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet9 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet10 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')
       if pet11 == 1:
          if pet_eat < 100:
             if c <= balance:
                await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы покормили своего питомца за {c3}!", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet_eat = {pet_eat + eat} WHERE user_id = "{user_id}"')
             if c > balance:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
          if pet_eat == 100:
             await bot.send_message(message.chat.id, f"🍗 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не голоден! {rloser}", parse_mode='html')

    if message.text.lower() in ["выгулять питомца", "Выгулять питомца"]:  
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10 + pet11
       c = Decimal((100 - pet_mood) * 10000)
       mood = 100 - pet_mood
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if pets == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету питомца! {rloser}", parse_mode='html')  
       if pet1 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet2 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet3 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet4 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet5 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet6 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet7 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet8 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet9 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet10 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')
       if pet11 == 1:
          if pet_mood < 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, вы выгуляли своего питомца!", parse_mode='html')
             cursor.execute(f'UPDATE users SET pet_mood = {pet_mood + mood} WHERE user_id = "{user_id}"')
          if pet_mood == 100:
             await bot.send_message(message.chat.id, f"🌳 <a href='tg://user?id={user_id}'>{user_name}</a>, ваш питомец не хочет гулять!", parse_mode='html')

    if message.text.startswith("питомец имя"): 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10 + pet11
       name = " ".join(message.text.split()[2:])
       if len(name) <= 20:
          pass
       else: 
          await bot.send_message(message.chat.id, f"ℹ️️ | <a href='tg://user?id={user_id}'>{user_name}</a> , ник питомца не может быть длинее 20 символов!", parse_mode='html')
          return
       if pets == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету питомца! {rloser}", parse_mode='html')
       if pet1 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet2 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet3 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet4 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet5 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet6 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet7 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet8 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet9 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet10 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet11 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')

    if message.text.startswith("Питомец имя"): 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10 + pet11
       name = " ".join(message.text.split()[2:])
       if len(name) <= 20:
          pass
       else: 
          await bot.send_message(message.chat.id, f"ℹ️️ | <a href='tg://user?id={user_id}'>{user_name}</a> , ник питомца не может быть длинее 20 символов!", parse_mode='html')
          return
       if pets == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету питомца! {rloser}", parse_mode='html')
       if pet1 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet2 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet3 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet4 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet5 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet6 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet7 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet8 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet9 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet10 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')
       if pet11 == 1:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поменяли имя своего питомца на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET pet_name = \"{name}\" WHERE user_id = "{user_id}"')

    if message.text.lower() in ["продать питомца", "Продать питомца"]:  
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       pet1 = cursor.execute("SELECT pet1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet1 = int(pet1[0])
       pet2 = cursor.execute("SELECT pet2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet2 = int(pet2[0])
       pet3 = cursor.execute("SELECT pet3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet3 = int(pet3[0])
       pet4 = cursor.execute("SELECT pet4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet4 = int(pet4[0])
       pet5 = cursor.execute("SELECT pet5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet5 = int(pet5[0])
       pet6 = cursor.execute("SELECT pet6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet6 = int(pet6[0])
       pet7 = cursor.execute("SELECT pet7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet7 = int(pet7[0])
       pet8 = cursor.execute("SELECT pet8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet8 = int(pet8[0])
       pet9 = cursor.execute("SELECT pet9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet9 = int(pet9[0])
       pet10 = cursor.execute("SELECT pet10 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet10 = int(pet10[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = int(pet11[0])
       pet_name = cursor.execute("SELECT pet_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_name = str(pet_name[0])
       pet_hp = cursor.execute("SELECT pet_hp from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_hp = int(pet_hp[0])
       pet_eat = cursor.execute("SELECT pet_eat from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_eat = int(pet_eat[0])
       pet_mood = cursor.execute("SELECT pet_mood from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet_mood = int(pet_mood[0])
       chat_id = message.chat.id
       user_id = message.from_user.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       c = 1
       pets = pet1 + pet2 + pet3 + pet4 + pet5 + pet6 + pet7 + pet8 + pet9 + pet10 + pet11
       if pets == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету питомца! {rloser}", parse_mode='html')
       if pet1 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 750.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 750000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet1 = {pet1 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet2 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 75.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 75000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet2 = {pet2 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet3 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 375.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 375000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet3 = {pet3 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet4 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 750.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 750000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet4 = {pet4 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet5 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 37.500.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 37500000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet5 = {pet5 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet6 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 75.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 75000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet6 = {pet6 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"')
       if pet7 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 375.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 375000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet7 = {pet7 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet8 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 7.500.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 7500000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet8 = {pet8 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"')
       if pet9 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 75.000.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 75000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet9 = {pet9 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet10 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 22.000.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 22000000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet10 = {pet10 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 
       if pet11 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали своего питомца за 10.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 10000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet11 = {pet11 - c} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_hp = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_eat = {100} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET pet_mood = {100} WHERE user_id = "{user_id}"') 

######################################РАБОТА#################################################
    if message.text.lower() in ["работать", "Работать"]:
       await asyncio.sleep(1)  
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       chat_id = message.chat.id
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       args = message.get_args()
       x = random.randint(500000,5000000)
       work = random.randint(1,10)
       period = 3600
       get = cursor.execute("SELECT last_work FROM users WHERE user_id=?", (user_id,)).fetchall()
       last_work = f"{int(get[0][0])}"
       worktime = time.time() - float(last_work)
       x2 = '{0:,}'.format(x).replace(',', '.')
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if worktime > period:
          if work == 1:
             await bot.send_message(chat_id, f"🧹 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты поработал дворником и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit()   
          if work == 2:
             await bot.send_message(chat_id, f"🛎 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты поработал оффициантом и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 3:
             await bot.send_message(chat_id, f"💻 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты написал сайт и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 4:
             await bot.send_message(chat_id, f"📦 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты поработал курьером и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 5:
             await bot.send_message(chat_id, f"🍯 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты продал бабушкины заготовки и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 6:
             await bot.send_message(chat_id, f"🍎 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты поработал продавцом и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 7:
             await bot.send_message(chat_id, f"🍕 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты поработал доставщиком пиццы и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 8:
             await bot.send_message(chat_id, f"🔦 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты поработал охранником и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
          if work == 9:
             await bot.send_message(chat_id, f"🙏 | <a href='tg://user?id={user_id}'>{user_name}</a>, ты попрошайничал у людей и заработал {x2}$", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + x} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET last_work=? WHERE user_id=?', (time.time(), user_id,))
             connect.commit() 
       else:
          await bot.send_message(message.chat.id, f"ℹ️ | {user_name}, вы уже работали недавно, приходите через час! {rloser}", parse_mode='html')

###########################################КЕЙСЫ###########################################
    if message.text.lower() in ["кейсы", "Кейсы"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case1 = cursor.execute("SELECT case1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case2 = cursor.execute("SELECT case2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case3 = cursor.execute("SELECT case3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case4 = cursor.execute("SELECT case4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case1 = int(case1[0])
       case2 = int(case2[0])
       case3 = int(case3[0])
       case4 = int(case4[0])
       cs1 = '{0:,}'.format(case1).replace(',', '.')
       cs2 = '{0:,}'.format(case2).replace(',', '.')
       cs3 = '{0:,}'.format(case3).replace(',', '.')
       cs4 = '{0:,}'.format(case4).replace(',', '.')
       c = int(case1) + int(case2) + int(case3) + int(case4)
       c = int(c)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       if c == 0:
          m = "😕 | У вас нету кейсов.\n\n"
          m1 = "🛒 | Для покупки кейсы введите «купить кейс [номер] [сумма]»"
       if c >= 1:
          m = "🧾 | Ваши кейсы:\n"
          m1 = "🔐 | Для открытия кейсов используйте - «Открыть кейс [1/2/3]»"
       if case1 == 0:
          s1 = ""
       if case1 >= 1:
          s1 = f"     📦 Обычный кейс - {cs1}шт.\n"
       if case2 == 0:
          s2 = ""
       if case2 >= 1:
          s2 = f"     🏵 Золотой кейс - {cs2}шт.\n"
       if case3 == 0:
          s3 = ""
       if case3 >= 1:
          s3 = f"     💎 Алмазный кейс - {cs3}шт.\n"
       if ivent == 1:
          if case4 == 0:
             s4 = ""
          if case4 >= 1:
             s4 = f"     🐰 Пасхальный кейс - {cs4}шт.\n"
       if ivent == 0:
          await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, доступные кейсы:\n🎁 1. Обычный кейс - 50 млрд.\n🎁 2. Золотой кейс - 1 трлн.\n🎁 3. Алмазный кейс - 5 трлн.\n\n{m}{s1}{s2}{s3}\n{m1}", parse_mode='html')
       if ivent == 1:
          await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, доступные кейсы:\n🎁 1. Обычный кейс - 50 млрд.\n🎁 2. Золотой кейс - 1 трлн.\n🎁 3. Алмазный кейс - 5 трлн.\n🎁 4. Пасхальный кейс - 2 трлн.\n\n{m}{s1}{s2}{s3}{s4}\n{m1}", parse_mode='html')

    if message.text.startswith("купить кейс 1"): 
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case1 = cursor.execute("SELECT case1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case1 = int(case1[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 50000000000 * summ
       c2 = '{0:,}'.format(c).replace(',', '.')
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} обычных кейсов за {c2}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case1 = {case1 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("купить кейс 2"):  
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case2 = cursor.execute("SELECT case2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case2 = int(case2[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 1000000000000 * summ
       c2 = '{0:,}'.format(c).replace(',', '.')
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} золотых кейсов за {c2}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case2 = {case2 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("купить кейс 3"): 
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case3 = cursor.execute("SELECT case3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case3 = int(case3[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 5000000000000 * summ
       c2 = '{0:,}'.format(c).replace(',', '.')
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} алмазных кейсов за {c2}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case3 = {case3 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("купить кейс 4"): 
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case4 = cursor.execute("SELECT case4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case4 = int(case4[0])
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 2000000000000 * summ
       c2 = '{0:,}'.format(c).replace(',', '.')
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return 
       if ivent == 1:
          if summ >= 1:
             if balance >= c:
                await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} пасхальных кейсов за {c2}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 + summ} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             if balance < c:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if summ <= 0:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, пасхальный ивент еще не начался! {rloser}", parse_mode='html')

    if message.text.startswith("Купить кейс 1"): 
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case1 = cursor.execute("SELECT case1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case1 = int(case1[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 50000000000 * summ
       c2 = '{0:,}'.format(c).replace(',', '.')
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} обычных кейсов за {c2}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case1 = {case1 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("Купить кейс 2"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case2 = cursor.execute("SELECT case2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case2 = int(case2[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 1000000000000 * summ
       c2 = '{0:,}'.format(c).replace(',', '.')
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} золотых кейсов за {c2}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case2 = {case2 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("Купить кейс 3"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case3 = cursor.execute("SELECT case3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case3 = int(case3[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 5000000000000 * summ
       c2 = '{0:,}'.format(c).replace(',', '.')
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if summ >= 1:
          if balance >= c:
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} алмазных кейсов за {c2}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case3 = {case3 + summ} WHERE user_id = "{user_id}"') 
             connect.commit()    
             return
          if balance < c:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
             return
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')

    if message.text.startswith("Купить кейс 4"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case4 = cursor.execute("SELECT case4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case4 = int(case4[0])
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       summ = int(msg.text.split()[3])
       c = 2000000000000 * summ
       c2 = '{0:,}'.format(c).replace(',', '.')
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if ivent == 1:
          if summ >= 1:
             if balance >= c:
                await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ2} пасхальных кейсов за {c2}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 + summ} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             if balance < c:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')
                return
          if summ <= 0:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, нельзя купить отрицательное число! {rloser}", parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, пасхальный ивент еще не начался! {rloser}", parse_mode='html')
             
    if message.text.lower() in ["открыть кейс 1", "Открыть кейс 1"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case1 = cursor.execute("SELECT case1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case1 = int(case1[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       money = ('44000000000', '45000000000', '46000000000', '47000000000', '48000000000', '49000000000', '50000000000', '51000000000', '52000000000', '53000000000', '54000000000', '55000000000')
       rmoney = random.choice(money)
       rmoney = int(rmoney)
       rmoney2 = '{0:,}'.format(rmoney).replace(',', '.')
       rrating = random.randint(0, 50)
       rrating2 = '{0:,}'.format(rrating).replace(',', '.')
       rexpe = random.randint(0, 50)
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
       expe = int(expe[0])
       prize = random.randint(1, 3)
       if case1 >= 1:
          if prize == 1:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rmoney2}$! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + rmoney} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case1 = {case1 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if prize == 2:
             await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rrating2} рейтинга! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET rating = {rating + rrating} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case1 = {case1 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()
          if prize == 3:
             await bot.send_message(message.chat.id, f" 🌟 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rexpe} опыта! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET expe = {expe + rexpe} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case1 = {case1 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()     
       if case1 <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету данного кейса! {rloser}", parse_mode='html')

    if message.text.lower() in ["открыть кейс 2", "Открыть кейс 2"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case2 = cursor.execute("SELECT case2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case2 = int(case2[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       money = ('950000000000', '960000000000', '970000000000', '980000000000', '990000000000', '1000000000000', '1010000000000', '1020000000000', '1030000000000', '1040000000000', '1050000000000', '1060000000000', '1070000000000', '1080000000000', '1090000000000', '1100000000000')
       rmoney = random.choice(money)
       rmoney = int(rmoney)
       rmoney2 = '{0:,}'.format(rmoney).replace(',', '.')
       rrating = random.randint(4750, 6750)
       rrating2 = '{0:,}'.format(rrating).replace(',', '.')
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       prize = random.randint(1, 3)
       rexpe = random.randint(50, 100)
       expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
       expe = int(expe[0])
       if case2 >= 1:
          if prize == 1:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rmoney2}$! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + rmoney} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case2 = {case2 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if prize == 2:
             await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rrating2} рейтинга! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET rating = {rating + rrating} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case2 = {case2 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if prize == 3:
             await bot.send_message(message.chat.id, f" 🌟 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rexpe} опыта! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET expe = {expe + rexpe} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case2 = {case2 - 1} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if case2 <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету данного кейса! {rloser}", parse_mode='html')

    if message.text.lower() in ["открыть кейс 3", "Открыть кейс 3"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case3 = cursor.execute("SELECT case3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case3 = int(case3[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       money = ('4950000000000', '4960000000000', '4970000000000', '4980000000000', '4990000000000', '5000000000000', '5010000000000', '5020000000000', '5030000000000', '5040000000000', '5050000000000', '5060000000000', '5070000000000', '5080000000000', '5090000000000', '5100000000000')
       rmoney = random.choice(money)
       rmoney = int(rmoney)
       rmoney2 = '{0:,}'.format(rmoney).replace(',', '.')
       rrating = random.randint(25000, 33500)
       rrating2 = '{0:,}'.format(rrating).replace(',', '.')
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       prize = random.randint(1, 3)
       rexpe = random.randint(100, 250)
       expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
       expe = int(expe[0])
       if case3 >= 1:
          if prize == 1:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rmoney2}$! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + rmoney} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case3 = {case3 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if prize == 2:
             await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rrating2} рейтинга! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET rating = {rating + rrating} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case3 = {case3 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()  
          if prize == 3:
             await bot.send_message(message.chat.id, f" 🌟 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rexpe} опыта! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET expe = {expe + rexpe} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET case3 = {case3 - 1} WHERE user_id = "{user_id}"') 
             connect.commit()  
       if case3 <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету данного кейса! {rloser}", parse_mode='html')

    if message.text.lower() in ["открыть кейс 4", "Открыть кейс 4"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       case4 = cursor.execute("SELECT case4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       case4 = int(case4[0])
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       money = ('1950000000000', '1960000000000', '1970000000000', '1980000000000', '1990000000000', '2000000000000', '2010000000000', '2020000000000', '2030000000000', '2040000000000', '2050000000000', '2060000000000', '2070000000000', '2080000000000', '2090000000000', '2100000000000')
       rmoney = random.choice(money)
       rmoney = int(rmoney)
       rrating = random.randint(1500, 2500)
       rexpe = random.randint(100, 250)
       rmoney2 = '{0:,}'.format(rmoney).replace(',', '.')
       rsnow = random.randint(1, 5)
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       prize = random.randint(1, 4)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       egg = cursor.execute("SELECT egg from users where user_id = ?",(message.from_user.id,)).fetchone()
       egg = int(egg[0])
       expe = cursor.execute("SELECT expe from users where user_id = ?", (message.from_user.id,)).fetchone()
       expe = int(expe[0])
       if ivent == 1:
          if case4 >= 1:
             if prize == 1:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rmoney2}$! {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + rmoney} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 - 1} WHERE user_id = "{user_id}"') 
                connect.commit()   
             if prize == 2:
                await bot.send_message(message.chat.id, f"👑 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rrating} рейтинга! {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET rating = {rating + rrating} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 - 1} WHERE user_id = "{user_id}"')
                connect.commit()    
             if prize == 3:
                await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rsnow} пасхальных яиц! {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET egg = {egg + rsnow} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 - 1} WHERE user_id = "{user_id}"') 
                connect.commit()  
             if prize == 4:
                await bot.send_message(message.chat.id, f" 🌟 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам выпало {rexpe} опыта! {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET expe = {expe + rexpe} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET case4 = {case4 - 1} WHERE user_id = "{user_id}"') 
                connect.commit()   
          if case4 <= 0:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету данного кейса! {rloser}", parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, пасхальный ивент еще не начался или уже закончен! {rloser}", parse_mode='html')

######################################ПАСХАЛЬНЫЙ ИВЕНТ#################################################
    if message.text.lower() in ["пасхальный ивент", "Пасхальный ивент"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       egg = cursor.execute("SELECT egg from users where user_id = ?",(message.from_user.id,)).fetchone()
       egg = int(egg[0])
       if ivent == 1:
          await bot.send_message(message.chat.id, f'🐰"Пасхальный ивент"🐰\n\n🥚 Кол-во пасхальных яиц: {egg}\n\n🌟 Награды:\n1. 💰 10.000.000$ - 10🥚\n2. 👑 1 рейтинг - 25🥚\n3. 🐰 Эксклюзивный питомец "Пасхальный кролик" - 50🥚\n4. 🎆 Особый статус "✨ Пасха 2022" - 250🥚\n\nℹ️ Пасхальные яйца можно заработать открывая "Пасхальные кейсы".\n📦 В кейсах можно заработать: от 1 до 5 пасхальных яиц.\n🥚️ Заходя каждый день в игру вы будете получать по 9 пасхальных яиц.\nℹ️ Чтобы забрать желаемую награду введите: ивент забрать [номер].\nℹ Не забывай каждый день читать новости на нашем канале, так как в течении недели мы будем публиковать разные промокоды на игровую и ивентную валюты и раздавать экслюзивные вещи которые вы сможете продать или оставить на память.\n📆 Ивент продлится с 24.04.22 по 31.04.22', parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, пасхальный ивент еще не начался или уже закончен! {rloser}", parse_mode='html')
   
    if message.text.lower() in ["ивент забрать 1", "Ивент забрать 1"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       egg = cursor.execute("SELECT egg from users where user_id = ?",(message.from_user.id,)).fetchone()
       egg = int(egg[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 10
       if ivent == 1:
          if egg >= 10:
             await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы обменяли свои пасхальные яйца на 10.000.000$! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET egg = {egg - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + 10000000} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if egg < 10:
             await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно пасхальных яиц! {rloser}", parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, пасхальный ивент еще не начался или уже закончен! {rloser}", parse_mode='html')

    if message.text.lower() in ["ивент забрать 2", "Ивент забрать 2"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       egg = cursor.execute("SELECT egg from users where user_id = ?",(message.from_user.id,)).fetchone()
       egg = int(egg[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = round(int(rating[0]))
       summ = 25
       if ivent == 1:
          if egg >= 25:
             await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы обменяли свои пасхальные яйца на 1👑! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET egg = {egg - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET rating = {rating + 1} WHERE user_id = "{user_id}"') 
             connect.commit()   
          if egg < 25:
             await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно пасхальных яиц! {rloser}", parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, пасхальный ивент еще не начался или уже закончен! {rloser}", parse_mode='html')

    if message.text.lower() in ["ивент забрать 3", "Ивент забрать 3"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       egg = cursor.execute("SELECT egg from users where user_id = ?",(message.from_user.id,)).fetchone()
       egg = int(egg[0])
       pet11 = cursor.execute("SELECT pet11 from users where user_id = ?",(message.from_user.id,)).fetchone()
       pet11 = round(int(pet11[0]))
       summ = 50
       if ivent == 1:
          if egg >= 50:
             if pet11 == 0:
                await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы обменяли свои пасхальные яйца на питомца \"Пасхальный кролик\"! {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET egg = {egg - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET pet11 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()   
             if pet11 == 1:
                await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы уже забрали данную награду! {rloser}", parse_mode='html')
          if egg < 50:
             await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно пасхальных яиц! {rloser}", parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, пасхальный ивент еще не начался или уже закончен! {rloser}", parse_mode='html')

    if message.text.lower() in ["ивент забрать 5", "Ивент забрать 5"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = msg.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       egg = cursor.execute("SELECT egg from users where user_id = ?",(message.from_user.id,)).fetchone()
       egg = int(egg[0])
       status = cursor.execute("SELECT status from users where user_id = ?",(message.from_user.id,)).fetchone()
       status = str(status[0])
       stat = "Пасха 2022"
       summ = 250
       if ivent == 1:
          if egg >= 250:
             if status == "Игрок":
                await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы обменяли свои пасхальные яйца на статус \"Пасха 2022\"! {rwin}", parse_mode='html')
                cursor.execute(f'UPDATE users SET egg = {egg - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET status = \"{stat}\" WHERE user_id = "{user_id}"') 
                connect.commit()   
             if status == "Пасха 2022":
                await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы уже забрали данную награду! {rloser}", parse_mode='html')
          if egg < 250:
             await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно пасхальных яиц! {rloser}", parse_mode='html')
       if ivent == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, пасхальный ивент еще не начался или уже закончен! {rloser}", parse_mode='html')

    if message.text.lower() in ["начать ивент", "Начать ивент"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == "Owner":
          await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно включили пасхальный ивент! {rwin}", parse_mode='html')
          cursor.execute(f"UPDATE bot SET ivent = {1}")
          connect.commit()   
       if user_status[0] == "Player":
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь владельцем бота!", parse_mode='html')

    if message.text.lower() in ["закончить ивент", "Закончить ивент"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       ivent = cursor.execute("SELECT ivent from bot").fetchone()
       ivent = int(ivent[0])
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone() 
       if user_status[0] == "Owner":
          await bot.send_message(message.chat.id, f"🐰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно отключили пасхальный ивент! {rwin}", parse_mode='html')
          cursor.execute(f"UPDATE bot SET ivent = {0}")
          connect.commit() 
       if user_status[0] == "Player":
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь владельцем бота!", parse_mode='html')

    if message.text.lower() in ["NexxlfPassword", "nexxlfpassword"]:
       await bot.send_message(message.chat.id, f'Описание пиздец', parse_mode='html')

    if message.text.lower() in ["nexxlfkwest", "NexxlfKwest"]:
       await bot.send_message(message.chat.id, f'Вопрос: как называлась первая версия бота ? \n Ответ писать @rave_admin', parse_mode='html')

###########################################ЭЛЕКТРОСТАНЦИИ###########################################
    if message.text.lower() in ["электростанции", "Электростанции"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, доступные для покупки электростанции:\n🎡 1. Grand Coulee |  1⚡️/час (20.000.000$)\n🎡 2. Xiluodu |  5⚡️/час (600.000.000$)\n🎡 3. Three Gorges Dam | 25⚡️/час (6.500.000.000$)\n🎡 4. Xiangjiaba | 450⚡️/час (800.000.000.000$)\n🎡 5. Itaipu Dam | 3.000⚡️/час (7.500.000.000.000$)\n\n🛒 Для покупки электростанции введите - [Купить электростанцию][номер]\n\n🛒 Для покупки турбин для электростанции введите - [Купить турбины][кол-во]", parse_mode='html')
    
    if message.text.lower() in ["купить электростанцию 1", "Купить электростанцию 1"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 20000000
       c = 1
       farms = farm1 + farm2 + farm3 + farm4 + farm5
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if farms == 0:
          if farm1 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Grand Coulee за 20.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farm1 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farm1 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная электростанция! {rloser}", parse_mode='html')     
             return
       if farms == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть электростанция! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить электростанцию 2", "Купить электростанцию 2"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 600000000
       c = 1
       farms = farm1 + farm2 + farm3 + farm4 + farm5
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if farms == 0:
          if farm2 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Xiluodu за 600.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farm2 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farm2 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная электростанция! {rloser}", parse_mode='html')     
             return
       if farms == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть электростанция! {rloser}", parse_mode='html') 

    if message.text.lower() in ["купить электростанцию 3", "Купить электростанцию 3"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 6500000000
       c = 1
       farms = farm1 + farm2 + farm3 + farm4 + farm5
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if farms == 0:
          if farm3 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Three Gorges Dam за 6.500.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farm3 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farm3 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная электростанция! {rloser}", parse_mode='html')     
             return
       if farms == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть электростанция! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить электростанцию 4", "Купить электростанцию 4"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 800000000000
       c = 1
       farms = farm1 + farm2 + farm3 + farm4 + farm5
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if farms == 0:
          if farm4 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Xiangjiaba Dam за 800.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farm4 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farm4 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная электростанция! {rloser}", parse_mode='html')     
             return
       if farms == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть электростанция! {rloser}", parse_mode='html')    

    if message.text.lower() in ["купить электростанцию 5", "Купить электростанцию 5"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       msg = message
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 7500000000000
       c = 1
       farms = farm1 + farm2 + farm3 + farm4 + farm5
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       if farms == 0:
          if farm5 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили Itaipu Dam за 7.500.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farm5 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farm5 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная электростанция! {rloser}", parse_mode='html')     
             return
       if farms == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть электростанция! {rloser}", parse_mode='html')    

    if message.text.lower() in ["продать электростанцию", "Продать электростанцию"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       farms = farm1 + farm2 + farm3 + farm4 + farm5 
       if farms == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету электростанции! {rloser}", parse_mode='html')
       if farm1 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою электростанцию за 15.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 15000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farm1 = {0} WHERE user_id = "{user_id}"')  
          cursor.execute(f'UPDATE users SET generator = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if farm2 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою электростанцию за 450.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 450000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farm2 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET generator = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if farm3 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою электростанцию за 4.875.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 4875000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farm3 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET generator = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if farm4 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою электростанцию за 600.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 600000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farm4 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET generator = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if farm5 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою электростанцию за 5.625.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 5625000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farm5 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET generator = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 

    if message.text.lower() in ["моя электростанция", "Моя электростанция"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       generator = cursor.execute("SELECT generator from users where user_id = ?",(message.from_user.id,)).fetchone()
       generator = int(generator[0])
       farm_coin = cursor.execute("SELECT farm_coin from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm_coin = int(farm_coin[0])
       farm_coin_get = '{0:,}'.format(farm_coin).replace(',', '.')
       generator1 = '{0:,}'.format(generator * 1).replace(',', '.')
       generator2 = '{0:,}'.format(generator * 5).replace(',', '.')
       generator3 = '{0:,}'.format(generator * 25).replace(',', '.')
       generator4 = '{0:,}'.format(generator * 450).replace(',', '.')
       generator5 = '{0:,}'.format(generator * 3000).replace(',', '.')
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       farms = farm1 + farm2 + farm3 + farm4 + farm5 
       if farms == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету электростанции! {rloser}", parse_mode='html')
       if farm1 == 1:
          await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваша электростанция:\nℹ️ Название электростанции: Grand Coulee\n💸 Прибыль: {generator1}⚡️/чаc\n💼 Турбин: {generator}/15\n💰 На счету: {farm_coin_get} ⚡️", parse_mode='html')
       if farm2 == 1:
          await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваша электростанция:\nℹ️ Название электростанции: Xiluodu\n💸 Прибыль: {generator2}⚡️/чаc\n💼 Турбин: {generator}/15\n💰 На счету: {farm_coin_get} ⚡️", parse_mode='html')
       if farm3 == 1:
          await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваша электростанция:\nℹ️ Название электростанции: Three Gorges Dam\n💸 Прибыль: {generator3}⚡️/чаc\n💼 Турбин: {generator}/15\n💰 На счету: {farm_coin_get} ⚡️", parse_mode='html')
       if farm4 == 1:
          await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваша электростанция:\nℹ️ Название электростанции: Xiangjiaba\n💸 Прибыль: {generator4}⚡️/чаc\n💼 Турбин: {generator}/15\n💰 На счету: {farm_coin_get} ⚡️", parse_mode='html')
       if farm5 == 1:
          await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваша электростанция:\nℹ️ Название электростанции: Itaipu Dam\n💸 Прибыль: {generator5}⚡️/чаc\n💼 Турбин: {generator}/15\n💰 На счету: {farm_coin_get} ⚡️", parse_mode='html')

    if message.text.startswith("купить турбины"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       generator = cursor.execute("SELECT generator from users where user_id = ?",(message.from_user.id,)).fetchone()
       generator = int(generator[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       farms = farm1 + farm2 + farm3 + farm4 + farm5 
       summ = int(msg.text.split()[2])
       check = generator + summ

       check_balance1 = summ * 20000000
       check_balance2 = summ * 600000000
       check_balance3 = summ * 6500000000
       check_balance4 = summ * 800000000000
       check_balance5 = summ * 7500000000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число турбин! {rloser}", parse_mode='html')
          return
       if farms == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету электростанции! {rloser}", parse_mode='html')
          return
       if check > 15:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить больше 15 турбин! {rloser}", parse_mode='html')
          return
       if check <= 15:
          if farm1 == 1:
             if check_balance1 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance1 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farm2 == 1:
             if check_balance2 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance2 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farm3 == 1:
             if check_balance3 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance3 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farm4 == 1:
             if check_balance4 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance4 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farm5 == 1:
             if check_balance5 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance5 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return

    if message.text.startswith("Купить турбины"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       generator = cursor.execute("SELECT generator from users where user_id = ?",(message.from_user.id,)).fetchone()
       generator = int(generator[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       farms = farm1 + farm2 + farm3 + farm4 + farm5 
       summ = int(msg.text.split()[2])
       check = generator + summ

       check_balance1 = summ * 20000000
       check_balance2 = summ * 600000000
       check_balance3 = summ * 6500000000
       check_balance4 = summ * 800000000000
       check_balance5 = summ * 7500000000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число турбин! {rloser}", parse_mode='html')
          return
       if farms == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету электростанции! {rloser}", parse_mode='html')
          return
       if check > 15:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить больше 15 турбин! {rloser}", parse_mode='html')
          return
       if check <= 15:
          if farm1 == 1:
             if check_balance1 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance1 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farm2 == 1:
             if check_balance2 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance2 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farm3 == 1:
             if check_balance3 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance3 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farm4 == 1:
             if check_balance4 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance4 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farm5 == 1:
             if check_balance5 <= balance:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} турбин за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance5 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return

    if message.text.startswith("электростанция снять"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       generator = cursor.execute("SELECT generator from users where user_id = ?",(message.from_user.id,)).fetchone()
       generator = int(generator[0])
       farm_coin = cursor.execute("SELECT farm_coin from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm_coin = int(farm_coin[0])
       energy = cursor.execute("SELECT energy from users where user_id = ?",(message.from_user.id,)).fetchone()
       energy = int(energy[0])
       summ = int(msg.text.split()[2])
       summ_get = '{0:,}'.format(summ).replace(',', '.')
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       farms = farm1 + farm2 + farm3 + farm4 + farm5 
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете снять отрицательное число энергии! {rloser}", parse_mode='html') 
          return
       if farms == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету электростанции! {rloser}", parse_mode='html')
       if farm1 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции!", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farm2 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farm3 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции!", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farm4 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции!", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farm5 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции!", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 

    if message.text.startswith("Электростанция снять"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       generator = cursor.execute("SELECT generator from users where user_id = ?",(message.from_user.id,)).fetchone()
       generator = int(generator[0])
       farm_coin = cursor.execute("SELECT farm_coin from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm_coin = int(farm_coin[0])
       energy = cursor.execute("SELECT energy from users where user_id = ?",(message.from_user.id,)).fetchone()
       energy = int(energy[0])
       summ = int(msg.text.split()[2])
       summ_get = '{0:,}'.format(summ).replace(',', '.')
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       farms = farm1 + farm2 + farm3 + farm4 + farm5 
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете снять отрицательное число энергии! {rloser}", parse_mode='html') 
          return
       if farms == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету электростанции! {rloser}", parse_mode='html')
       if farm1 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции!", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farm2 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции!", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farm3 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции!", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farm4 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции!", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farm5 == 1:
          if summ > farm_coin:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей электростанции недостаточно энергии! {rloser}", parse_mode='html') 
          if summ <= farm_coin:
             await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}⚡️ с вашей электростанции!", parse_mode='html')
             cursor.execute(f'UPDATE users SET farm_coin = {farm_coin - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET energy = {energy + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 

    if message.text.lower() in ["Энергия курс", "энергия курс"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       chat_id = message.chat.id
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, на данный момент курс 1⚡  составляет - 10.000$", parse_mode='html') 

    if message.text.startswith("продать энергию"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       energy = cursor.execute("SELECT energy from users where user_id = ?",(message.from_user.id,)).fetchone()
       energy = int(energy[0])
       summ = int(msg.text.split()[2])
       summ_get = '{0:,}'.format(summ).replace(',', '.')
       price = '{0:,}'.format(summ * 10000).replace(',', '.')
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете продать отрицательное число энергии! {rloser}", parse_mode='html') 
          return
       if summ > energy:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно энергии! {rloser}", parse_mode='html') 
       if summ <= energy:
          await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ_get}⚡️ за {price}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + (summ * 10000)} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET energy = {energy - summ} WHERE user_id = "{user_id}"') 
          connect.commit() 

    if message.text.startswith("Продать энергию"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       energy = cursor.execute("SELECT energy from users where user_id = ?",(message.from_user.id,)).fetchone()
       energy = int(energy[0])
       summ = int(msg.text.split()[2])
       summ_get = '{0:,}'.format(summ).replace(',', '.')
       price = '{0:,}'.format(summ * 10000).replace(',', '.')
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете продать отрицательное число энергии! {rloser}", parse_mode='html') 
          return
       if summ > energy:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно энергии! {rloser}", parse_mode='html') 
       if summ <= energy:
          await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ_get}⚡️ за {price}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + (summ * 10000)} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET energy = {energy - summ} WHERE user_id = "{user_id}"') 
          connect.commit() 
 
    if message.text.startswith("Продать турбины"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       generator = cursor.execute("SELECT generator from users where user_id = ?",(message.from_user.id,)).fetchone()
       generator = int(generator[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       farms = farm1 + farm2 + farm3 + farm4 + farm5 
       summ = int(msg.text.split()[2])
       check = generator + summ

       check_balance1 = summ * 15000000
       check_balance2 = summ * 400000000
       check_balance3 = summ * 4875000000
       check_balance4 = summ * 600000000000
       check_balance5 = summ * 5625000000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число турбин! {rloser}", parse_mode='html')
          return
       if farms == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету электростанции! {rloser}", parse_mode='html')
          return
       if summ > 15:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете продать больше 15 турбин! {rloser}", parse_mode='html')
          return
       if summ <= 15:
          if farm1 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return
          if farm2 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return
          if farm3 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return
          if farm4 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return
          if farm5 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return
    
    if message.text.startswith("продать турбины"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farm1 = cursor.execute("SELECT farm1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm1 = int(farm1[0])
       farm2 = cursor.execute("SELECT farm2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm2 = int(farm2[0])
       farm3 = cursor.execute("SELECT farm3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm3 = int(farm3[0])
       farm4 = cursor.execute("SELECT farm4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm4 = int(farm4[0])
       farm5 = cursor.execute("SELECT farm5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farm5 = int(farm5[0])
       generator = cursor.execute("SELECT generator from users where user_id = ?",(message.from_user.id,)).fetchone()
       generator = int(generator[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       
       farms = farm1 + farm2 + farm3 + farm4 + farm5 
       summ = int(msg.text.split()[2])
       check = generator + summ

       check_balance1 = summ * 15000000
       check_balance2 = summ * 400000000
       check_balance3 = summ * 4875000000
       check_balance4 = summ * 600000000000
       check_balance5 = summ * 5625000000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число турбин! {rloser}", parse_mode='html')
          return
       if farms == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету электростанции! {rloser}", parse_mode='html')
          return
       if summ > 15:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете продать больше 15 турбин! {rloser}", parse_mode='html')
          return
       if summ <= 15:
          if farm1 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return
          if farm2 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return
          if farm3 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return
          if farm4 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return
          if farm5 == 1:
             if summ <= generator:
                await bot.send_message(message.chat.id, f"🎡 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} турбин за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET generator = {generator - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > generator:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно турбин! {rloser}", parse_mode='html')
                return

    if message.text.lower() in ["Инвентарь", "инвентарь"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       chat_id = message.chat.id
       energy = cursor.execute("SELECT energy from users where user_id = ?", (message.from_user.id,)).fetchone()
       energy = round(int(energy[0]))
       energy_up = '{:,}'.format(energy)
       ore1 = cursor.execute("SELECT ore1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       ore1 = round(int(ore1[0]))
       ore1_up = '{0:,}'.format(ore1).replace(',', '.')
       ore2 = cursor.execute("SELECT ore2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       ore2 = round(int(ore2[0]))
       ore2_up = '{0:,}'.format(ore2).replace(',', '.')
       ore3 = cursor.execute("SELECT ore3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       ore3 = round(int(ore3[0]))
       ore3_up = '{0:,}'.format(ore3).replace(',', '.')
       ore4 = cursor.execute("SELECT ore4 from users where user_id = ?", (message.from_user.id,)).fetchone()
       ore4 = round(int(ore4[0]))
       ore4_up = '{0:,}'.format(ore4).replace(',', '.')
       ore5 = cursor.execute("SELECT ore5 from users where user_id = ?", (message.from_user.id,)).fetchone()
       ore5 = round(int(ore5[0]))
       ore5_up = '{0:,}'.format(ore5).replace(',', '.')
       ore6 = cursor.execute("SELECT ore6 from users where user_id = ?", (message.from_user.id,)).fetchone()
       ore6 = round(int(ore6[0]))
       ore6_up = '{0:,}'.format(ore6).replace(',', '.')
       ore7 = cursor.execute("SELECT ore7 from users where user_id = ?", (message.from_user.id,)).fetchone()
       ore7 = round(int(ore7[0]))
       ore7_up = '{0:,}'.format(ore7).replace(',', '.')
       ore8 = cursor.execute("SELECT ore8 from users where user_id = ?", (message.from_user.id,)).fetchone()
       ore8 = round(int(ore8[0]))
       ore8_up = '{0:,}'.format(ore8).replace(',', '.')
       checking = cursor.execute("SELECT checking from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking = round(int(checking[0]))
       if checking == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking1 = cursor.execute("SELECT checking1 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking1 = round(int(checking1[0]))
       if checking1 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking2 = cursor.execute("SELECT checking2 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking2 = round(int(checking2[0]))
       if checking2 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       checking3 = cursor.execute("SELECT checking3 from users where user_id = ?", (message.from_user.id,)).fetchone()
       checking3 = round(int(checking3[0]))
       inv = energy + ore1 + ore2 + ore3 + ore4 + ore5 + ore6 + ore7 + ore8
       if energy >= 1:
          e = f"⚡ Энергия - {energy_up} шт.\n"
       if energy == 0:
          e = ""
       if ore1 >= 1:
          or1 = f"⚫️ Уголь - {ore1_up} шт.\n"
       if ore1 == 0:
          or1 = ""
       if ore2 >= 1:
          or2 = f"🪙 Железо - {ore2_up} шт.\n"
       if ore2 == 0:
          or2 = ""
       if ore3 >= 1:
          or3 = f"🌕 Золото - {ore3_up} шт.\n"
       if ore3 == 0:
          or3 = ""
       if ore4 >= 1:
          or4 = f"💎 Алмазы - {ore4_up} шт.\n"
       if ore4 == 0:
          or4 = ""
       if ore5 >= 1:
          or5 = f"🏮 Рубины - {ore5_up} шт.\n"
       if ore5 == 0:
          or5 = ""
       if ore6 >= 1:
          or6 = f"🍀 Изумруды - {ore6_up} шт.\n"
       if ore6 == 0:
          or6 = ""
       if ore7 >= 1:
          or7 = f"💠 Сапфиры - {ore7_up} шт.\n"
       if ore7 == 0:
          or7 = ""
       if ore8 >= 1:
          or8 = f"🌌 Материя - {ore8_up} шт.\n"
       if ore8 == 0:
          or8 = ""
       if inv == 0:
          e = f"😔 Ваш инвентарь пуст!"
       if checking3 == 1:
          await bot.send_message(chat_id, f'ℹ | Дождитесь окончания игры! {rloser}', parse_mode='html')
          return
       await bot.send_message(message.chat.id, f"📦 | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш инвентарь:\n{e}{or1}{or2}{or3}{or4}{or5}{or6}{or7}{or8}", parse_mode='html') 
  
    if message.text.lower() in ["Брак", "брак"]:
       data = await get_rang(message)
       if data is None:
          return await message.reply(f"🚫 <b>Не найден в базе данных.</b>\n\n"
                                   f"/start в лс у бота!")
       user = message.from_user
       usid = user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(usid,)).fetchone()
       user_name = user_name[0]
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          rid = replyuser.id
          ruser_name = cursor.execute("SELECT user_name from users where user_id = ?",(rid,)).fetchone()
          ruser_name = ruser_name[0] 
          if data[91] == 0:
             if replyuser.id == user.id:
                return await message.reply(f"ℹ️ | Вы не можете сделать брак с самим собой.")
             replydata = await reply_get_rang(message)
             if replydata[91] == 0:
                marry_me.append(user.id)
                marry_rep.append(replyuser.id)
                await bot.send_message(message.chat.id, f"💍 <a href='tg://user?id={rid}'>{ruser_name}</a>, минуточку внимания.\n💖 <a href='tg://user?id={usid}'>{user_name}</a> сделал вам предложение руки и сердца.\n😍 Принять решение можно нажав на одну из кнопок ниже.",  parse_mode='html' , reply_markup=kb.button_marry)
             else:
                replyuser = reply.from_user
                rid = replyuser.id
                repuser_name = cursor.execute("SELECT user_name from users where user_id = ?",(rid,)).fetchone()
                repuser_name = repuser_name[0]
                marry = cursor.execute("SELECT marry FROM users WHERE user_id=?", (rid,)).fetchall()
                marry1 = int(marry[0][0])
                m_name = cursor.execute("SELECT user_name from users where user_id = ?",(marry1,)).fetchone()
                m_name = m_name[0]
                return await message.reply(f"ℹ️ | <a href='tg://user?id={rid}'>{repuser_name}</a> уже находится в браке с <a href='tg://user?id={marry1}'>{m_name}</a>!",  parse_mode='html')
          else:
            user = message.from_user
            usid = user.id
            marry = cursor.execute("SELECT marry FROM users WHERE user_id=?", (usid,)).fetchall()
            marry1 = int(marry[0][0])
            m_name = cursor.execute("SELECT user_name from users where user_id = ?",(marry1,)).fetchone()
            m_name = m_name[0]
            return await message.reply(f"ℹ️ | Вы уже находитесь в браке с <a href='tg://user?id={marry1}'>{m_name}</a>!",  parse_mode='html')

    if message.text.lower() in ["Развод", "развод"]:
       data = await get_rang(message)
       if data is None:
          return await message.reply(f"🚫 <b>Не найден в базе данных.</b>\n\n"
                                     f"/start в лс у бота!")
       user = message.from_user
       name = quote_html(user.full_name)
       if data[91] == 0:
          return await message.reply(f"ℹ️ Вы не состоите не с кем в браке!")
       else:
          marry = cursor.execute("SELECT marry FROM users WHERE user_id=?", (user.id,)).fetchall()
          marred = await bot.get_chat(str(marry[0][0]))
          mname = quote_html(marred.full_name)
          divorce_me.append(user.id)
          divorce_rep.append(marred.id)
          await bot.send_message(message.chat.id, f"📝 Убедить что вы согласны разводится.\n💔 Принять решение можно нажав на одну из кнопок ниже.",  parse_mode='html', reply_markup=kb.button_divorce)

    if message.text.lower() in ["Мой брак", "мой брак"]:
       data = await get_rang(message)
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       if data[91] == 0:
          await bot.send_message(message.chat.id, f"💔 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы пока не состоите ни с кем в браке",  parse_mode='html')
       else:
          marry = cursor.execute("SELECT marry FROM users WHERE user_id = ?",(message.from_user.id,)).fetchone()
          marry = int(marry[0])
          mname = cursor.execute("SELECT user_name FROM users WHERE user_id=?", (marry,)).fetchone()
          mname = mname[0]

          get = cursor.execute("SELECT marry_date FROM users WHERE user_id=?", (message.from_user.id,)).fetchall()
          date_time = datetime.fromisoformat(get[0][0])
          times = date_time.strftime( "%d.%m.%Y %H:%M:%S" ) 
          await bot.send_message(message.chat.id, f"❤️ Брак между <a href='tg://user?id={user_id}'>{user_name}</a> и <a href='tg://user?id={marry}'>{mname}</a>:\n📆 Зарегистрирован: {times}",  parse_mode='html')

    if message.text.lower() in ["Шахта", "шахта"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               #уголь, железо, золото, алмазы, рубины, изумруды, сапфиры, материя
       await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>, это шахта. Здесь вы сможете добыть ресурсы для дальнейшей продажи. На шахте можно добыть - уголь, железо, золото, алмазы, рубины, изумруды, сапфиры, материя. Чтобы копать вам понадобиться энергия.\n\n✅ Как начать работать и добывать ресурсы? Используйте команды: «копать уголь», «копать железо», «копать золото», «копать алмазы», «копать рубины», «копать изумруды», «копать сапфиры», «копать материю».\n\n♻️ Как продавать ресурсы? Используйте команды: «продать уголь», «продать железо», «продать золото», «продать алмазы», «продать рубины», «продать изумруды», «продать сапфиры», «продать материю».\n\n📜 Как посмотреть свою статистику? Используйте команду "Моя шахта", вы сможете просмотреть ваш опыт, сколько не хватает до следующего уровня, а также какая следующая стадия.', parse_mode='html')

    if message.text.lower() in ["Копать уголь", "копать уголь"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id    
       ore1 = cursor.execute("SELECT ore1 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone() 
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       ore1 = int(ore1[0])
       energy = int(energy[0])
       expe = int(expe[0])
       expe2 = '{0:,}'.format(expe + 1).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       random_ore = random.randint(20, 100)
       if energy >= 1:
          await asyncio.sleep(2)
          await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>,  +{random_ore} угля.\n💡 Энергия: {energy - 1}, опыт: {expe2}', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore1 = {ore1 + random_ore} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET expe = {expe + 1} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET ener = {energy - 1} WHERE user_id = "{user_id}"') 
          connect.commit()
       if energy == 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас закончилась энергия! {rloser}', parse_mode='html')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            

    if message.text.lower() in ["Копать железо", "копать железо"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore2 = cursor.execute("SELECT ore2 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone() 
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       ore2 = int(ore2[0])
       energy = int(energy[0])
       expe = int(expe[0])
       expe2 = '{0:,}'.format(expe + 5).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       random_ore = random.randint(20, 50)
       if expe <= 99:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, чтобы копать железо вам требуется 100 опыта! {rloser}', parse_mode='html')
          return

       if energy >= 1:
          await asyncio.sleep(2)
          await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>,  +{random_ore} железо.\n💡 Энергия: {energy - 1}, опыт: {expe2}', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore2 = {ore2 + random_ore} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET expe = {expe + 5} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET ener = {energy - 1} WHERE user_id = "{user_id}"') 
          connect.commit()
       if energy == 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас закончилась энергия! {rloser}', parse_mode='html')
   
    if message.text.lower() in ["Копать золото", "копать золото"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore3 = cursor.execute("SELECT ore3 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone() 
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       ore3 = int(ore3[0])
       energy = int(energy[0])
       expe = int(expe[0])
       expe2 = '{0:,}'.format(expe + 10).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       random_ore = random.randint(15, 30)
       if expe <= 499:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, чтобы копать золото вам требуется 500 опыта! {rloser}', parse_mode='html')
          return
          
       if energy >= 1:
          await asyncio.sleep(2)
          await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>,  +{random_ore} золота.\n💡 Энергия: {energy - 1}, опыт: {expe2}', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore3 = {ore3 + random_ore} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET expe = {expe + 10} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET ener = {energy - 1} WHERE user_id = "{user_id}"') 
          connect.commit()
       if energy == 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас закончилась энергия! {rloser}', parse_mode='html')   

    if message.text.lower() in ["Копать алмазы", "копать алмазы"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore4 = cursor.execute("SELECT ore4 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone() 
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       ore4 = int(ore4[0])
       energy = int(energy[0])
       expe = int(expe[0])
       expe2 = '{0:,}'.format(expe + 15).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       random_ore = random.randint(5, 20)
       if expe <= 999:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, чтобы копать алмазы вам требуется 1000 опыта! {rloser}', parse_mode='html')
          return
          
       if energy >= 1: 
          await asyncio.sleep(2)
          await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>,  +{random_ore} алмазов.\n💡 Энергия: {energy - 1}, опыт: {expe2}', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore4 = {ore4 + random_ore} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET expe = {expe + 15} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET ener = {energy - 1} WHERE user_id = "{user_id}"') 
          connect.commit()
       if energy == 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас закончилась энергия! {rloser}', parse_mode='html')   

    if message.text.lower() in ["Копать рубины", "копать рубины"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore5 = cursor.execute("SELECT ore5 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone() 
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       ore5 = int(ore5[0])
       energy = int(energy[0])
       expe = int(expe[0])
       expe2 = '{0:,}'.format(expe + 20).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       random_ore = random.randint(1, 15)
       if expe <= 9999:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, чтобы копать рубины вам требуется 10000 опыта! {rloser}', parse_mode='html')
          return
          
       if energy >= 1:
          await asyncio.sleep(2)
          await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>,  +{random_ore} рубинов.\n💡 Энергия: {energy - 1}, опыт: {expe2}', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore5 = {ore5 + random_ore} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET expe = {expe + 20} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET ener = {energy - 1} WHERE user_id = "{user_id}"') 
          connect.commit()
       if energy == 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас закончилась энергия! {rloser}', parse_mode='html')   

    if message.text.lower() in ["Копать изумруды", "копать изумруды"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore6 = cursor.execute("SELECT ore6 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone() 
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       ore6 = int(ore6[0])
       energy = int(energy[0])
       expe = int(expe[0])
       expe2 = '{0:,}'.format(expe + 25).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       random_ore = random.randint(1, 10)
       if expe <= 24999:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, чтобы копать изумруды вам требуется 25000 опыта! {rloser}', parse_mode='html')
          return
          
       if energy >= 1:
          await asyncio.sleep(2)
          await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>,  +{random_ore} изумрудов.\n💡 Энергия: {energy - 1}, опыт: {expe2}', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore6 = {ore6 + random_ore} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET expe = {expe + 25} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET ener = {energy - 1} WHERE user_id = "{user_id}"') 
          connect.commit()

       if energy == 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас закончилась энергия! {rloser}', parse_mode='html') 

    if message.text.lower() in ["Копать сапфиры", "копать сапфиры"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore7 = cursor.execute("SELECT ore7 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone() 
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       ore7 = int(ore7[0])
       energy = int(energy[0])
       expe = int(expe[0])
       expe2 = '{0:,}'.format(expe + 35).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       random_ore = random.randint(1, 7)
       if expe <= 49999:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, чтобы копать сапфиры вам требуется 50000 опыта! {rloser}', parse_mode='html')
          return
          
       if energy >= 1:
          await asyncio.sleep(2)
          await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>,  +{random_ore} сапфиров.\n💡 Энергия: {energy - 1}, опыт: {expe2}', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore7 = {ore7 + random_ore} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET expe = {expe + 35} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET ener = {energy - 1} WHERE user_id = "{user_id}"') 
          connect.commit()

       if energy == 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас закончилась энергия! {rloser}', parse_mode='html') 

    if message.text.lower() in ["Копать материю", "копать материю"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore8 = cursor.execute("SELECT ore8 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone() 
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       ore8 = int(ore8[0])
       energy = int(energy[0])
       expe = int(expe[0])
       expe2 = '{0:,}'.format(expe + 50).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       random_ore = random.randint(1, 5)
       if expe <= 99999:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, чтобы копать материю вам требуется 100000 опыта! {rloser}', parse_mode='html')
          return
          
       if energy >= 1:
          await asyncio.sleep(2)
          await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>,  +{random_ore} материи.\n💡 Энергия: {energy - 1}, опыт: {expe2}', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore8 = {ore8 + random_ore} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET expe = {expe + 50} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET ener = {energy - 1} WHERE user_id = "{user_id}"') 
          connect.commit()

       if energy == 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас закончилась энергия! {rloser}', parse_mode='html') 

    if message.text.lower() in ["Курс руды", "курс руды"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id  
       await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>, курс руды:\n⚫️ 1 уголь - 50.000$\n🪙 1 железо - 230.000$\n🌕 1 золото - 1.000.000$\n💎 1 алмаз - 116.000.000$\n🏮 1 рубины - 217.000.000$\n🍀 1 изумруд - 461.000.000$\n💠 1 сапфир - 792.000.000$\n🌌 1 материя - 8.000.000.000$', parse_mode='html')

    if message.text.startswith("продать уголь"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id  
       msg = message   
       ore1 = cursor.execute("SELECT ore1 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore1 = int(ore1[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 50000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore1:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} угля за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore1 = {ore1 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore1:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.startswith("продать железо"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id   
       msg = message  
       ore2 = cursor.execute("SELECT ore2 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore2 = int(ore2[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 230000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore2:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} железа за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore2 = {ore2 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore2:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')
      
    if message.text.startswith("продать золото"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore3 = cursor.execute("SELECT ore3 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore3 = int(ore3[0])
       msg = message
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 1000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore3:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} золота за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore3 = {ore3 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore3:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.startswith("продать алмазы"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore4 = cursor.execute("SELECT ore4 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore4 = int(ore4[0])
       msg = message
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 116000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore4:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} алмазов за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore4 = {ore4 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore4:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.startswith("продать рубины"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore5 = cursor.execute("SELECT ore5 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore5 = int(ore5[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       msg = message
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 217000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore5:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} рубинов за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore5 = {ore5 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore5:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.startswith("продать изумруды"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore6 = cursor.execute("SELECT ore6 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore6 = int(ore6[0])
       msg = message
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 461000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore6:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} изумрудов за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore6 = {ore6 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore6:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')
  
    if message.text.startswith("продать сапфиры"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore7 = cursor.execute("SELECT ore7 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore7 = int(ore7[0])
       msg = message
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 792000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore7:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} сапфиров за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore7 = {ore7 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore7:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html') 

    if message.text.startswith("продать материю"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore8 = cursor.execute("SELECT ore8 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore8 = int(ore8[0])
       msg = message
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 8000000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore8:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} материи за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore8 = {ore8 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore8:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.startswith("Продать уголь"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id 
       msg = message    
       ore1 = cursor.execute("SELECT ore1 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore1 = int(ore1[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 50000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore1:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} угля за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore1 = {ore1 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore1:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.startswith("Продать железо"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id
       msg = message     
       ore2 = cursor.execute("SELECT ore2 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore2 = int(ore2[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 230000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore2:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} железа за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore2 = {ore2 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore2:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')
      
    if message.text.startswith("Продать золото"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       msg = message
       ore3 = cursor.execute("SELECT ore3 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore3 = int(ore3[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 1000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore3:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} золота за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore3 = {ore3 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore3:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.startswith("Продать алмазы"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore4 = cursor.execute("SELECT ore4 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore4 = int(ore4[0])
       msg = message
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 116000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore4:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} алмазов за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore4 = {ore4 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore4:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.startswith("Продать рубины"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore5 = cursor.execute("SELECT ore5 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore5 = int(ore5[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       msg = message
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 217000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore5:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} рубинов за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore5 = {ore5 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore5:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.startswith("Продать изумруды"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore6 = cursor.execute("SELECT ore6 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore6 = int(ore6[0])
       msg = message
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 461000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore6:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} изумрудов за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore6 = {ore6 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore6:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')
  
    if message.text.startswith("Продать сапфиры"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore7 = cursor.execute("SELECT ore7 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore7 = int(ore7[0])
       msg = message
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 792000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore7:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} сапфиров за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore7 = {ore7 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore7:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html') 

    if message.text.startswith("Продать материю"):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id     
       ore8 = cursor.execute("SELECT ore8 from users where user_id = ?",(message.from_user.id,)).fetchone()  
       ore8 = int(ore8[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()  
       balance = int(balance[0])
       msg = message
       summ = int(msg.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       price = summ * 8000000000
       price2 = '{0:,}'.format(price).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rwin = random.choice(win)
       rloser = random.choice(loser)
       if summ <= 0:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, вы не можете продать отрацательное число! {rloser}', parse_mode='html')
          return          
       if summ <= ore8:
          await bot.send_message(message.chat.id, f'💰 | <a href="tg://user?id={user_id}">{user_name}</a>, вы успешно продали {summ2} материи за {price2}$!', parse_mode='html')
          cursor.execute(f'UPDATE users SET ore8 = {ore8 - summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET balance = {balance + price} WHERE user_id = "{user_id}"') 
          connect.commit()
       if summ > ore8:
          await bot.send_message(message.chat.id, f'ℹ | <a href="tg://user?id={user_id}">{user_name}</a>, у вас недостаточно руды для продажи! {rloser}', parse_mode='html')

    if message.text.lower() in ["Моя шахта", "моя шахта"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id 
       energy = cursor.execute("SELECT ener from users where user_id = ?",(message.from_user.id,)).fetchone() 
       expe = cursor.execute("SELECT expe from users where user_id = ?",(message.from_user.id,)).fetchone()
       energy = int(energy[0])
       expe = int(expe[0]) 
       expe2 = '{0:,}'.format(expe).replace(',', '.')
       if expe in range(0,99):
          lvl = 'Уголь ⚫'    
       if expe in range(100,499):
          lvl = 'Железо ⛓'    
       if expe in range(500,999):
          lvl = 'Золото 🌕'   
       if expe in range(1000,9999):
          lvl = 'Алмазы 💎' 
       if expe in range(10000,24999):
          lvl = 'Рубины 🏮' 
       if expe in range(25000,49999):
          lvl = 'Изумруды 🍀' 
       if expe in range(50000,99999):
          lvl = 'Сапфиры 💠'   
       if expe >= 100000:
          lvl = 'Материя 🌌' 

       if expe in range(0,99):
          lvl_soon = 'Железо ⛓'    
       if expe in range(100,499):
          lvl_soon = 'Золото 🌕'    
       if expe in range(500,999):
          lvl_soon = 'Алмазы 💎'   
       if expe in range(1000,9999):
          lvl_soon = 'Рубины 🏮' 
       if expe in range(10000,24999):
          lvl_soon = 'Изумруды 🍀' 
       if expe in range(25000,49999):
          lvl_soon = 'Сапфиры 💠' 
       if expe in range(50000,99999):
          lvl_soon = 'Материя 🌌'   
       if expe >= 100000:
          lvl_soon = '???'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      #уголь, железо, золото, алмазы, рубины, изумруды, сапфиры, материя
       await bot.send_message(message.chat.id, f'<a href="tg://user?id={user_id}">{user_name}</a>, это ваш профиль шахты:\n🏆 Опыт: {expe2}\n⚡️ Энергия: {energy}\n⛏ Ваш уровень: {lvl}\n➡️ Следующий уровень: {lvl_soon}', parse_mode='html')

    if message.text.lower() in ["Выбрать пол", "выбрать пол"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await bot.send_message(message.chat.id, f'👤 | <a href="tg://user?id={user_id}">{user_name}</a>, выбрать свой пол можно нажав на одну из кнопок ниже.', parse_mode='html', reply_markup=kb.gender)

    if message.text.lower() in ["Фермы", "фермы"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, доступные для покупки майнинг фермы:\n🧰 1. TI-Miner 4฿/час (5.000.000$)\n🧰 2. Saturn 12฿/час (60.000.000$)\n🧰 3. Calisto 64฿/час (650.000.000$)\n🧰 4. HashMiner 650฿/час (80.000.000.000$)\n🧰 5. MegaWatt 3.500฿/час (750.000.000.000$)\n\n💡 Вы не можете иметь фермы от разных производителей.\n🛒 Для покупки фермы введите \"Купить ферму [номер]\"\n🛒 Для покупки видеокарты для фермы введите \"Купить видеокарту [кол-во]\"", parse_mode='html')

    if message.text.lower() in ["продать ферму", "Продать ферму"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5 
       if farmscoin == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету майнинг-фермы! {rloser}", parse_mode='html')
       if farmcoin1 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою майнинг-ферму за 3.750.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 3750000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farmcoin1 = {0} WHERE user_id = "{user_id}"')  
          cursor.execute(f'UPDATE users SET vcard = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if farmcoin2 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою майнинг-ферму за 45.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 45000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farmcoin2 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET vcard = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if farmcoin3 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою майнинг-ферму за 487.500.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 487500000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farmcoin3 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET vcard = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if farmcoin4 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою майнинг-ферму за 60.000.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 60000000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farmcoin4 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET vcard = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if farmcoin5 == 1:
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свою майнинг-ферму за 562.500.000.000$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + 562500000000} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET farmcoin5 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET vcard = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 

    if message.text.lower() in ["Моя ферма", "моя ферма"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       vcard = cursor.execute("SELECT vcard from users where user_id = ?",(message.from_user.id,)).fetchone()
       vcard = int(vcard[0])
       bitmaning = cursor.execute("SELECT bitmaning from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitmaning = int(bitmaning[0])
       profit1 = '{0:,}'.format(vcard * 4).replace(',', '.')
       profit2 = '{0:,}'.format(vcard * 12).replace(',', '.')
       profit3 = '{0:,}'.format(vcard * 64).replace(',', '.')
       profit4 = '{0:,}'.format(vcard * 650).replace(',', '.')
       profit5 = '{0:,}'.format(vcard * 3500).replace(',', '.')
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       bitmaning2 = '{0:,}'.format(bitmaning).replace(',', '.')
       if farmscoin == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету майнинг фермы! {rloser}", parse_mode='html')
       if farmcoin1 == 1:
          await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей майнинг-ферме:\nℹ️ Название фермы: TI-Miner\n💸 Прибыль: {profit1}฿/чаc\n💼 Видеокарт: {vcard}/1000\n💰 На счету: {bitmaning2}฿", parse_mode='html')
       if farmcoin2 == 1:
          await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей майнинг-ферме:\nℹ️ Название фермы: Saturn\n💸 Прибыль: {profit2}฿/чаc\n💼 Видеокарт: {vcard}/1000\n💰 На счету: {bitmaning2}฿", parse_mode='html')
       if farmcoin3 == 1:
          await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей майнинг-ферме:\nℹ️ Название фермы: Calisto\n💸 Прибыль: {profit3}฿/чаc\n💼 Видеокарт: {vcard}/1000\n💰 На счету: {bitmaning2}฿", parse_mode='html')
       if farmcoin4 == 1:
          await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей майнинг-ферме:\nℹ️ Название фермы: HashMiner\n💸 Прибыль: {profit4}฿/чаc\n💼 Видеокарт: {vcard}/1000\n💰 На счету: {bitmaning2}฿", parse_mode='html')
       if farmcoin5 == 1:
          await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашей майнинг-ферме:\nℹ️ Название фермы: MegaWatt\n💸 Прибыль: {profit5}฿/чаc\n💼 Видеокарт: {vcard}/1000\n💰 На счету: {bitmaning2}฿", parse_mode='html')

    if message.text.lower() in ["купить ферму 1", "Купить ферму 1"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 5000000
       c = 1
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       if farmscoin == 0:
          if farmcoin1 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили майнинг-ферму \"TI-Miner\" за 5.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farmcoin1 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farmcoin1 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная майнинг-ферма! {rloser}", parse_mode='html')     
             return
       if farmscoin == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть майнинг-ферма! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить ферму 2", "Купить ферму 2"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 60000000
       c = 1
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       if farmscoin == 0:
          if farmcoin2 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили майнинг-ферму \"Saturn\" за 60.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farmcoin2 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farmcoin2 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная майнинг-ферма! {rloser}", parse_mode='html')     
             return
       if farmscoin == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть майнинг-ферма! {rloser}", parse_mode='html')  
  
    if message.text.lower() in ["купить ферму 3", "Купить ферму 3"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 650000000
       c = 1
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       if farmscoin == 0:
          if farmcoin3 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили майнинг-ферму \"Calisto\" за 650.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farmcoin3 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farmcoin3 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная майнинг-ферма! {rloser}", parse_mode='html')     
             return
       if farmscoin == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть майнинг-ферма! {rloser}", parse_mode='html')  
    
    if message.text.lower() in ["купить ферму 4", "Купить ферму 4"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 80000000000
       c = 1
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       if farmscoin == 0:
          if farmcoin4 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили майнинг-ферму \"HashMiner\" за 80.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farmcoin4 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farmcoin4 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная майнинг-ферма! {rloser}", parse_mode='html')     
             return
       if farmscoin == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть майнинг-ферма! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить ферму 5", "Купить ферму 5"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 750000000000
       c = 1
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       if farmscoin == 0:
          if farmcoin5 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили майнинг-ферму \"MegaWatt\" за 750.000.000.000$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET farmcoin5 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if farmcoin5 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данная майнинг-ферма! {rloser}", parse_mode='html')     
             return
       if farmscoin == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть майнинг-ферма! {rloser}", parse_mode='html')  

    if message.text.startswith("купить видеокарту"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       vcard = cursor.execute("SELECT vcard from users where user_id = ?",(message.from_user.id,)).fetchone()
       vcard = int(vcard[0])
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       summ = int(msg.text.split()[2])
       check = vcard + summ

       check_balance1 = summ * 5000000
       check_balance2 = summ * 60000000
       check_balance3 = summ * 650000000
       check_balance4 = summ * 80000000000
       check_balance5 = summ * 750000000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число видеокарт! {rloser}", parse_mode='html')
          return
       if farmscoin == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету майнинг-фермы! {rloser}", parse_mode='html')
          return
       if check > 1000:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить больше 1000 видеокарт! {rloser}", parse_mode='html')
          return
       if check <= 1000:
          if farmcoin1 == 1:
             if check_balance1 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance1 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farmcoin2 == 1:
             if check_balance2 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance2 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farmcoin3 == 1:
             if check_balance3 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance3 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farmcoin4 == 1:
             if check_balance4 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance4 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farmcoin5 == 1:
             if check_balance5 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance5 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
   
    if message.text.startswith("Купить видеокарту"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       vcard = cursor.execute("SELECT vcard from users where user_id = ?",(message.from_user.id,)).fetchone()
       vcard = int(vcard[0])
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       summ = int(msg.text.split()[2])
       check = vcard + summ

       check_balance1 = summ * 5000000
       check_balance2 = summ * 60000000
       check_balance3 = summ * 650000000
       check_balance4 = summ * 80000000000
       check_balance5 = summ * 750000000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число видеокарт! {rloser}", parse_mode='html')
          return
       if farmscoin == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету майнинг-фермы! {rloser}", parse_mode='html')
          return
       if check > 1000:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить больше 1000 видеокарт! {rloser}", parse_mode='html')
          return
       if check <= 1000:
          if farmcoin1 == 1:
             if check_balance1 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance1 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farmcoin2 == 1:
             if check_balance2 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance2 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farmcoin3 == 1:
             if check_balance3 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance3 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farmcoin4 == 1:
             if check_balance4 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance4 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if farmcoin5 == 1:
             if check_balance5 <= balance:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} видеокарт за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance5 > balance:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return

    if message.text.startswith("ферма снять"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       vcard = cursor.execute("SELECT vcard from users where user_id = ?",(message.from_user.id,)).fetchone()
       vcard = int(vcard[0])
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       bitmaning = cursor.execute("SELECT bitmaning from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitmaning = int(bitmaning[0])
       summ = int(message.text.split()[2])
       summ_get = '{0:,}'.format(summ).replace(',', '.')
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете снять отрицательное число биткоина! {rloser}", parse_mode='html') 
          return
       if farmscoin == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету майнинг-фермы! {rloser}", parse_mode='html')
       if farmcoin1 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿ с балансов вашей майнинг-фермы!", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farmcoin2 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿ с балансов вашей майнинг-фермы", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farmcoin3 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿️ с баланса вашей майнинг-фермы!", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farmcoin4 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿️ с баланса вашей майнинг-фермы!", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farmcoin5 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿️ с баланса вашей майнинг-фермы!", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 

    if message.text.startswith("Ферма снять"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       vcard = cursor.execute("SELECT vcard from users where user_id = ?",(message.from_user.id,)).fetchone()
       vcard = int(vcard[0])
       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       bitcoin = cursor.execute("SELECT bitcoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitcoin = int(bitcoin[0])
       bitmaning = cursor.execute("SELECT bitmaning from users where user_id = ?",(message.from_user.id,)).fetchone()
       bitmaning = int(bitmaning[0])
       summ = int(message.text.split()[2])
       summ_get = '{0:,}'.format(summ).replace(',', '.')
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете снять отрицательное число биткоина! {rloser}", parse_mode='html') 
          return
       if farmscoin == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету майнинг-фермы! {rloser}", parse_mode='html')
       if farmcoin1 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿ с баланса вашей майнинг-фермы!", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farmcoin2 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно битк! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿ с баланса вашей майнинг-фермы", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farmcoin3 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿️ с баланса вашей майнинг-фермы!", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farmcoin4 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿️ с баланса вашей майнинг-фермы!", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 
       if farmcoin5 == 1:
          if summ > bitmaning:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= bitmaning:
             await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}฿️ с баланса вашей майнинг-фермы!", parse_mode='html')
             cursor.execute(f'UPDATE users SET bitmaning = {bitmaning - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bitcoin = {bitcoin + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 

    if message.text.startswith("продать видеокарту"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       vcard = cursor.execute("SELECT vcard from users where user_id = ?",(message.from_user.id,)).fetchone()
       vcard = int(vcard[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       summ = int(msg.text.split()[2])
       check = vcard + summ

       check_balance1 = summ * 3750000
       check_balance2 = summ * 45000000
       check_balance3 = summ * 487500000
       check_balance4 = summ * 60000000000
       check_balance5 = summ * 562500000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число видеокарт! {rloser}", parse_mode='html')
          return
       if farmscoin == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету майнинг-фермы! {rloser}", parse_mode='html')
          return
       if summ > 1000:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете продать больше 1000 видеокарт! {rloser}", parse_mode='html')
          return
       if summ <= 1000:
          if farmcoin1 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return
          if farmcoin2 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return
          if farmcoin3 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return
          if farmcoin4 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return
          if farmcoin5 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return

    if message.text.startswith("Продать видеокарту"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       farmcoin1 = cursor.execute("SELECT farmcoin1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin1 = int(farmcoin1[0])
       farmcoin2 = cursor.execute("SELECT farmcoin2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin2 = int(farmcoin2[0])
       farmcoin3 = cursor.execute("SELECT farmcoin3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin3 = int(farmcoin3[0])
       farmcoin4 = cursor.execute("SELECT farmcoin4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin4 = int(farmcoin4[0])
       farmcoin5 = cursor.execute("SELECT farmcoin5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       farmcoin5 = int(farmcoin5[0])
       vcard = cursor.execute("SELECT vcard from users where user_id = ?",(message.from_user.id,)).fetchone()
       vcard = int(vcard[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       farmscoin = farmcoin1 + farmcoin2 + farmcoin3 + farmcoin4 + farmcoin5
       summ = int(msg.text.split()[2])
       check = vcard + summ

       check_balance1 = summ * 3750000
       check_balance2 = summ * 45000000
       check_balance3 = summ * 487500000
       check_balance4 = summ * 60000000000
       check_balance5 = summ * 562500000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число видеокарт! {rloser}", parse_mode='html')
          return
       if farmscoin == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету майнинг-фермы! {rloser}", parse_mode='html')
          return
       if summ > 1000:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете продать больше 1000 видеокарт! {rloser}", parse_mode='html')
          return
       if summ <= 1000:
          if farmcoin1 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return
          if farmcoin2 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return
          if farmcoin3 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return
          if farmcoin4 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return
          if farmcoin5 == 1:
             if summ <= vcard:
                await bot.send_message(message.chat.id, f"🧰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} видеокарт за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET vcard = {vcard - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > vcard:
                await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно видеокарт! {rloser}", parse_mode='html')
                return

    if message.text.lower() in ["Бизнесы", "бизнесы"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, доступные бизнесы для покупки: \n🌯 1. Шаурмечная: 50 тыс $\nПрибыль: 1.000$/час\n\n🕺 2. Ночной клуб: 500 тыс $\nПрибыль: 10.000$/час\n\n🚬 3. Кальянная: 1 млн $\nПрибыль: 40.000$/час\n\n⛽️ 4. АЗС: 1.5 млн $\nПрибыль: 50.000$/час\n\n🏩 5. Порностудия: 3 млн $\nПрибыль: 75.000$/час\n\n🏢 6. Маленький офис: 7 млн $\nПрибыль: 150.000$/час\n\n🛢 7. Нефтевышка: 10 млн $\nПрибыль: 200.000$/час\n\n👩 8. Космическое агентство: 20 млн $\nПрибыль: 400.000$/час\n\n🚀 9. Межпланетный экспресс: 40 млн $\nПрибыль: 800.000$/час\n\n💡 Вы можете купить только ОДИН бизнес.\n🛒 Для покупки введите \"Купить бизнес [номер]\"", parse_mode='html')

    if message.text.lower() in ["купить бизнес 1", "Купить бизнес 1"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 50000
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       name = "Шаурмечная"
       sticker = "🌯"
       c = 1
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          if business1 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили бизнес \"{name}\" за {summ2}$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET business1 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if business1 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный бизнес! {rloser}", parse_mode='html')     
             return
       if businesses == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть бизнес! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить бизнес 2", "Купить бизнес 2"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 500000
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       name = "Ночной клуб"
       sticker = "🕺"
       c = 1
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          if business2 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили бизнес \"{name}\" за {summ2}$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET business2 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if business2 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный бизнес! {rloser}", parse_mode='html')     
             return
       if businesses == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть бизнес! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить бизнес 3", "Купить бизнес 3"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1000000
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       name = "Кальянная"
       sticker = "🚬"
       c = 1
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          if business3 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили бизнес \"{name}\" за {summ2}$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET business3 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if business3 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный бизнес! {rloser}", parse_mode='html')     
             return
       if businesses == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть бизнес! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить бизнес 4", "Купить бизнес 4"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 1500000
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       name = "АЗС"
       sticker = "⛽"
       c = 1
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          if business4 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили бизнес \"{name}\" за {summ2}$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET business4 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if business4 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный бизнес! {rloser}", parse_mode='html')     
             return
       if businesses == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть бизнес! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить бизнес 5", "Купить бизнес 5"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 3000000
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       name = "Порностудия"
       sticker = "🏩"
       c = 1
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          if business5 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили бизнес \"{name}\" за {summ2}$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET business5 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if business5 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный бизнес! {rloser}", parse_mode='html')     
             return
       if businesses == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть бизнес! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить бизнес 6", "Купить бизнес 6"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 7000000
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       name = "Маленький офис"
       sticker = "🏢"
       c = 1
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          if business6 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили бизнес \"{name}\" за {summ2}$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET business6 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if business6 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный бизнес! {rloser}", parse_mode='html')     
             return
       if businesses == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть бизнес! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить бизнес 7", "Купить бизнес 7"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 10000000
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       name = "Нефтевышка"
       sticker = "🛢"
       c = 1
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          if business7 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили бизнес \"{name}\" за {summ2}$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET business7 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if business7 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный бизнес! {rloser}", parse_mode='html')     
             return
       if businesses == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть бизнес! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить бизнес 8", "Купить бизнес 8"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 20000000
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       name = "Космическое агентство"
       sticker = "👩"
       c = 1
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          if business8 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили бизнес \"{name}\" за {summ2}$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET business8 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if business8 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный бизнес! {rloser}", parse_mode='html')     
             return
       if businesses == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть бизнес! {rloser}", parse_mode='html')  

    if message.text.lower() in ["купить бизнес 9", "Купить бизнес 9"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       summ = 40000000
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       name = "Межпланетный экспресс"
       sticker = "🚀"
       c = 1
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          if business9 == 0:
             if int(balance) >= int(summ):
                await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили бизнес \"{name}\" за {summ2}$ 🎉", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET business9 = {1} WHERE user_id = "{user_id}"') 
                connect.commit()    
                return
             else:
                await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств! {rloser}", parse_mode='html')     
                return
          if business9 == 1:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть данный бизнес! {rloser}", parse_mode='html')     
             return
       if businesses == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас уже есть бизнес! {rloser}", parse_mode='html') 

    if message.text.lower() in ["Мой бизнес", "мой бизнес"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       workers = cursor.execute("SELECT workers from users where user_id = ?",(message.from_user.id,)).fetchone()
       workers = int(workers[0])
       busscash = cursor.execute("SELECT busscash from users where user_id = ?",(message.from_user.id,)).fetchone()
       busscash = int(busscash[0])
       income1 = '{0:,}'.format(workers).replace(',', '.')
       income2 = '{0:,}'.format(10000).replace(',', '.')
       income3 = '{0:,}'.format(40000).replace(',', '.')
       income4 = '{0:,}'.format(50000).replace(',', '.')
       income5 = '{0:,}'.format(75000).replace(',', '.')
       income6 = '{0:,}'.format(150000).replace(',', '.')
       income7 = '{0:,}'.format(200000).replace(',', '.')
       income8 = '{0:,}'.format(400000).replace(',', '.')
       income9 = '{0:,}'.format(800000).replace(',', '.')
       workbonus = '{0:,}'.format(workers * 100000).replace(',', '.')
       busscash = '{0:,}'.format(busscash).replace(',', '.')
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету бизнеса! {rloser}", parse_mode='html')
       if business1 == 1:
          sticker = "🌯"
          name = "Шаурмечная"
          await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашем бизнесе:\nℹ️ Название бизнеса: {name}\n💸 Прибыль: {income1}$/чаc\n💼 Рабочих: {workers}/750\n💰 На счету: {busscash}$\n💲 Бонус за рабочих: {workbonus}$", parse_mode='html')
       if business2 == 1:
          sticker = "🕺"
          name = "Ночной клуб"
          await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашем бизнесе:\nℹ️ Название бизнеса: {name}\n💸 Прибыль: {income2}$/чаc\n💼 Рабочих: {workers}/750\n💰 На счету: {busscash}$\n💲 Бонус за рабочих: {workbonus}$", parse_mode='html')
       if business3 == 1:
          sticker = "🚬"
          name = "Кальянная"
          await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашем бизнесе:\nℹ️ Название бизнеса: {name}\n💸 Прибыль: {income3}$/чаc\n💼 Рабочих: {workers}/750\n💰 На счету: {busscash}$\n💲 Бонус за рабочих: {workbonus}$", parse_mode='html')
       if business4 == 1:
          sticker = "⛽"
          name = "АЗС"
          await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашем бизнесе:\nℹ️ Название бизнеса: {name}\n💸 Прибыль: {income4}$/чаc\n💼 Рабочих: {workers}/750\n💰 На счету: {busscash}$\n💲 Бонус за рабочих: {workbonus}$", parse_mode='html')
       if business5 == 1:
          sticker = "🏩"
          name = "Порностудия"
          await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашем бизнесе:\nℹ️ Название бизнеса: {name}\n💸 Прибыль: {income5}$/чаc\n💼 Рабочих: {workers}/750\n💰 На счету: {busscash}$\n💲 Бонус за рабочих: {workbonus}$", parse_mode='html')
       if business6 == 1:
          sticker = "🏢"
          name = "Маленький офис"
          await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашем бизнесе:\nℹ️ Название бизнеса: {name}\n💸 Прибыль: {income6}$/чаc\n💼 Рабочих: {workers}/750\n💰 На счету: {busscash}$\n💲 Бонус за рабочих: {workbonus}$", parse_mode='html')
       if business7 == 1:
          sticker = "🛢"
          name = "Нефтевышка"
          await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашем бизнесе:\nℹ️ Название бизнеса: {name}\n💸 Прибыль: {income7}$/чаc\n💼 Рабочих: {workers}/750\n💰 На счету: {busscash}$\n💲 Бонус за рабочих: {workbonus}$", parse_mode='html')
       if business8 == 1:
          sticker = "👩"
          name = "Космическое агентство"
          await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашем бизнесе:\nℹ️ Название бизнеса: {name}\n💸 Прибыль: {income8}$/чаc\n💼 Рабочих: {workers}/750\n💰 На счету: {busscash}$\n💲 Бонус за рабочих: {workbonus}$", parse_mode='html')
       if business9 == 1:
          sticker = "🚀"
          name = "Межпланетный экспресс"
          await bot.send_message(message.chat.id, f"{sticker} | <a href='tg://user?id={user_id}'>{user_name}</a>, информация о вашем бизнесе:\nℹ️ Название бизнеса: {name}\n💸 Прибыль: {income9}$/чаc\n💼 Рабочих: {workers}/750\n💰 На счету: {busscash}$\n💲 Бонус за рабочих: {workbonus}$", parse_mode='html')

    if message.text.lower() in ["продать бизнес", "Продать бизнес"]: 
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       if businesses == 0:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету бизнеса! {rloser}", parse_mode='html')
       if business1 == 1:
          summ = 50000 * 0.75
          summ2 = '{0:,}'.format(summ).replace(',', '.')
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свой бизнес за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET business1 = {0} WHERE user_id = "{user_id}"')  
          cursor.execute(f'UPDATE users SET workers = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if business2 == 1:
          summ = 500000 * 0.75
          summ2 = '{0:,}'.format(summ).replace(',', '.')
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свой бизнес за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET business2 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET workers = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if business3 == 1:
          summ = 1000000 * 0.75
          summ2 = '{0:,}'.format(summ).replace(',', '.')
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свой бизнес за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET business3 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET workers = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if business4 == 1:
          summ = 1500000 * 0.75
          summ2 = '{0:,}'.format(summ).replace(',', '.')
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свой бизнес за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET business4 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET workers = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if business5 == 1:
          summ = 3000000 * 0.75
          summ2 = '{0:,}'.format(summ).replace(',', '.')
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свой бизнес за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET business5 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET workers = {0} WHERE user_id = "{user_id}"') 
          connect.commit() 
       if business6 == 1:
          summ = 7000000 * 0.75
          summ2 = '{0:,}'.format(summ).replace(',', '.')
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свой бизнес за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET business6 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET workers = {0} WHERE user_id = "{user_id}"') 
          connect.commit()
       if business7 == 1:
          summ = 10000000 * 0.75
          summ2 = '{0:,}'.format(summ).replace(',', '.')
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свой бизнес за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET business7 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET workers = {0} WHERE user_id = "{user_id}"') 
          connect.commit()
       if business8 == 1:
          summ = 20000000 * 0.75
          summ2 = '{0:,}'.format(summ).replace(',', '.')
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свой бизнес за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET business8 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET workers = {0} WHERE user_id = "{user_id}"') 
          connect.commit()
       if business9 == 1:
          summ = 40000000 * 0.75
          summ2 = '{0:,}'.format(summ).replace(',', '.')
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали свой бизнес за {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET business9 = {0} WHERE user_id = "{user_id}"') 
          cursor.execute(f'UPDATE users SET workers = {0} WHERE user_id = "{user_id}"') 
          connect.commit()

    if message.text.startswith("купить рабочих"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       workers = cursor.execute("SELECT workers from users where user_id = ?",(message.from_user.id,)).fetchone()
       workers = int(workers[0])
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       summ = int(msg.text.split()[2])
       check = workers + summ

       check_balance1 = summ * 50000
       check_balance2 = summ * 500000
       check_balance3 = summ * 1000000
       check_balance4 = summ * 1500000
       check_balance5 = summ * 3000000
       check_balance6 = summ * 7000000
       check_balance7 = summ * 10000000
       check_balance8 = summ * 20000000
       check_balance9 = summ * 40000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')
       check_balance6_up = '{0:,}'.format(check_balance6).replace(',', '.')
       check_balance7_up = '{0:,}'.format(check_balance7).replace(',', '.')
       check_balance8_up = '{0:,}'.format(check_balance8).replace(',', '.')
       check_balance9_up = '{0:,}'.format(check_balance9).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число рабочих! {rloser}", parse_mode='html')
          return
       if businesses == 0:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету бизнеса! {rloser}", parse_mode='html')
          return
       if check > 750:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить больше 750 рабочих! {rloser}", parse_mode='html')
          return
       if check <= 750:
          if business1 == 1:
             if check_balance1 <= balance:
                await bot.send_message(message.chat.id, f"🌯 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance1 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business2 == 1:
             if check_balance2 <= balance:
                await bot.send_message(message.chat.id, f"🕺 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance2 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business3 == 1:
             if check_balance3 <= balance:
                await bot.send_message(message.chat.id, f"🚬 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance3 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business4 == 1:
             if check_balance4 <= balance:
                await bot.send_message(message.chat.id, f"⛽️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance4 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business5 == 1:
             if check_balance5 <= balance:
                await bot.send_message(message.chat.id, f"🏩 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance5 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business6 == 1:
             if check_balance6 <= balance:
                await bot.send_message(message.chat.id, f"🏢 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance6_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance6} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance6 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business7 == 1:
             if check_balance7 <= balance:
                await bot.send_message(message.chat.id, f"🛢 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance7_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance7} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance7 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business8 == 1:
             if check_balance8 <= balance:
                await bot.send_message(message.chat.id, f"👩 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance8_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance8} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance8 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business9 == 1:
             if check_balance9 <= balance:
                await bot.send_message(message.chat.id, f"🚀 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance9_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance9} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance9 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return

    if message.text.startswith("Купить рабочих"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       workers = cursor.execute("SELECT workers from users where user_id = ?",(message.from_user.id,)).fetchone()
       workers = int(workers[0])
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       summ = int(msg.text.split()[2])
       check = workers + summ

       check_balance1 = summ * 50000
       check_balance2 = summ * 500000
       check_balance3 = summ * 1000000
       check_balance4 = summ * 1500000
       check_balance5 = summ * 3000000
       check_balance6 = summ * 7000000
       check_balance7 = summ * 10000000
       check_balance8 = summ * 20000000
       check_balance9 = summ * 40000000
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')
       check_balance6_up = '{0:,}'.format(check_balance6).replace(',', '.')
       check_balance7_up = '{0:,}'.format(check_balance7).replace(',', '.')
       check_balance8_up = '{0:,}'.format(check_balance8).replace(',', '.')
       check_balance9_up = '{0:,}'.format(check_balance9).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число рабочих! {rloser}", parse_mode='html')
          return
       if businesses == 0:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету бизнеса! {rloser}", parse_mode='html')
          return
       if check > 750:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить больше 750 рабочих! {rloser}", parse_mode='html')
          return
       if check <= 750:
          if business1 == 1:
             if check_balance1 <= balance:
                await bot.send_message(message.chat.id, f"🌯 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance1 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business2 == 1:
             if check_balance2 <= balance:
                await bot.send_message(message.chat.id, f"🕺 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance2 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business3 == 1:
             if check_balance3 <= balance:
                await bot.send_message(message.chat.id, f"🚬 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance3 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business4 == 1:
             if check_balance4 <= balance:
                await bot.send_message(message.chat.id, f"⛽️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance4 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business5 == 1:
             if check_balance5 <= balance:
                await bot.send_message(message.chat.id, f"🏩 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance5 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business6 == 1:
             if check_balance6 <= balance:
                await bot.send_message(message.chat.id, f"🏢 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance6_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance6} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance6 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business7 == 1:
             if check_balance7 <= balance:
                await bot.send_message(message.chat.id, f"🛢 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance7_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance7} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance7 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business8 == 1:
             if check_balance8 <= balance:
                await bot.send_message(message.chat.id, f"👩 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance8_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance8} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance8 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return
          if business9 == 1:
             if check_balance9 <= balance:
                await bot.send_message(message.chat.id, f"🚀 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили {summ} рабочих за {check_balance9_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance - check_balance9} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers + summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if check_balance9 > balance:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, не достаточно средств! {rloser}", parse_mode='html')
                return

    if message.text.startswith("продать рабочих"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       workers = cursor.execute("SELECT workers from users where user_id = ?",(message.from_user.id,)).fetchone()
       workers = int(workers[0])
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       summ = int(msg.text.split()[2])
       check = workers + summ

       check_balance1 = summ * 50000 * 0.75
       check_balance2 = summ * 500000 * 0.75
       check_balance3 = summ * 1000000 * 0.75
       check_balance4 = summ * 1500000 * 0.75
       check_balance5 = summ * 3000000 * 0.75
       check_balance6 = summ * 7000000 * 0.75
       check_balance7 = summ * 10000000 * 0.75
       check_balance8 = summ * 20000000 * 0.75
       check_balance9 = summ * 40000000 * 0.75
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')
       check_balance6_up = '{0:,}'.format(check_balance6).replace(',', '.')
       check_balance7_up = '{0:,}'.format(check_balance7).replace(',', '.')
       check_balance8_up = '{0:,}'.format(check_balance8).replace(',', '.')
       check_balance9_up = '{0:,}'.format(check_balance9).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число рабочих! {rloser}", parse_mode='html')
          return
       if businesses == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету бизнеса! {rloser}", parse_mode='html')
          return
       if summ > 750:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете продать больше 750 рабочих! {rloser}", parse_mode='html')
          return
       if summ <= 750:
          if business1 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🌯 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business2 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🕺 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business3 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🚬 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business4 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"⛽️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business5 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🏩 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business6 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🏢 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance6_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance6} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return        
          if business7 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🛢 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance7_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance7} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business8 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"👩 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance8_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance8} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business9 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🚀 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance9_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance9} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return

    if message.text.startswith("Продать рабочих"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       workers = cursor.execute("SELECT workers from users where user_id = ?",(message.from_user.id,)).fetchone()
       workers = int(workers[0])
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       chat_id = message.chat.id
       msg = message
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = msg.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))

       summ = int(msg.text.split()[2])
       check = workers + summ

       check_balance1 = summ * 50000 * 0.75
       check_balance2 = summ * 500000 * 0.75
       check_balance3 = summ * 1000000 * 0.75
       check_balance4 = summ * 1500000 * 0.75
       check_balance5 = summ * 3000000 * 0.75
       check_balance6 = summ * 7000000 * 0.75
       check_balance7 = summ * 10000000 * 0.75
       check_balance8 = summ * 20000000 * 0.75
       check_balance9 = summ * 40000000 * 0.75
       
       check_balance1_up = '{0:,}'.format(check_balance1).replace(',', '.')
       check_balance2_up = '{0:,}'.format(check_balance2).replace(',', '.')
       check_balance3_up = '{0:,}'.format(check_balance3).replace(',', '.')
       check_balance4_up = '{0:,}'.format(check_balance4).replace(',', '.')
       check_balance5_up = '{0:,}'.format(check_balance5).replace(',', '.')
       check_balance6_up = '{0:,}'.format(check_balance6).replace(',', '.')
       check_balance7_up = '{0:,}'.format(check_balance7).replace(',', '.')
       check_balance8_up = '{0:,}'.format(check_balance8).replace(',', '.')
       check_balance9_up = '{0:,}'.format(check_balance9).replace(',', '.')

       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число рабочих! {rloser}", parse_mode='html')
          return
       if businesses == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нету бизнеса! {rloser}", parse_mode='html')
          return
       if summ > 750:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете продать больше 750 рабочих! {rloser}", parse_mode='html')
          return
       if summ <= 750:
          if business1 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🌯 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance1_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance1} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business2 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🕺 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance2_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance2} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business3 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🚬 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance3_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance3} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business4 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"⛽️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance4_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance4} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business5 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🏩 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance5_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance5} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business6 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🏢 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance6_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance6} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return        
          if business7 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🛢 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance7_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance7} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business8 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"👩 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance8_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance8} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return
          if business9 == 1:
             if summ <= workers:
                await bot.send_message(message.chat.id, f"🚀 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно продали {summ} рабочих за {check_balance9_up}$ !", parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + check_balance9} WHERE user_id = "{user_id}"') 
                cursor.execute(f'UPDATE users SET workers = {workers - summ} WHERE user_id = "{user_id}"') 
                connect.commit() 
             if summ > workers:
                await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно рабочих! {rloser}", parse_mode='html')
                return

    if message.text.startswith("бизнес снять"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       busscash = cursor.execute("SELECT busscash from users where user_id = ?",(message.from_user.id,)).fetchone()
       busscash = int(busscash[0])
       summ = int(message.text.split()[2])
       summ_get = '{0:,}'.format(summ).replace(',', '.')
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете снять отрицательное число с баланса бизнеса! {rloser}", parse_mode='html') 
          return
       if businesses == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас бизнеса! {rloser}", parse_mode='html')
       else:
          if summ > busscash:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= busscash:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}$ с баланса вашего бизнеса!", parse_mode='html')
             cursor.execute(f'UPDATE users SET busscash = {busscash - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
             connect.commit() 

    if message.text.startswith("Бизнес снять"):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       business1 = cursor.execute("SELECT business1 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business1 = int(business1[0])
       business2 = cursor.execute("SELECT business2 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business2 = int(business2[0])
       business3 = cursor.execute("SELECT business3 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business3 = int(business3[0])
       business4 = cursor.execute("SELECT business4 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business4 = int(business4[0])
       business5 = cursor.execute("SELECT business5 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business5 = int(business5[0])
       business6 = cursor.execute("SELECT business6 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business6 = int(business6[0])
       business7 = cursor.execute("SELECT business7 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business7 = int(business7[0])
       business8 = cursor.execute("SELECT business8 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business8 = int(business8[0])
       business9 = cursor.execute("SELECT business9 from users where user_id = ?",(message.from_user.id,)).fetchone()
       business9 = int(business9[0])
       businesses = business1 + business2 + business3 + business4 + business5 + business6 + business7 + business8 + business9
       busscash = cursor.execute("SELECT busscash from users where user_id = ?",(message.from_user.id,)).fetchone()
       busscash = int(busscash[0])
       summ = int(message.text.split()[2])
       summ_get = '{0:,}'.format(summ).replace(',', '.')
       chat_id = message.chat.id
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       user_id = message.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       if summ <= 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете снять отрицательное число с баланса бизнеса! {rloser}", parse_mode='html') 
          return
       if businesses == 0:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас бизнеса! {rloser}", parse_mode='html')
       else:
          if summ > busscash:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, на счету вашей фермы недостаточно биткоинов! {rloser}", parse_mode='html') 
          if summ <= busscash:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно сняли {summ_get}$ с баланса вашего бизнеса!", parse_mode='html')
             cursor.execute(f'UPDATE users SET busscash = {busscash - summ} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + summ} WHERE user_id = "{user_id}"') 
             connect.commit()
    
    if message.text.lower() in ["Донат", "донат"]:
       user_id = message.from_user.id
       scoin = cursor.execute("SELECT scoin from users where user_id = ?",(message.from_user.id,)).fetchone()
       scoin = round(int(scoin[0]))
       admin_id = 5592294018
       donate = cursor.execute("SELECT donate from users where user_id = ?",(admin_id,)).fetchone()
       donate = round(int(donate[0]))
       scoin2 = '{0:,}'.format(scoin).replace(',', '.')
       donate2 = '{0:,}'.format(donate).replace(',', '.')
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, наш магазин:\n\n🏆 Привилегии:\n1️⃣ Admin Status | 1.500 S-Coin\n\n💸 Валюта:\n2️⃣ 1 S-Coin - {donate2}$\n\n🔝Покупка: Купить привилегию [номер]\n🔝Покупка: Купить валюту [сумма S-Coin]\n\n💰Ваш донат-баланс: {scoin2} S-Coin\n⚡️Для пополнения своего донат-баланса просьба обратиться к владельцу: @rave_admin", parse_mode='html')

    if message.text.startswith("set donate"):  
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(user_id,)).fetchone()
       user_name = user_name[0]
       admin_id = 5592294018
       donate = cursor.execute("SELECT donate from users where user_id = ?",(admin_id,)).fetchone()
       donate = round(int(donate[0]))
       summ = int(message.text.split()[2])
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if user_id == admin_id:        
          await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно установили валютный курс равный {summ2}$", parse_mode='html')
          cursor.execute(f'UPDATE users SET donate = {summ} WHERE user_id = "{admin_id}"')
          connect.commit()      
       else:
          return

    if message.text.startswith("купить валюту"):  
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(user_id,)).fetchone()
       user_name = user_name[0]
       scoin = cursor.execute("SELECT scoin from users where user_id = ?",(user_id,)).fetchone()
       scoin = round(int(scoin[0]))
       balance = cursor.execute("SELECT balance from users where user_id = ?",(user_id,)).fetchone()
       balance = round(int(balance[0]))
       admin_id = 5592294018
       donate = cursor.execute("SELECT donate from users where user_id = ?",(admin_id,)).fetchone()
       donate = round(int(donate[0]))
       summ = int(message.text.split()[2])
       money = donate * summ
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       money2 = '{0:,}'.format(money).replace(',', '.')
       user_status = "Admin"
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if summ > 0:
          if scoin >= summ:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно {money2}$ за {summ2} S-Coin! {rwin}", parse_mode='html')
             await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a> купил {money2}$ на сумму {summ2} S-Coin! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET scoin = {scoin - summ} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET balance = {balance + money} WHERE user_id = "{user_id}"')
             connect.commit() 
          elif scoin < summ:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно донат-валюты! {rloser}", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число валюты! {rloser}", parse_mode='html') 

    if message.text.startswith("Купить валюту"):  
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(user_id,)).fetchone()
       user_name = user_name[0]
       scoin = cursor.execute("SELECT scoin from users where user_id = ?",(user_id,)).fetchone()
       scoin = round(int(scoin[0]))
       balance = cursor.execute("SELECT balance from users where user_id = ?",(user_id,)).fetchone()
       balance = round(int(balance[0]))
       admin_id = 5592294018
       donate = cursor.execute("SELECT donate from users where user_id = ?",(admin_id,)).fetchone()
       donate = round(int(donate[0]))
       summ = int(message.text.split()[2])
       money = donate * summ
       summ2 = '{0:,}'.format(summ).replace(',', '.')
       money2 = '{0:,}'.format(money).replace(',', '.')
       user_status = "Admin"
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if summ > 0:
          if scoin >= summ:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно {money2}$ за {summ2} S-Coin! {rwin}", parse_mode='html')
             await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a> купил {money2}$ на сумму {summ2} S-Coin! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET scoin = {scoin - summ} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET balance = {balance + money} WHERE user_id = "{user_id}"')
             connect.commit() 
          elif scoin < summ:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно донат-валюты! {rloser}", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не можете купить отрицательное число валюты! {rloser}", parse_mode='html') 

    if message.text.startswith("купить привилегию"):  
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(user_id,)).fetchone()
       user_name = user_name[0]
       scoin = cursor.execute("SELECT scoin from users where user_id = ?",(user_id,)).fetchone()
       scoin = round(int(scoin[0]))
       num = int(message.text.split()[2])
       user_status = "Admin_Donate"
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       admin_id = 5592294018
       if num == 1:
          if scoin >= 1500:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию \"Администратор\"! {rwin}", parse_mode='html')
             await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a> купил привилегию \"Администратор\"! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET scoin = {scoin - 1500} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{user_id}"')
             connect.commit() 
          elif scoin < 1500:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно донат-валюты! {rloser}", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, данной привилегии не существует! {rloser}", parse_mode='html') 

    if message.text.startswith("Купить привилегию"):  
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(user_id,)).fetchone()
       user_name = user_name[0]
       scoin = cursor.execute("SELECT scoin from users where user_id = ?",(user_id,)).fetchone()
       scoin = round(int(scoin[0]))
       num = int(message.text.split()[2])
       user_status = "Admin_Donate"
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       admin_id = 5592294018
       if num == 1:
          if scoin >= 1500:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно купили привилегию \"Администратор\"! {rwin}", parse_mode='html')
             await bot.send_message(admin_id, f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a> купил привилегию \"Администратор\"! {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET scoin = {scoin - 1500} WHERE user_id = "{user_id}"')
             cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{user_id}"')
             connect.commit() 
          elif scoin < 1500:
             await bot.send_message(message.chat.id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно донат-валюты! {rloser}", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"ℹ | <a href='tg://user?id={user_id}'>{user_name}</a>, данной привилегии не существует! {rloser}", parse_mode='html')                                                          

    if message.text.startswith("Начислить"):
       perevod = int(message.text.split()[1])
       reply_id = int(message.text.split()[2])
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where id = ?",(reply_id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply_user_id = cursor.execute("SELECT user_id from users where id = ?",(reply_id,)).fetchone()
       reply_user_id = reply_user_id[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')
       user_id = message.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       scoin = cursor.execute("SELECT scoin from users where user_id = ?", (reply_user_id,)).fetchone()
       scoin = round(scoin[0])
       admin_id = 5592294018
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы выдали {perevod2} S-Coin игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          await bot.send_message(admin_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал {perevod2} S-Coin игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html') 
          cursor.execute(f'UPDATE users SET scoin = {scoin + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь владельцем бота!", parse_mode='html') 

    if message.text.startswith("начислить"):
       perevod = int(message.text.split()[1])
       reply_id = int(message.text.split()[2])
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where id = ?",(reply_id,)).fetchone()
       reply_user_name = reply_user_name[0]
       reply_user_id = cursor.execute("SELECT user_id from users where id = ?",(reply_id,)).fetchone()
       reply_user_id = reply_user_id[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod2 = '{0:,}'.format(perevod).replace(',', '.')
       user_id = message.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       scoin = cursor.execute("SELECT scoin from users where user_id = ?", (reply_user_id,)).fetchone()
       scoin = round(scoin[0])
       admin_id = 5592294018
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы выдали {perevod2} S-Coin игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          await bot.send_message(admin_id, f"💰 | <a href='tg://user?id={user_id}'>{user_name}</a> выдал {perevod2} S-Coin игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html') 
          cursor.execute(f'UPDATE users SET scoin = {scoin + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь владельцем бота!", parse_mode='html') 
    
    if message.text.lower() in ["промокод #may9", "Промокод #may9"]:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       promo20 = cursor.execute("SELECT promo20 from users where user_id = ?",(message.from_user.id,)).fetchone()
       promo20 = int(promo20[0])
       promo20_b = cursor.execute("SELECT promo20 from bot").fetchone()
       promo20_b = int(promo20_b[0])
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       if promo20 == 0:
          if promo20_b <= 99:
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно активировали промокод #march8!\n🎁 Получено: 999.999.999.999$ {rwin}", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + 999999999999} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET promo20 = {1}  WHERE user_id = "{user_id}"') 
             cursor.execute(f"UPDATE bot SET promo20 = {promo20_b + 1}")
             connect.commit()
          if promo20_b == 100:
             await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, промокод уже не действителен!", parse_mode='html')
       if promo20 == 1:
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы уже использовали этот промокод!", parse_mode='html')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)