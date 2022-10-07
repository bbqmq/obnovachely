import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()

print("Введите команду:")
message = input()

if message == "reset":
   cursor.execute(f"DELETE FROM users")
   connect.commit()
   print("База данных изменена!")

if message == "new":
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo5")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo6")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo7")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo8")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo9")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo10")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo11")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo12")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo13")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo14")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo15")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo16")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo17")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo18")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo19")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo20")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo21")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo22")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo23")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "promo24")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "cazna")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' STRING" % "group_name")
   cursor.execute("ALTER TABLE bot ADD COLUMN '%s' INT" % "group_time")
   connect.commit()
   print("База данных изменена!")

if message == "antibag":
   cursor.execute(f"UPDATE users SET checking = {0}")
   cursor.execute(f"UPDATE users SET checking1 = {0}")
   cursor.execute(f"UPDATE users SET checking2 = {0}")
   cursor.execute(f"UPDATE users SET checking3 = {0}")
   connect.commit()
   print("Баги исправлены!")
if message == "players":
   list = cursor.execute(f"SELECT * FROM users ORDER BY balance")
   top_list = []
   num = 0
   for user in list:
       num += 1         
       top_list.append(f"{num}. {user[19]}  —  {user[1]}")
   top = "\n".join(top_list)
   print(f"список игроков бота:\n" + top)

if message == "set id":
   list1 = cursor.execute(f"SELECT * FROM users ORDER BY id DESC").fetchall()
   num = 10000
   num2 = 0
   for user in list1:
       cursor.execute(f"UPDATE users SET id = {num} WHERE user_id = {list1[num2][0]}")
       num += 1
       num2 += 1
   connect.commit()