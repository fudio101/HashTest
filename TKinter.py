from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from typing import Collection

window = Tk()
window.title("Hash table test")
window.geometry("800x600")
# Thêm label
lbl = Label(window, text="Separate chaining", font=("Times New Roman", 14))
lbl.grid(column=0, row=0)
# Thêm textbox
txt = Entry(window, width=20)
txt.grid(column=0, row=1)


def handleButton():
    lbl.configure(text="Hi, "+txt.get())
    return


# Thêm button
btn = Button(window, text="Say hello", command=handleButton, state="readonly")
btn.grid(column=1, row=1)
# Thêm combobox
combo = Combobox(window)
combo["values"] = ("Separate chaining", "Linear probing",
                   "Quadratic probing", "Double hashing")
combo.current(0)
combo.grid(column=0, row=2)


def handleButton1():
    # lbl.configure(text="Hi, "+combo.get())
    messagebox.showinfo("Test", "Hi "+combo.get())
    return


# Thêm button
btn1 = Button(window, text="Say hello Combo", command=handleButton1)
btn1.grid(column=1, row=2)

window.mainloop()
