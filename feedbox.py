from tkinter import *
import tkinter.messagebox as mb

def Cli():
    mb.showinfo("thanks","your feedback is submited")
    


root=Tk()

root.title("Feedback")
root.config(background="pink")
root.geometry("400x300")
root.maxsize(400,400)
Label(root,text="Feedback form",fg="white",font=("arial",30,'bold'),bg="pink").pack()
Label(root,text="Name",fg="white",bg="pink",font=("arial",20,'bold')).place(x=90,y=90)
e1=Entry()
e1.place(x=200,y=100)
Button(root,text="submit",fg="black",bg="red",command=Cli).place(x=150,y=150)

root.mainloop()