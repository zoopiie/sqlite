import sqlite3

connection = sqlite3.connect("essai.db")

cursor = connection.cursor()

cursor.execute('UPDATE listeall SET ledbleu=70854 WHERE (user_name="orti")')

cursor.execute('SELECT id_user FROM listeall WHERE (user_name="dbvyj")')

b = cursor.fetchone()
#c= b[0]-1
print(b)
connection.commit()

connection.close()