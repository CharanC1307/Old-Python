from tkinter import *
import os.path

cool=Tk()
cool.title("Login")
cool.configure(background="white")

def exit():
    sys.exit(1)

def submit():
    global definition
    entered_text1=e1.get()
    entered_text2=e2.get()
    t1.delete(0.0, END)
    if os.path.exists(entered_text1):
        file = open(entered_text1)
        content = file.read()
        file.close()
        if content==entered_text2:
            definition="Good job."
        else:
            definition="Wrong Password"
    else:
        definition="Wrong username and Password. Please try again or register."
    t1.insert(0.0, definition)
    e1.delete(0, END)
    e2.delete(0, END)

t1=Text(cool, width=24, height=2, wrap=WORD, padx=12, font=("Helevita", 9))

l1=Label(cool, text="Username:", bg="white", font=("Helevita",9),)

l2=Label(cool, text="Password:", bg="white", font=("Helevita",9))

e1=Entry(cool)
e2=Entry(cool, show="•")

b1=Button(cool, text="Submit", padx=40, command=submit, bd=2)
b2=Button(cool, text="Exit", padx=20, command=exit, bd=2)

t1.grid(row=3, column=0, columnspan=2, sticky=W)
l1.grid(row=0, column=0, sticky=W)
e1.grid(row=0, column=1, sticky=W)
l2.grid(row=1, column=0, sticky=W)
e2.grid(row=1, column=1, sticky=W)
b1.grid(row=2, column=1, sticky=W)
b2.grid(row=2, column=0, sticky=W)

cool.mainloop()