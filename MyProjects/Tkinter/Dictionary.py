from tkinter import *
from PyDictionary import PyDictionary

cool=Tk()
cool.title("Dictionary")
cool.configure(background="white")

def exit():
    sys.exit(1)

def submit():
    word=e1.get()
    t1.delete(0.0, END)
    dictionary=PyDictionary()
    definition=dictionary.meaning(word)
    t1.insert(0.0, definition)
    e1.delete(0, END)

t1=Text(cool, width=18, height=2, wrap=WORD, padx=17, pady=50, font=("Helevita", 9))

l1=Label(cool, text="Charan's Dictionary", bg="white", font=("Helevita",9),)

l2=Label(cool, text="Word:", bg="white", font=("Helevita",9))

e1=Entry(cool)

b1=Button(cool, text="Submit", padx=39, command=submit, bd=2)
b2=Button(cool, text="Exit", padx=5, command=exit, bd=2)

t1.grid(row=3, column=0, columnspan=30, sticky=W)
l1.grid(row=0, column=0, columnspan=2)
e1.grid(row=1, column=1, sticky=W)
l2.grid(row=1, column=0, sticky=W)
b1.grid(row=2, column=1, sticky=W)
b2.grid(row=2, column=0, sticky=W)

cool.mainloop()