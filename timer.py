from tkinter import Tk
import time
import tkinter as tk
from tkinter import *
import tkinter 
import os
from win10toast import ToastNotifier
import tkinter as Tk
import pyperclip
import pyautogui

window = tk.Tk()
n = ToastNotifier()

window.title("Main Timer")

window.resizable(width = False, height = False)

window.geometry("300x150")

label=tk.Label(window,text="Stop video after")
label.pack()

entry=tk.Entry(width=20 , justify="center")
entry.pack()

label=tk.Label(window,text="seconds.")
label.pack()

def butontrigger2():
    x = entry.get()
    def countdown(t):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        window3 = tk.Tk()

        n = ToastNotifier()

        pyautogui.press("space")

        window3.title("Are You Want To Close System?")
        
        window3.resizable(width = False, height = False)
        
        window3.geometry("350x190")
        
        def yes():
            os.system("shutdown /s /t 10")
            n.show_toast("Timer Warning", "Shut down function triggered. Your computer will shut down in 10 seconds.", duration = 5)
        
        def no():
            window3.destroy()
            window.destroy()
        
        b2=tkinter.Button(window3 , text="Yes",bg="green",command=yes , width=70 , height=4 , font="Calibri 15")
        b2.pack()
        
        b1 = tk.Button(window3, text="No", bg="red" , command=no , width=70 , height=5 , font="Calibri 15")
        b1.pack()
        
        window3.mainloop()

    t = (x)
    countdown(int(t))
    
b2=tk.Button(text="Start",bg="black",fg="white",font="Arial 14 bold",command=butontrigger2)
b2.pack()

def openfile():
    window2=Tk.Tk()

    window2.title("Converting minutes and hours to seconds")
    window2.resizable(width=False , height=False)
    window2.geometry("400x120")
    
    l1=Tk.Label(window2 , text="Please enter hour;")
    l1.pack()
    
    hourentry=Tk.Entry(window2 , width=30 , justify="center")
    hourentry.pack()
    
    l2=Tk.Label(window2 , text="Please enter minute;")
    l2.pack()
    
    minentry=Tk.Entry(window2 , width=30 , justify="center")
    minentry.pack()
    

    def enter():
        window2.geometry("400x250")
        hour=hourentry.get()
        min=minentry.get()
        minson = (int(min)*60)
        hourson=(int(hour)*3600)
        last=(int(minson) + (int(hourson)))
        space=Tk.Label(window2 , text=" ")
        space.pack()
        lastlabel=Tk.Label(window2 ,  text=(last) , font="Calibri 20")
        lastlabel.pack()
        secondlabel=Tk.Label(window2 , text="seconds.")
        secondlabel.pack()
        
        def copy():
            pyperclip.copy(last)
            copyb.config(text="Copied" , state="disabled")

        copyb=Tk.Button(window2 , text="Copy" , command=copy)
        copyb.pack()
        enter.config(state="active")
        
    enter=Tk.Button(window2 , text="Confirm" , command=enter)
    enter.pack()
    
    window2.mainloop()

openb=tk.Button(window , text="I have only minutes and hours" , command=openfile)
openb.pack()

window.mainloop()