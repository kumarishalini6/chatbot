from tkinter import *

def Back():
    root.destroy()
    import signin

def Chat():
    root.destroy()
    import bot2    



def His():
    root.destroy()
    import his    

def Tech():
    root.destroy()
    import tech

def Phy():
    root.destroy()
    import phy

def Covid():
    root.destroy()
    import corona      

def Math():
    root.destroy()
    import maths           

root=Tk()
root.title("content page")
root.config(background="purple")
root.geometry("600x785")
root.resizable(0,0)

Label(root,text="Select Topic",font=("arial",50,'bold'),bg="purple",fg="cornsilk").place(x=105,y=80)

Label(root,text="Select Topic",font=("arial",50,'bold'),bg="purple",fg="cornsilk").place(x=105,y=80)
Label(root,text="1.    Simple Chat",font=("arial",25,'bold'),bg="purple",fg="darkorange").place(x=6,y=190)
Label(root,text="2.    About  Technology",font=("arial",25,'bold'),bg="purple",fg="darkorange").place(x=6,y=250)
Label(root,text="3.    About  Mathmatics",font=("arial",25,'bold'),bg="purple",fg="darkorange").place(x=6,y=310)
Label(root,text="4.    About  Physics",font=("arial",25,'bold'),bg="purple",fg="darkorange").place(x=6,y=370)
Label(root,text="5.    About  Corona",font=("arial",25,'bold'),bg="purple",fg="darkorange").place(x=6,y=430)
Label(root,text="6.    About  History",font=("arial",25,'bold'),bg="purple",fg="darkorange").place(x=6,y=500)

Button(root,text=" ≫ ",bg="darkorange",command=Chat).place(x=520,y=195)
Button(root,text=" ≫ ",bg="darkorange",command=Tech).place(x=520,y=255)
Button(root,text=" ≫ ",bg="darkorange",command=Math).place(x=520,y=315)
Button(root,text=" ≫ ",bg="darkorange",command=Phy).place(x=520,y=375)
Button(root,text=" ≫ ",bg="darkorange",command=Covid).place(x=520,y=435)
Button(root,text=" ≫ ",bg="darkorange",command=His).place(x=520,y=505)


Button(root,text="Back",bg="darkorange",fg="white",font=("arial",12,'bold'),command=Back).place(x=30,y=10)


root.mainloop()



