import sqlite3
import random

def lettre():
    a = random.randint(4,13)
    k =""
    for i in range(a):
        b = random.randint(97, 122)
        b = chr(b)
        k = "%s%s" % (k, b)
    return k




name = input('tu veux pas me doner ton nom steuplé :   ')

lieu = input('tu veux aller ou ?(t as interet a bien l ecrire)   ')

nb_entry = input("tu veux y aller combien de fois !?   ")






if (lieu == 'rouge'):
    connection = sqlite3.connect("essai.db")

    cursor = connection.cursor()
    b= lettre()
    nb = random.randint(1,7)

    new_user = (cursor.lastrowid, name,b, int(nb_entry), 0, 0)
    print(b)
    cursor.execute('INSERT INTO listeall VALUES (?,?,?,?,?,?)', new_user)
    connection.commit()

    connection.close()

if (lieu == 'vert'):
    connection = sqlite3.connect("essai.db")

    cursor = connection.cursor()
    b = lettre()
    nb = random.randint(1, 7)

    new_user = (cursor.lastrowid, name, b, 0, int(nb_entry), 0)
    print(b)
    cursor.execute('INSERT INTO listeall VALUES (?,?,?,?,?,?)', new_user)
    connection.commit()

    connection.close()

if (lieu == 'bleu'):
    connection = sqlite3.connect("essai.db")

    cursor = connection.cursor()
    b = lettre()
    nb = random.randint(1, 7)

    new_user = (cursor.lastrowid, name, b, 0, 0, int(nb_entry))
    print(b)
    cursor.execute('INSERT INTO listeall VALUES (?,?,?,?,?,?)', new_user)
    connection.commit()

    connection.close()