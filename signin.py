from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as mb

def Back():
    Back=mb.askyesno("canteen management system","confirm you wnat to exit")
    if Back>0:
        root.destroy()
        return

def submit():
    if e1.get()=="" or e2.get()=="":
        mb.showerror("error","you need to fill the form")
    else:
        root.destroy()
        import index    

root=Tk()
root.title("bot project 2")
root.geometry("1280x720")
root.resizable(0,0)

photo=ImageTk.PhotoImage(file="max.jpg")
photo_image=Label(image=photo).place(x=0,y=0,relheight=1,relwidth=1)
frame=Frame(root,bg="gray").place(x=325,y=86,width=625,height=540)
Label(frame,text="Entry Information",fg="white",bg="gray",font=("arial",30,'bold')).place(x=472,y=70)
Button(frame,text="Back",bg="darkorange",fg="white",width=8,height=1,font=("arial",12,'bold'),command=Back).place(x=338,y=100)
Button(frame,text="Submit",bg="darkorange",fg="white",width=12,height=1,font=("arial",20,'bold'),command=submit).place(x=690,y=500)

Label(frame,text="Enter your name",font=("arial",25,'bold'),fg="darkorange",bg="gray").place(x=365,y=180)
e1=Entry(frame,font=("arial",25),width=29)
e1.place(x=380,y=250,height=50)
Label(frame,text="Enter your Email",font=("arial",25,'bold'),fg="darkorange",bg="gray").place(x=365,y=335)
e2=Entry(frame,font=("arial",25),width=29)
e2.place(x=380,y=400,height=50)

root.mainloop()
