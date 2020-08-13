from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3
import speech_recognition as sr 
import threading

from tkinter import *
from PIL import ImageTk

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
    "what is your name?",
    "my name is saturday"
    "how are you?",
    "i am fine,how are you",
    "what are you doing?",
    "nothing,what are you doing",
    "nothing,i am geeting bored"
    "can i help you",
    "what can you do for me",
    "anything you want",
    "ok thanks",
    "in which language do you speak",
    "i am speaking in english!!"

]

trainer=ListTrainer(bot)
trainer.train(conversation)

def Back():
    root.destroy()
    import index

def Go():
    root.destroy()
    import tech  

root=Tk()
root.title("my bot saturday")
root.config(background="skyblue")
root.geometry("848x760")
root.resizable(0,0)

btn=Button(root,text="Back",fg="white",font=("verdana",18),bg="powder blue",command=Back).place(x=12,y=2)
btn=Button(root,text="Next",fg="white",font=("verdana",18),bg="powder blue",bd=4,command=Go).place(x=700,y=2)

Label(root,text="Simple Chatting",font=("arial",30,'bold'),fg="white",bg="skyblue").pack()

photo= PhotoImage(file="bot2.png")
photo_image=Label(image=photo).place(x=0,y=45,height=240)

photo3= PhotoImage(file="bot.png")
photo3_image=Label(image=photo3).place(x=420,y=45,height=240)

photo2=  ImageTk.PhotoImage(file="bot5.jpg")
photo2_image=Label(image=photo2).place(x=200,y=45,height=240)

Label(root,bg="black").place(x=0,y=290,relwidth=1,height=6)


             

def lets_chatting_with_me():
    quary=e1.get()
    answer_from_bot=bot.get_response(quary)
    textarea.insert(END,"\nyou :" + quary)
    textarea.insert(END,"\nsaturday :"+ str(answer_from_bot))
    speak(answer_from_bot)
    e1.delete(0,END)
    textarea.yview(END)

frame=Frame(root,bd=20)
frame.place(x=9,y=297,width=830,height=400)
f1=Frame(frame,bd=15,relief=RIDGE)
f1.place(x=-17,y=-17,width=830,height=400)
scrol_y=Scrollbar(f1,orient=VERTICAL)
textarea=Text(f1,yscrollcommand=scrol_y.set,font=("arial",15))
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()

e1=Entry(root,font=("verdana",20,))
e1.place(x=10,y=699,width=640,height=55)

btn=Button(root,text="summit",font=("verdana",18,'bold'),bg="powder blue",bd=4,command=lets_chatting_with_me).place(x=682,y=699)




root.mainloop()