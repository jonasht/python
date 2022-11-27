from cgitb import text
from tkinter import *
from tkinter import ttk


root = Tk()

sep = ttk.Separator(root, orient=VERTICAL)

txt1 = Text(root)
txt2 = Text(root)
sep.grid(row=0, column=1, padx=5, pady=5, sticky=NS)
txt1.grid(row=0, column=0, padx=5, pady=5)
txt2.grid(row=0, column=2, padx=5, pady=5)

from sys import exit
root.bind('q', exit)

root.mainloop()