from tkinter import *
import sqlite3
def tableur():
    connection = sqlite3.connect("betav1.mwb")

    cursor = connection.cursor()

    var = entry.get()

    k = 'CREATE TABLE "'

    k = "%s%s" % (k, var)

    b = '" ("id_user"	INTEGER,"user_name"	TEXT,"qr_code"	TEXT,"nb_entry"	INTEGER,PRIMARY KEY("id_user" AUTOINCREMENT))'

    k = "%s%s" % (k, b)

    cursor.execute(k)

    connection.commit()
    connection.close()



win = Tk()

win.title("La tirelire magique ")
win.geometry("360x200")
win.config(background='#00ffe0')

label = Label(win, text='nom du nouveau lieu', font=('Courrier', 27), bg='#00ffe0')
label.pack(side=TOP)

entry = Entry(win, width=45)
entry.pack(expand=YES)

but = Button(win, text='créer ma table', font=('Courrier', 20), bg='#00ffe0', command=tableur)
but.pack(expand=YES)

win.mainloop()