from tkinter import *
from PIL import ImageTk

def Back():
    root.destroy()
    import his

root=Tk()
root.title("thanks")
root.geometry("441x380")
root.resizable(0,0)
photo=ImageTk.PhotoImage(file="cbot.jpg")
photo_image=Label(image=photo).pack()
Label(root,text="Thanks",font=("arial",26,'bold'),bg="white",fg="black").place(x=0,y=310,relwidth=1,height=70)
Button(root,text="back",bg="darkorange",fg="white",font=("arial",15),command=Back).place(x=10,y=10)
root.mainloop()