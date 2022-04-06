from tkinter import *
from tkinter import messagebox

window=Tk()
window.withdraw()

messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")
messagebox.askokcancel("Python","Would you like to save the data?")
messagebox.askretrycancel("Title","Installation failed, try again?")
if messagebox.askyesno("Title","Do you want to save?")==True:
    print("Yes")
elif messagebox.askyesno("Title","Do you want to save?")==False:
    print("No")

window.deiconify()
window.destroy()
window.quit()