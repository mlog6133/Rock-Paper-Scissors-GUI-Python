'''
NAME: MARQUIS LOGAN

DATE: November 25, 2022

DESCRIPTION: SUCCESSFULLY RUN A ROCK PAPER SHOOT GAME IMPLEMENTING A GUI (GRAPHIC USER INTERFACE) USING TKINTER
             RATHER THAN EASYFRAME
'''

from tkinter import *
import random

#create tkinter
win= Tk()

# window Size
win.geometry("575x450")

# title of the window
win.title("RPS GAME")

# RPS OPTIONS FOR COMPUTER
computer_options = {
   "0":"Rock",
   "1":"Paper",
   "2":"Scissors"
}


#rock function
def isrock():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result =  "Draw"
   elif value=="Scissors":
      match_result = "Victory! You Won"
   else:
      match_result = "Computer Wins"
   label.config(text = match_result)
   l1.config(text = "Rock")
   l3.config(text =value)
   

#paper function
def ispaper():
   value = computer_options[str(random.randint(0, 2))]
   if value == "Paper":
      match_result = "Draw"
   elif value=="Scissors":
      match_result = "Computer Win"
   else:
      match_result = "You won!"
   label.config(text = match_result)
   l1.config(text = "Paper")
   l3.config(text = value)
   

# scissors function
def isscissor():
   value = computer_options[str(random.randint(0,2))]
   if value == "Rock":
      match_result = "Computer Win"
   elif value == "Scissor":
      match_result = "Match Draw"
   else:
      match_result = "You won!"
   label.config(text = match_result)
   l1.config(text = "Scissor")
   l3.config(text = value)
  




#labeling the frame
labelframe= LabelFrame(win, text= "VSU Rock Paper Scissors", font= ('Century 20 bold'),labelanchor= "n",bd=5,bg= "white",width= 600, height= 450, cursor= "target")
labelframe.pack(expand= True, fill= BOTH)

#player labels
l1= Label(labelframe, text="Player", font= ('Helvetica 18 bold'), bg='white')
l1.place(relx= .18, rely= .1)

#label for 'VS'
l2= Label(labelframe, text="VS", font= ('Helvetica 18 bold'), bg="white")
l2.place(relx= .45, rely= .1)

#computer label
l3= Label(labelframe, text="Computer", font= ('Helvetica 18 bold'), bg='white')
l3.place(relx= .65, rely= .1)

# conditions label
label= Label(labelframe, text="", font=('Coveat', 25,'bold'), bg= "white")
label.pack(pady=150)

#buttons for rock paper scissors
b1= Button(labelframe, text= "Rock", font= 10, width= 7, command= isrock)
b1.place(relx=.25, rely= .62)
b2= Button(labelframe, text= "Paper", font= 10, width= 7 ,command= ispaper)
b2.place(relx= .41,rely= .62)
b3= Button(labelframe, text= "Scissor", font= 10, width= 7, command= isscissor)
b3.place(relx= .58, rely= .62)

#main loop call
win.mainloop()


