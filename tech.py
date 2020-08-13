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
    
    "what is technology",
    "Technology is the sum of techniques, skills, methods, and processes used in the production of goods or services or in the accomplishment of objectives, such as scientific investigation.",
    
    "what is purpose of technology",
    "The purpose of technology is to enable the effective sharing of data to address some of society's biggest challenges and help individuals and organizations be more innovative, efficient, and productive.",

    "advantages of technology",
    "Speed, Efficiency, and Agility. ...Storage and Sharing. ...Mobility and Remote Connectivity. ...Automation. ...Communication.  The increased automation of manufacturing and many other jobs, thanks to computers, means greater efficiency, less people doing boring repetitive jobs, and an increase in flexibility regarding work times.",

    "disadvantages of technology in education",
    " Disadvantages of Technology in Education   It can be distracting to students. ...It can disconnect students from face-to-face relationships. ...It can make it easier to cheat. ...It could put some students at a disadvantage. ...It could cause students to use unreliable resources for learning.",
    
    "what is information technology",
    "Information technology (IT) is the use of any computers, storage, networking and other physical devices, infrastructure and processes to create, process, store, secure and exchange all forms of electronic data. ... The commercial use of IT encompasses both computer technology and telephony.",

    "What are the features of information technology?",
    "Important Features of Information Technology   The development of Information Technology has made education system simpler, easier, and widespread. ...  Diffusion of e-governance on a large scale.   Participation of public in governance and policy making.   Fast economic development.   Development of remote areas.",

    "What is the main function of information technology?",
    "Information technology (IT) is the use of any computers, storage, networking and other physical devices, infrastructure and processes to create, process, store, secure and exchange all forms of electronic data.",
    

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
    import bot2


def Next():
    root.destroy()
    import  maths   
    
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
    textarea.delete(1.0,END)
    #textarea.config(state=DISABLED)

root=Tk()
root.title("technology bot")
menu=Menu(root)
root.config(menu=menu)
root.geometry("800x750")
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



frame=Frame(root,bg="blue",bd=18,relief=RIDGE).place(x=0,y=0,relwidth=1,relheight=1)
photo=ImageTk.PhotoImage(file="images.jpeg")
photo_image=Label(image=photo).place(x=350,y=20)
Label(frame,text="Learn tecnology ",fg="white",bg="blue",font=("arial",30,'bold')).place(x=20,y=70)
Label(frame,text="  with bot",fg="white",bg="blue",font=("arial",30,'bold')).place(x=20,y=137)
Label(frame,bg="white").place(x=20,y=262,width=745,height=2)
f1=Frame(frame,bd=8,bg="skyblue",relief=RIDGE).place(x=20,y=267,width=765,height=370)
f2=Frame(frame,bd=8,bg="skyblue",relief=RIDGE).place(x=20,y=640,width=765,height=87)
e1=Entry(f1,fg="black",font=("arial",20),bg="cornsilk")
e1.place(x=26,y=649,width=580,height=73)

scrollbar = Scrollbar(f1)
scrollbar.place(x=759,y=275,height=354)

textarea = Text(f1, yscrollcommand = scrollbar.set,bg="cornsilk" )

textarea.place(x=28,y=275,width=730,height=354)
scrollbar.config( command = textarea.yview )

Button(f1,text="Enter",fg="black",bg="powder blue",font=("arial",15,'bold'),bd=7,command=chatting).place(x=640,y=649,height=72,width=100)
Button(frame,text="Back",fg="white",bg="darkorange",command=Back).place(x=20,y=20)
Button(frame,text="Next",fg="white",bg="darkorange",command=Next).place(x=740,y=22)


root.mainloop()