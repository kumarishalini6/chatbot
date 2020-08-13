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
    
    "what is physic",
    "The science of matter and energy, and their properties and interactions in fields including mechanics, acoustics, optics, heat, electricity, magnetism, radiation, and atomic and nuclear science. Physics is the science of how things work.",
    
    "what is newton's first law",
    "Newton's first law of motion is often stated as  An object at rest stays at rest and an object in motion stays in motion with the same speed and in the same direction unless acted upon by an unbalanced force.",
    
    "what is newton's third law of motion",
    "According to Newton's third law of motion, whenever two objects interact, they exert equal and opposite forces on each other. This is often worded as 'every action has an equal and opposite reaction.",
    
    "what is magnetic field",
    "The magnetic field is the area around a magnet in which there is magnetic force.   Moving electric charges can make magnetic fields. ... In physics, the magnetic field is a field that passes through space and which makes a magnetic force move electric charges and magnetic dipoles.",

    "what is light",
    "Light is a form of electromagnetic radiation with a wavelength which can be detected by the human eye",

    "why light is important",
    "It acts as a catalyst during photosynthesis in plants, and it provides sustenance for the survival of plankton in the oceans. Both these forms of herbal life go on to provide nutrition to many species, including human beings. Light is the most important tool of guidance.",

    "what are the properties of light",
    "The properties of light:   Reflection of light.    Refraction of light.   Diffraction of light.   Interference of light.   Polarization of light.   Dispersion of light.   Scattering of light.",

    

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
    import maths

def Next():
    root.destroy()
    import corona  
    
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
root.title("physic bot")
menu=Menu(root)
root.config(menu=menu)
root.geometry("1300x750")
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

frame=Frame(root,bd=18,bg="gray",relief=RIDGE).place(x=0,y=0,relwidth=1,relheight=1)
photo=ImageTk.PhotoImage(file="physic.jpg")
photo_image=Label(image=photo).place(x=15,y=15,width=1268,height=720)
f2=Frame(frame,bd=12,bg="gray",relief=RIDGE).place(x=730,y=150,width=500,height=400)
f3=Frame(frame,bd=12,bg="gray",relief=RIDGE).place(x=730,y=550,width=500,height=100)

scrollbar = Scrollbar(f2)
scrollbar.place(x=1200,y=163,height=374)

textarea = Text(f2, yscrollcommand = scrollbar.set,bg="cornsilk" )

textarea.place(x=743,y=163,width=452,height=374)
scrollbar.config( command = textarea.yview )

e1=Entry(f3,fg="black",font=("arial",20),bg="cornsilk")
e1.place(x=742,y=562,width=330,height=76)
Button(f3,text="Enter",fg="black",bg="powder blue",font=("arial",20,'bold'),bd=7,command=chatting).place(x=1095,y=565,height=70,width=120)

Button(frame,text="Back",fg="white",bg="darkorange",command=Back,font=("arial",13)).place(x=20,y=20)
Button(frame,text="Next",fg="white",bg="darkorange",command=Next,font=("arial",13)).place(x=1190,y=22)


root.mainloop()