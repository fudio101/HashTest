from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from Hashing import *
from typing import Collection, OrderedDict


SC = SeprateChaining(11)
LP = LinearProbing(11)
QP = QuadraticProbing(11)
DH = DoubleHashing(11)


window = Tk()
window.title("Hash table test")
window.geometry("500x400")


lbl = Label(window, text="Please choose one: ", font=("Arial", 12))

selected = IntVar()
curr = 0

rad1 = Radiobutton(window, text="Seprate Chaining",
                   value=0, variable=selected)

rad2 = Radiobutton(window, text="Linear Probing", value=1, variable=selected)

rad3 = Radiobutton(window, text="Quadratic Probing",
                   value=2, variable=selected)

rad4 = Radiobutton(window, text="Double Hashing", value=3, variable=selected)

txt = Entry(window, width=20)


def clicked():
    print(selected.get())
    return


def refresh():
    global curr
    global dis
    if curr == 0:
        SC.refresh()
    elif curr == 1:
        LP.refresh()
    elif curr == 2:
        QP.refresh()
    elif curr == 3:
        DH.refresh()


def insert():
    global curr
    global selected
    print('\n\n\n')
    if curr != selected.get():
        refresh()
        curr = selected.get()
    if curr == 0:
        SC.insert(str(txt.get()))
        print('Seprate Chaining')
        SC.display()
    elif curr == 1:
        LP.insert(str(txt.get()))
        print('Linear Probing')
        LP.display()
    elif curr == 2:
        QP.insert(str(txt.get()))
        print('Quadratic Probing')
        QP.display()
    elif curr == 3:
        DH.insert(str(txt.get()))
        print('Double Hashing')
        DH.display()
    return


insert()

btn = Button(window, text="Insert", command=insert)
btnr = Button(window, text="Reset", command=refresh)


lbl.grid(column=0, row=0)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)
rad4.grid(column=3, row=1)
txt.grid(column=0, row=2)
btn.grid(column=1, row=2)
btnr.grid(column=2, row=2)


window.mainloop()
