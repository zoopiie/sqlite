from time import sleep
from tkinter import *


def led():
    #yo = var.get()
    yo = float(entry.get())

    yo = int(yo)
    if (0<=yo<=255):
        hx = hex(yo)[2::]
        if (yo<16):
            v= "0"
            hx = "%s%s" % (v, hx)
        k = "#ff"
        k = "%s%s" % (k, hx)
        bv = "00"
        k = "%s%s" % (k, bv)
        r = 255
        g = yo
        b = 0
        print(k, r, g, b)

    if (256<=yo<=511):
        yo = 511 - yo
        hx = hex(yo)[2::]
        if (yo<16):
            v= "0"
            hx = "%s%s" % (v, hx)
        k = "#"
        k = "%s%s" % (k, hx)
        bv = "ff00"
        k = "%s%s" % (k, bv)
        r = yo
        g = 255
        b = 0
        print(k, r, g, b)

    if (512 <= yo <= 767):
        yo = yo - 512
        hx = hex(yo )[2::]
        if (yo<16):
            v= "0"
            hx = "%s%s" % (v, hx)

        k = "#00ff"
        k = "%s%s" % (k, hx)
        bv = ""
        k = "%s%s" % (k, bv)
        r = 0
        g = 255
        b = yo
        print(k, r, g, b)

    if (768 <= yo <= 1023):
        yo = 1023 -yo
        hx = hex(yo )[2::]
        if (yo<16):
            v= "0"
            hx = "%s%s" % (v, hx)

        k = "#00"
        k = "%s%s" % (k, hx)
        bv = "ff"
        k = "%s%s" % (k, bv)
        r = 0
        g = yo
        b = 255
        print(k, r, g, b)
    if (1024 <= yo <= 1279):
        yo = yo - 1024
        hx = hex(yo)[2::]
        if (yo<16):
            v= "0"
            hx = "%s%s" % (v, hx)

        k = "#"
        k = "%s%s" % (k, hx)
        bv = "00ff"
        k = "%s%s" % (k, bv)
        r = yo
        g = 0
        b = 255
        print(k, r, g, b)
    if (1278 <= yo <= 1535):
        yo = 1535 - yo
        hx = hex(yo )[2::]
        if (yo<16):
            v= "0"
            hx = "%s%s" % (v, hx)
        k = "#ff00"
        k = "%s%s" % (k, hx)
        bv = ""
        k = "%s%s" % (k, bv)
        r = 255
        g = 0
        b = yo
        print(k, r, g, b)

    if (1536<= yo):
        k = "#ffffff"
        r = 255
        g = 255
        b = 255
        print(k, r , g, b)
    can.config(bg = k)

win = Tk()
can = Canvas(win, width = 200, height= 200, bg = 'white')
can.pack()

entry = Entry(win , width = 45)
entry.pack()

but = Button(win, text= 'kjznihergtiuahrgtiaerigha' , command= led, bg='#00ff00')
but.pack()

win.mainloop()