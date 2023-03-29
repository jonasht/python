import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar
from tkinter import Tk


root = ttk.Window()
# root = Tk()



for i, style in enumerate(root.style.colors):
    bt1 = ttk.Button(root, text=style, bootstyle=style)
    bt1.grid(row=0, column=i, padx=5, pady=20)
    
    bt2 = ttk.Button(root, text=style, bootstyle=(style, OUTLINE))
    bt2.grid(row=1, column=i, padx=2, pady=20)
    
root.bind('q', lambda x: exit())

themes = root.style.theme_names()

stringvar = StringVar()

root.style.theme_use('darkly')

def change_theme():
    theme = stringvar.get()
    root.style.theme_use(theme)

rb = []
frame = ttk.Frame(root)

for i, theme in enumerate(themes):
    rb.append(ttk.Radiobutton(frame, text=theme, variable=stringvar, value=theme, command=change_theme))
    rb[i].grid(row=0, column=i, padx=6)
    

frame.grid(row=2, columnspan=8)
root.mainloop()