
from tkinter import *
from random import random

win=Tk()
win.configure(bg="light slate gray")
num = int(100*random())
# flag = 0
win.geometry("300x150")

def cal_sum():
    x=int(a.get())

    if(flag==10):
        label.config(text="You Lost :-( :-(")
        a.delete(first=0, last=END)
    
    if(x==num):
        label.config(text=f"Congo!! You won :-) :-)\nYou completed the game in {flag} gussess.")
        a.delete(first=0, last=END)
        
    elif (x > num):
        label.config(text="The number you entered is greater.")
        a.delete(first=0, last=END)
        flag += 1

    elif (x < num):
        label.config(text="The number you entered is smaller")
        a.delete(first=0, last=END)
        flag += 1

Label(win, text="Enter Number", font=('Calibri 10'), bg="misty rose").pack()
a=Entry(win, width=35)
a.pack()

label=Label(win, text="Start Guessing", font=('Calibri 15'))
label.pack(pady=20)
# label.config(text="Start Guessing")

Button(win, text="GUESS", command=cal_sum, bg='turquoise').pack()

win.mainloop()