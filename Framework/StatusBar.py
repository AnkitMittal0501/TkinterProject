from tkinter import  *

def doNothing():
    print("Do Nothing please")

root=Tk()

menu=Menu(root)
root.config(menu=menu)

submenu=Menu(menu)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Project...",command=doNothing)
submenu.add_command(label="New ...",command=doNothing)
submenu.add_separator()

submenu.add_command(label="Exit",command=doNothing)
editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)

#####Toolbar creation
toolbar=Frame(root,bg="blue")

insertButton = Button(toolbar,text="Insert Image",command=doNothing)
insertButton.pack(side=LEFT,padx=2,pady=2)
printBut=Button(toolbar,text="Print ",command=doNothing)
printBut.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)

# ***Status Bar like loading and something
# bd means border and Sunken relief means placed like a
# status bar
status=Label(root,text="File saved",bd=2,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)
root.mainloop()