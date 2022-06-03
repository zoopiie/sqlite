from tkinter import *
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


def edit():
    connection = sqlite3.connect("betav1.mwb")

    cursor = connection.cursor()
    b= lettre()
    a = entry2.get()
    c = entry1.get()
    d = entry.get()

    k = "INSERT INTO "

    k = "%s%s" % (k, d)

    e = " VALUES (?,?,?,?)"

    k = "%s%s" % (k, e)

    new_user = (cursor.lastrowid, a,b, c)
    print(k)
    cursor.execute(k, new_user)
    connection.commit()

    connection.close()



win = Tk()

win.title("La tirelire magique ")
win.geometry("800x600")
win.config(background='#00ffe0')


label = Label(win, text='nom du nouveau lieu', font=('Courrier', 27), bg='#00ffe0')
label.pack(side=TOP)

entry = Entry(win, width=45)
entry.pack(expand=YES)

label1 = Label(win, text='nom du gugusse', font=('Courrier', 27), bg='#00ffe0')
label1.pack(side=TOP)

entry2 = Entry(win, width=45)
entry2.pack(expand=YES)

label2 = Label(win, text='nombre de entrez, faites comme chez vous', font=('Courrier', 27), bg='#00ffe0')
label2.pack(side=TOP)

entry1 = Entry(win, width=45)
entry1.pack(expand=YES)

but = Button(win, text='créer utilisateur', font=('Courrier', 20), bg='#00ffe0', command=edit)
but.pack(expand=YES)

win.mainloop()



