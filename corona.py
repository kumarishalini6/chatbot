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
    
    "what is a novel coronavirus",
    "a novel coronavirus ia a new coronavirus that has bben previously identified. The virus causing coronavirus disease 2019 (COVID-19), is not the same as the coronaviruses that commonly circulate among humans and cause mild illness, like the common cold.",
    
    "how does the virus spread",
    "The virus that causes COVID-19 is thought to spread mainly from person to person, mainly through respiratory droplets produced when an infected person coughs, sneezes, or talks. These droplets can land in the mouths or noses of people who are nearby or possibly be inhaled into the lungs. Spread is more likely when people are in close contact with one another (within about 6 feet).",
    
    "wii warm weather stop outbreak of covid-19",
    "It is not yet known whether weather and temperature affect the spread of COVID-19. Some other viruses, like those that cause the common cold and flu, spread more during cold weather months but that does not mean it is impossible to become sick with these viruses during other months.  There is much more to learn about the transmissibility, severity, and other features associated with COVID-19 and investigations are ongoing.",

    "what is community spread",
    "Community spread means people have been infected with the virus in an area, including some who are not sure how or where they became infected. Each health department determines community spread differently based on local conditions. For information on community spread in your area, please visit your health department’s website.​",
    

    "tell me something about corona",
    "Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.  Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease,   diabetes,   chronic respiratory disease,   and cancer are more likely to develop serious illness.",

    "what are the preventions",
    "To prevent infection and to slow transmission of COVID-19, do the following:  Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub.Maintain at least 1 metre distance between you and people coughing or sneezing.Avoid touching your face.Cover your mouth and nose when coughing or sneezing.Stay home if you feel unwell.",
    
    "what are the symptoms",
    "Most common symptoms: fever.  dry cough. tiredness.  Serious symptoms:   difficulty breathing or shortness of breath.   chest pain or pressure.  loss of speech or movement.",

    "",
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
    import phy

def Next():
    root.destroy()
    import his 
    
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
root.title("math bot")
menu=Menu(root)
root.config(menu=menu)
root.geometry("870x750")
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
color.add_command(label="powder blue",command=color_blue)
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


f1=Frame(root,bd=20,bg="orange",relief=RIDGE).place(x=0,y=0,relwidth=1,relheight=1)

photo=ImageTk.PhotoImage(file="covid.jpeg")
photo_image=Label(image=photo).place(x=20,y=20,heigh=200)
Label(f1,text="Learn about corona with bot",fg="white",bg="orange",font=("arial",25,'bold')).place(x=340,y=20,height=200)
Label(f1,bg="white").place(x=20,y=222,height=3,width=830)
f2=Frame(f1,bd=14,bg="orange",relief=RIDGE).place(x=20,y=229,width=830,height=400)
f3=Frame(f1,bd=10,bg="orange",relief=RIDGE).place(x=20,y=633,height=96,width=830)

def chatting():
    quary=e1.get()
    answer_from_bot=bot.get_response(quary)
    textarea.insert(END,"\nyou :" + quary)
    textarea.insert(END,"\nsaturday :"+ str(answer_from_bot))
    speak(answer_from_bot)
    e1.delete(0,END)
    textarea.yview(END)

scrollbar = Scrollbar(f2)
scrollbar.place(x=818,y=243,height=371)

textarea = Text(f2, yscrollcommand = scrollbar.set,bg="cornsilk" )

textarea.place(x=34,y=243,width=782,height=371)
scrollbar.config( command = textarea.yview )

e1=Entry(f3,fg="black",font=("arial",20),bg="cornsilk")
e1.place(x=30,y=643,width=670,height=77)
Button(f3,text="Enter",fg="white",bg="darkorange",font=("arial",15,'bold'),bd=7,command=chatting).place(x=720,y=643,height=75,width=120)

Button(f1,text="Back",fg="white",bg="gray",command=Back).place(x=20,y=20)
Button(f1,text="Next",fg="white",bg="gray",command=Next).place(x=810,y=22)


root.mainloop()