from tkinter import *
import os.path


cool=Tk()
cool.title("Login")
cool.configure(background="white")
cool.geometry("200x158")

login=Button(cool,text="Login", command=login,font=("Times New Roman",20, NORMAL),padx=53, pady=10, bd=5).pack()
register=Button(cool,text="Register", font=("Times New Roman",20, NORMAL),padx=40, pady=10, bd=5).pack()


def Exit():
    sys.exit(1)

def Submit():
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
    text1.insert(0.0, definition)
    e1.delete(0, END)
    e2.delete(0, END)

def Login():
    Exit()
    cool.geometry("200x200")
    text1=Text(cool, width=24, height=2, wrap=WORD, padx=12, font=("Helevita", 9))

    username=Label(cool, text="Username:", bg="white", font=("Helevita",9))

    password=Label(cool, text="Password:", bg="white", font=("Helevita",9))

    usernameE=Entry(cool)
    passwordE=Entry(cool, show="•")

    submit=Button(cool, text="Submit", padx=40, command=submit, bd=2)
    exit=Button(cool, text="Exit", padx=20, command=exit, bd=2)

    text1.grid(row=3, column=0, columnspan=2, sticky=W)
    l1.grid(row=0, column=0, sticky=W)
    e1.grid(row=0, column=1, sticky=W)
    l2.grid(row=1, column=0, sticky=W)
    e2.grid(row=1, column=1, sticky=W)
    b1.grid(row=2, column=1, sticky=W)
    b2.grid(row=2, column=0, sticky=W)

login=Button(cool,text="Login", command=Login,font=("Times New Roman",20, NORMAL),padx=53, pady=10, bd=5).pack()
register=Button(cool,text="Register", font=("Times New Roman",20, NORMAL),padx=40, pady=10, bd=5).pack()


cool.mainloop()
