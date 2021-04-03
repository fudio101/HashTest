from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
from typing import Collection, OrderedDict


def Hashing(keyvalue, size):  # 1 + 2*n + 1 = O(n)
    sum = 0
    for i in keyvalue:
        sum += ord(i)
    return sum % size


def Hashing1(keyvalue, size):
    sum = 0
    prime = size // 2+1
    for i in keyvalue:
        sum += ord(i)
    return (prime - (sum % prime))


class SeprateChaining:
    _size = 0
    _hashTable = []

    def __init__(self, size) -> None:
        self._size = size
        self._hashTable = [[] for _ in range(self._size)]

    def insert(self, value):  # O(n)
        hash_key = Hashing(value, self._size)
        self._hashTable[hash_key].append(value)

    def display(self):
        for i in range(len(self._hashTable)):
            print(i, end=" ")
            for j in self._hashTable[i]:
                print("-->", end=" ")
                print(j, end=" ")
            print()

    def refresh(self):
        self._hashTable = [[] for _ in range(self._size)]


class HashTable:
    _size = 0
    _hashTable = []

    def __init__(self, size) -> None:
        self._size = size
        self._hashTable = [None]*self._size

    def _isFull(self):
        currSize = 0
        for i in range(self._size):
            if self._hashTable[i] != None:
                currSize += 1
        if currSize >= self._size - 1:
            return True
        return False

    def insert(self, value):
        pass

    def display(self):
        for i in range(len(self._hashTable)):
            if self._hashTable[i] != None:
                print(i, '', self._hashTable[i])
            else:
                print(i, ' None!!!')

    def refresh(self):
        self._hashTable = [None]*self._size


class LinearProbing(HashTable):
    def insert(self, value):
        if self._isFull():
            return False
        hash_key = Hashing(value, self._size)
        step = 0
        while self._hashTable[hash_key] != None:
            step += 1
            hash_key = (hash_key + step) % self._size
        self._hashTable[hash_key] = value
        return True


class QuadraticProbing(HashTable):
    def insert(self, value):
        if self._isFull():
            return False
        hash_key = base = Hashing(value, self._size)
        step = 0
        while self._hashTable[hash_key] != None:
            step += 1
            hash_key = (base + step ** 2) % self._size
        self._hashTable[hash_key] = value
        return True


class DoubleHashing(HashTable):
    def insert(self, value):
        if self._isFull():
            return False
        hash_key = Hashing1(value, self._size)
        if self._hashTable[hash_key] != None:
            hash_key1 = Hashing1(value)
            step = 0
            while True:
                step += 1
                hash_key = (hash_key + step * hash_key1) % self._size
                if self._hashTable[hash_key] == None:
                    self._hashTable[hash_key] = value
                    break
        else:
            self._hashTable[hash_key] = value


a = DoubleHashing(11)
a.insert('dfnsfl')
a.insert('skngkl')
a.insert('asjfakjb')
a.display()
window = Tk()
window.title("Hash table test")
window.geometry("500x400")
_hashTable = [None] * 11
dis = {
    0: "",
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: ""
}

lbl = Label(window, text="Please choose one: ", font=("Arial", 12))

selected = IntVar()
curr = 0

rad1 = Radiobutton(window, text="Separate Chaining",
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
    switcher = {
        0: sr(hashTable),
        1: lr(_hashTable),
        2: lr(_hashTable),
        3: lr(_hashTable)
    }
    return switcher.get(curr)


def display():
    global dis
    global hashTable
    global _hashTable
    if curr == 0:
        # for i in range(len(hashTable)):
        #     for j in range(hashTable[i]):
        #         dis[i] += (j+"->")
        #     dis[i] += "NULL"
        pass
    else:
        for i in range(len(_hashTable)):
            dis[i] = _hashTable[i]
    for i in range(len(dis)):
        print(dis[i], end="\t")
    print("\n")


def insert():
    global curr
    global selected
    if curr != selected.get():
        refresh()
        curr = selected.get()
    switcher = {
        0: si(hashTable, str(txt.get())),
        1: li(_hashTable, str(txt.get())),
        2: qi(_hashTable, str(txt.get())),
        3: di(_hashTable, str(txt.get()))
    }
    switcher.get(curr)
    display()
    return


btn = Button(window, text="Insert", command=insert)
lbl_ = Label(window, text="")
lbl0 = Label(window, text="0->" + dis[0], font=("Arial", 14))
lbl1 = Label(window, text="1->" + dis[0], font=("Arial", 14))
lbl2 = Label(window, text="2->" + dis[0], font=("Arial", 14))
lbl3 = Label(window, text="3->" + dis[0], font=("Arial", 14))
lbl4 = Label(window, text="4->" + dis[0], font=("Arial", 14))
lbl5 = Label(window, text="5->" + dis[0], font=("Arial", 14))
lbl6 = Label(window, text="6->" + dis[0], font=("Arial", 14))
lbl7 = Label(window, text="7->" + dis[0], font=("Arial", 14))
lbl8 = Label(window, text="8->" + dis[0], font=("Arial", 14))
lbl9 = Label(window, text="9->" + dis[0], font=("Arial", 14))
lbl10 = Label(window, text="10->" + dis[0], font=("Arial", 14))

lbl.grid(column=0, row=0)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)
rad4.grid(column=3, row=1)
txt.grid(column=0, row=2)
btn.grid(column=1, row=2)
lbl_.grid(column=0, row=3)
lbl0.grid(column=0, row=4)
lbl1.grid(column=0, row=5)
lbl2.grid(column=0, row=6)
lbl3.grid(column=0, row=7)
lbl4.grid(column=0, row=8)
lbl5.grid(column=0, row=9)
lbl6.grid(column=0, row=10)
lbl7.grid(column=0, row=11)
lbl8.grid(column=0, row=12)
lbl9.grid(column=0, row=13)
lbl10.grid(column=0, row=14)

window.mainloop()
