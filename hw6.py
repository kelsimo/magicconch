#I had an idea in mind and didn't need outside resources, I hope that's okay.
# Magic Conch Shell (from Spongebob). Functions like a magic 8 ball.

import random
from tkinter import *
win = Tk()
win.title("Ask the Magic Conch")
win.geometry('500x350') #window dimensions
win.resizable(0, 0)
#image background
img = PhotoImage(file="magicconch.PNG") #image has to be png!
label =Label(win, image=img, width=500, height=350)
label.place(x=0, y=0)

typing = Entry(win)
typing.place(x=100, y=250, width=250, height=24) #entry box

responses = [''] #List of responses

def submit(): #randomizes responses and prints them
    answer = random.choice(responses)
    label2.configure(text="The Magic Conch says: " + str(answer))

label = Label(win, text = "Consult the Magic Conch:", font=("Arial", 24), fg="#CE9BE1")
label.place(x=15, y=75) #title label

label2 = Label(win, text =" ", font=("Arial", 16), fg ="white", bg="#CE9BE1")
label2.place(x=15, y=120) #label to hold the response print

button1= Button(win, text ="Ask", fg='white', bg='#CE9BE1', command=submit)
button1.place(x=355,y=250) #submit button


win.mainloop()