from tkinter import *
from PIL import ImageTk
import time
import datetime


def Next():
    root.destroy()
    import signin

root=Tk()
root.title("chatbot project 2")
root.geometry("770x760")
root.resizable(0,0)

Date1=StringVar()
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))


frame1=Frame(root,bg="black").place(x=0,y=0,relwidth=1,height=380)
Label(frame1,bg="black",fg="white",font=("arial",55,'bold'),text="Welcome").place(x=240,y=205)
Label(frame1,bg="black",fg="white",font=("arial",20),text="I am chatbot ! ").place(x=315,y=295)
Label(frame1,bg="black",fg="white",font=("arial",10),text="My name is saturday").place(x=335,y=333)



Label(frame1,bg="black",fg="darkorange",font=("arial",15,'bold'),textvariable=Date1).place(x=70,y=100)
Label(frame1,bg="black",fg="darkorange",font=("arial",15,'bold'),textvariable=Time1).place(x=610,y=100)

Button(frame1,text="Next",fg="white",bg="darkorange",font=("arial",15,'bold'),width=8,height=1,command=Next).place(x=650,y=20)

frame2=Frame(root,bg="blue").place(x=0,y=380,relwidth=1,height=380)
Label(frame2,bg="blue",fg="white",font=("arial",25,'bold'),text="Let's talk to bot").place(x=265,y=715)
photo=PhotoImage(file="chat.png")
photo_image=Label(image=photo).place(x=228,y=417)


root.mainloop()