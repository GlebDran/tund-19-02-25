from tkinter import *
from tund_19_02_25 import *
def figuur():
    valik=var.get()
    if valik==1:
        vaal()
    elif valik==2:
            Vihmavari()
    elif valik==3:
                prillid()
    else:
        print("Joonistan hiljem")

aken=Tk() #modul okna Tk

aken.geometry("400x400")
aken.title("Graafikud")

pealkiri=Label(aken, text="Erinevad piltid Matplotlib abil", font="Calibri 20", fg="white", bg="black", pady=50, width=50)

var=IntVar()

r1=Radiobutton(aken, text="Vaal", font="Calibri 15", fg="white", bg="black", variable=var, value=1,command=figuur)
r2=Radiobutton(aken, text="Vihmavari", font="Calibri 15", fg="blue", bg="yellow", variable=var, value=2,command=figuur)
r3=Radiobutton(aken, text="Prillid", font="Calibri 15", fg="red", bg="black", variable=var, value=3,command=figuur)

pealkiri.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()


