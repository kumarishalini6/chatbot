from tkinter import *


root=Tk()
root.title("New file")
root.config(background="powder blue")
root.geometry("300x300")
root.minsize(300,300)
root.maxsize(500,500)
Label(root,text="Hii ! This is your new page",fg="black",bg="powder blue",font=("arial",15,'bold')).pack()


root.mainloop()