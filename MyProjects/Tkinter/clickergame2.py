from tkinter import *

window = Tk()
window.title("ClickerGame")
window.geometry("2222x2222")
window.configure (background="black")

a=0
def click():
    global a
    global l1
    a=a+1
    print(a)
    l1.destroy()
    l1 = Label(window, text = "Score:"+ str(a), bg="black", fg="white", font="none 12 normal", anchor=E)
    l1.grid(row = 0, column = 1)

b=0
c=20
def PlusOne():
    global b
    global a
    global c
    if a>=c:
        a=a-20
        b=b+1
        c=c+12

l1 = Label(window, text = "Score:"+ str(a), bg="black", fg="white", font="none 12 normal", anchor=E)

b1 = Button(window, text = "Click", bg="black", fg="white", font="none 24 bold", command=click, anchor=CENTER)

l2= Button(window, text = "+1 Forver", bg="black", fg="white", font="none 12 normal", command=PlusOne, anchor=E)


l1.grid(row = 0, column = 1)
b1.grid(row = 1, column = 2, pady=275, padx=550)
l2.grid(row=0, column=3)

print("whi")

def cool():
    global a
    global l1
    a=a+b
    l1.destroy()
    l1 = Label(window, text = "Score:"+ str(a), bg="black", fg="white", font="none 12 normal", anchor=E)
    l1.grid(row = 0, column = 1)
    window.after(1000, cool)

window.after(1000, cool)

mainloop()