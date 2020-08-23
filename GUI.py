import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont
window = tk.Tk()

def clickup():
    messagebox.showinfo("Message:","Button UP was clicked")

def clickdown():
    messagebox.showinfo("Message:","Button DOWN was clicked")

def clickright():
    messagebox.showinfo("Message:","Button RIGHT was clicked")

def clickleft():
    messagebox.showinfo("Message:","Button LEFT was clicked")



window.title("GUI")
#label = tk.Label(window,text = "Hello World").pack()
window.geometry('1920x1080')

helv36 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
l1 = tk.Label(window,text = "GUI TEST", font = ("Arial Bold",50)).place(x=750,y=150)
bt1 = tk.Button(window,text = "UP",height = 5,width = 10,font = helv36,bg = "green",command = clickup).place(x = 850,y=350)
bt2 = tk.Button(window,text = "DOWN",height = 5,width = 10,font = helv36,bg = 'red',command = clickdown).place(x = 850,y=700)
bt3 = tk.Button(window,text = "RIGHT",height = 5,width = 10,font = helv36,bg = 'yellow',command = clickright).place(x = 1200,y=525)
bt4 = tk.Button(window,text = "LEFT",height = 5,width = 10,font = helv36,bg = 'blue',command = clickleft).place(x =500 ,y=525)
window.mainloop()
