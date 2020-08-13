from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3

from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as mb 

eng=pyttsx3.init()
voices=eng.getProperty('voices')
print(voices)

eng.setProperty('voice',voices[0].id)

def speak(word):
    eng.say(word)
    eng.runAndWait()


bot=ChatBot("saturday")

conversation=[
    "hii",
    "hii shalini",
    
   "who is akbar",
   " Akbar was the son of 2nd Mughal Emperor Humayun. Akbar became the de jure king in 1556 at the age of 13 when his father died.",
    
   "what is full name of akbar",
   "Akbar,  in  full  Abū  al - Fatḥ  Jalāl  al- Dīn  Muḥammad  Akbar,",

   "when was akbar born",
   "he was born on October 15, 1542, Umarkot now in Sindh province, Pakistan  and —died  October 25, 1605, Agra, India)",

   "who killed akbar",
   "As per official text, no one killed Akbar, he died of dysentery, around ten days after his 63rd birthday in Agra.",

   "tell me something about jahangir",
   "jahangir was the son of akbar, his full name is  Nur - ud- din  Muhammad  Salim  born on 31 August 1569  and died on  – 28 October 1627  he was the fourth Mughal Emperor, who ruled from 1605 until his death in 1627. His imperial name (in Persian), means 'conqueror of the world', 'world-conqueror' or 'world-seizer'",
    

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
    import corona

def Next():
    root.destroy()
    import bye   


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
    textarea.config(background="cornsilk")
    e1.config(background="cornsilk")
    background="cornsilk" 

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
   # textarea.delete(1.0,END)
    textarea.config(state=DISABLED)

    
root=Tk()
root.title("history bot")
menu=Menu(root)
root.config(menu=menu)
root.geometry("890x770")
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
font.add_command(label="verdana",command=font_verdana)
font.add_command(label="Times",command=font_Times)
font.add_command(label="System",command=font_System)

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




frame=Frame(root,bg="gray",bd=18,relief=RIDGE).place(x=0,y=0,relwidth=1,relheight=1)
photo=ImageTk.PhotoImage(file="history.jpg")
photo_image=Label(image=photo).place(x=19,y=15,width=853)
f1=Frame(frame,bg="gray",bd=9,relief=RIDGE).place(x=19,y=330,height=360,width=853)
f2=Frame(frame,bg="gray",bd=9,relief=RIDGE).place(x=19,y=691,height=60,width=853)
e1=Entry(f2,bg="cornsilk",fg="black",font=("arial",25))
e1.place(x=26,y=700,width=650)


def chatting():
    quary=e1.get()
    answer_from_bot=bot.get_response(quary)
    textarea.insert(END,"\nyou :" + quary)
    textarea.insert(END,"\nsaturday :"+ str(answer_from_bot))
    speak(answer_from_bot)
    e1.delete(0,END)
    textarea.yview(END)

scrollbar = Scrollbar(f1)
scrollbar.place(x=843,y=340,height=341)

textarea = Text(f1, yscrollcommand = scrollbar.set,bg="cornsilk" )

textarea.place(x=28,y=340,width=812,height=341)
scrollbar.config( command = textarea.yview )

Button(f2,bg="cornsilk",fg="black",font=("arial",15,'bold'),text="Enter",command=chatting).place(x=740,y=700,width=100)
btn=Button(frame,text="Back",fg="white",bg="darkorange",font=("arial",15),command=Back).place(x=23,y=22)
btn=Button(frame,text="Next",fg="white",bg="darkorange",font=("arial",15),command=Next).place(x=803,y=22)


root.mainloop()