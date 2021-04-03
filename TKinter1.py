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
dis = {0: '', 1: '', 2: '',   3: '',  4: '',
       5: '', 6: '', 7: '', 8: '', 9: '', 10: ''}


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
    dis.update({0: '', 1: '', 2: '',   3: '',  4: '',
                5: '', 6: '', 7: '', 8: '', 9: '', 10: ''})
    if curr == 0:
        SC.refresh()
    elif curr == 1:
        LP.refresh()
    elif curr == 2:
        QP.refresh()
    elif curr == 3:
        DH.refresh()


def display():
    global dis
    global curr
    if curr == 0:
        SC.convert(dis)
    elif curr == 1:
        LP.convert(dis)
    elif curr == 2:
        QP.convert(dis)
    elif curr == 3:
        DH.convert(dis)
    for i in range(len(dis)):
        print(dis[i], end="\t")
        print()
    print()


def insert():
    global curr
    global selected
    if curr != selected.get():
        refresh()
        curr = selected.get()
    if curr == 0:
        SC.insert(str(txt.get()))
    elif curr == 1:
        LP.insert(str(txt.get()))
    elif curr == 2:
        QP.insert(str(txt.get()))
    elif curr == 3:
        DH.insert(str(txt.get()))
    display()
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
