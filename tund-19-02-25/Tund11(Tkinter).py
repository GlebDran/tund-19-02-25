from tkinter import *
from tund_19_02_25 import *

def varvi_valik():
    varv = "black"  # Значение по умолчанию
    if tekst.get() != "":
        varv = tekst.get()  # Считываем введённый цвет
    else:
        tekst.configure(bg="red")  # Подсвечиваем красным, если пусто
    return varv

def figuur():
    global varv
    valik = var.get()
    varv = varvi_valik()

    if valik == 1:
        vaal(varv)
    elif valik == 2:
        Vihmavari()
    elif valik == 3:
        prillid()
    else:
        print("Joonistan hiljem")

aken = Tk()
aken.geometry("400x400")
aken.title("Graafikud")

pealkiri = Label(aken, text="Erinevad piltid Matplotlib abil", font="Calibri 20", fg="white", bg="black", pady=50, width=50)

var = IntVar()

r1 = Radiobutton(aken, text="Vaal", font="Calibri 15", fg="white", bg="black", variable=var, value=1, command=figuur)
r2 = Radiobutton(aken, text="Vihmavari", font="Calibri 15", fg="blue", bg="yellow", variable=var, value=2, command=figuur)
r3 = Radiobutton(aken, text="Prillid", font="Calibri 15", fg="red", bg="black", variable=var, value=3, command=figuur)

tekst = Entry(aken, font="Calibri 20", fg="white", bg="blue", width=20)
nupp = Button(aken, text="Värvi valik", font="Calibri 20", fg="white", bg="black", command=varvi_valik)

pealkiri.pack()
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()
