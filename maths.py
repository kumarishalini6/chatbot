from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3

from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as mb 

eng=pyttsx3.init()
voices=eng.getProperty('voices')
print(voices)

eng.setProperty('voice',voices[1].id)

def speak(word):
    eng.say(word)
    eng.runAndWait()


bot=ChatBot("saturday")

conversation=[
    "hii",
    "hii shalini",
    
    "what is natural number",
    "A natural number is an integer greater than 0. Natural numbers begin at 1 and increment to infinity: 1, 2, 3, 4, 5, etc.",

    "what is integer",
    "Integers are like whole numbers, but they also include negative numbers ... but still no fractions allowed!",

    "20 % of 2 is equal to",
    " 0.4",
    
    "2+2=",
    "4",
    
    "2*3=",
    "6",

    "|-26|",
    "26",

    "3+2*(8-3)",
    "13",
    
    "area of square",
    "l^2",
    

    "is 4 is square root of 2",
    "yes",

    "How do we use calculus in real life?",
    "Calculus is used to determine the growth rate of bacteria when there is a change in temperature with time.Calculus is used to find with how much speed or velocity the object is moving.We can also use calculus to maximize or minimize the value.To find the area or volume of the solid, calculus is used.",
    
    
]

trainer=ListTrainer(bot)
trainer.train(conversation)


def About():
    mb.showinfo("welcome","you are opening my about")
    print("This is my first menubar")

def Help():
    mb.showinfo("welcome","How can i help you, This is help box")    

def feedback():
    root.destroy()
    import feedbox    

def Exit():
    Exit=mb.askyesno("hello","confirm if you want to exit")
    if Exit>0:

        root.destroy()
        return
     

def New():
    mb.showinfo("welcome","You want new file")
    root.destroy()
    import new 

def Back():
    root.destroy()
    import tech

def Next():
    root.destroy()
    import phy    

def font_default():
    textarea.config(font=("arial",20))
    e1.config(font=("arial",20))
    font=("arial",20)

def  font_verdana():
    textarea.config(font=("verdana",35))
    e1.config(font=("verdana",35))
    font=("verdana",35)

def  font_Times():
    textarea.config(font=("Time",40))
    e1.config(font=("Time",40))
    font=("Time",40) 

def  font_System():
    textarea.config(font=("System",45))
    e1.config(font=("System",45))
    font=("System",45)

def color_default():
    textarea.config(background="powder blue")
    e1.config(background="powder blue")
    background="powder blue" 

def color_gray():
    textarea.config(background="gray")
    e1.config(background="gray")
    background="gray"

def color_blue():
    textarea.config(background="blue")
    e1.config(background="blue")
    background="blue"  

def color_pink():
    textarea.config(background="pink")
    e1.config(background="pink")
    background="pink"             
def clear_chat():
    textarea.config(state=NORMAL)
    textarea.delete(1.0,END)
    textarea.delete(1.0,END)
    #textarea.config(state=DISABLED)

    
root=Tk()
root.title("math bot")
menu=Menu(root)
root.config(menu=menu)
root.geometry("850x710")
root.resizable(0,0)

filemenu=Menu(menu)
menu.add_cascade(label="  File",menu=filemenu)
filemenu.add_command(label="New file",command=New)
filemenu.add_separator()
filemenu.add_command(label="Clear chat",command=clear_chat)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=Exit)

font=Menu(menu,tearoff=0)
font.add_command(label="default",command=font_default)
font.add_command(label="Times",command=font_Times)
font.add_command(label="System",command=font_System)
font.add_command(label="verdana",command=font_verdana)

color=Menu(menu,tearoff=0)
color.add_command(label="default",command=color_default)
color.add_command(label="gray",command=color_gray)
color.add_command(label="blue",command=color_blue)
color.add_command(label="pink",command=color_pink)

optionmenu=Menu(menu)
menu.add_cascade(label=" Options",menu=optionmenu)
optionmenu.add_cascade(label="Font",menu=font)
optionmenu.add_cascade(label="Color",menu=color)

optionmenu.add_separator()
optionmenu.add_command(label="Exit",command=Exit)

helpmenu=Menu(menu)
menu.add_cascade(label=" Help",menu=helpmenu)
helpmenu.add_command(label="View help",command=Help)
helpmenu.add_command(label="Send feedback",command=feedback)
helpmenu.add_separator()
helpmenu.add_command(label="About",command=About)

def chatting():
    quary=e1.get()
    answer_from_bot=bot.get_response(quary)
    textarea.insert(END,"\nyou :" + quary)
    textarea.insert(END,"\nsaturday :"+ str(answer_from_bot))
    speak(answer_from_bot)
    e1.delete(0,END)
    textarea.yview(END)

frame=Frame(root,bg="cadet blue",relief=RIDGE,bd=18).place(x=0,y=0,relwidth=1,relheight=1)
Label(frame,bg="cadet blue",fg="cornsilk",font=("arial",40,'bold'),text="Learn Math with bot").place(x=145,y=40)
photo=ImageTk.PhotoImage(file="math.jpg")
photo_image=Label(image=photo).place(x=50,y=110,height=490,width=744)
f1=Frame(frame,bg="cadet blue",relief=RIDGE,bd=9).place(x=50,y=590,width=744,height=99)

f2=Frame(frame,bd=10,bg="powder blue",relief=RIDGE).place(x=153,y=205,width=547,height=385)



scrollbar = Scrollbar(f2)
scrollbar.place(x=673,y=215,height=365)

textarea = Text(f2, yscrollcommand = scrollbar.set,bg="powder blue" )

textarea.place(x=163,y=215,width=509,height=365)
scrollbar.config( command = textarea.yview )

e1=Entry(f1,fg="black",font=("arial",20),bg="cornsilk")
e1.place(x=56,y=596,width=600,height=83)
Button(f1,text="Enter",fg="black",bg="powder blue",font=("arial",15,'bold'),bd=7,command=chatting).place(x=663,y=600,height=78,width=120)

Button(frame,text="Back",fg="white",bg="darkorange",command=Back).place(x=20,y=20)
Button(frame,text="Next",fg="white",bg="darkorange",command=Next).place(x=790,y=22)




root.mainloop()