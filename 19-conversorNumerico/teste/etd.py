from tkinter import Tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def evento(event):
    print(et.get())

app = Tk()
app.geometry('500x500+700+200')

lb = ttk.Label(app, text='so um teste')
lb.pack()

et = ttk.Entry(app)
et.config(width=30)
et.pack()

et.bind('<KeyRelease>', evento)

app.mainloop()