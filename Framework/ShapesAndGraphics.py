from tkinter import *

root=Tk()
canvas=Canvas(root,width=200,height=100)
canvas.pack()
# first is x axis and y axis point

blackline=canvas.create_line(0,0,200,50)
# 100 means from bottom
redline=canvas.create_line(0,100,200,50,fill="red")
greenbox=canvas.create_rectangle(25,25,130,60,fill="green")
# delete redline
#canvas.delete(redline)
# delete everything on canvas
#canvas.delete(ALL)
root.mainloop()