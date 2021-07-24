# Source: https://data-flair.training/blogs/python-rock-paper-scissors-game/
#Programming regular Rock-Paper-Scissors is easy enough - using only the terminal
#as well as print statements, anyway. This program uses a GUI and buttons to get things done.
from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('DataFlair-Rock,Paper,Scissors')
root.config(bg = 'seashell3')

Label(root, text = 'Rock, Paper, Scissors', font='arial 20 bold', bg = 'seashell2').pack()
user_take = StringVar()
Label(root, text = 'Choose one: rock, paper, scissors', font='arial 15 bold', bg='seashell2').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)

comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('Tie, both contenders picked the same choice')
    elif user_pick == 'rock':
        if comp_pick == 'paper':
            Result.set('You lose, paper beats rock!')
        else:
            Result.set('You win! Rock beats scissors!')
    elif user_pick == 'paper':
        if comp_pick == 'scissors':
            Result.set('You lose, scissors beats paper!')
        else:
            Result.set('You win! Paper beats rock!')
    elif user_pick == 'scissors':
        if comp_pick == 'rock':
            Result.set('You lose, rock beats scissors!')
        else:
            Result.set('You win! Scissors beats paper!')
    else:
        Result.set('Invalid Choice: Choose another one')
        
def Reset():
    Result.set("") 
    user_take.set("")
    
def Exit():
    root.destroy()
    
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


root.mainloop()
        