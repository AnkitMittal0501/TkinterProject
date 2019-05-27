from tkinter import *
import tkinter.messagebox
root=Tk()
# work as Alert
tkinter.messagebox.showinfo("WindowTitle","This is messageBox")
answer=tkinter.messagebox.askquestion("Confirmation Required....","Are you sure?")
if answer == "yes":
    print("Hay!!! Awesome")
else:
    print("Sorry!!!")
root.mainloop()