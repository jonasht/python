from tkinter import *
from tkinter import ttk

from pyparsing import col 
  
  
x = Tk() 
x.geometry("400x300") 
  
  
b = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="separador") 
  
  
separator = ttk.Separator(x, orient='vertical') 
a = Label(x, background="#f5f5f5", border=4, relief=RAISED, text="separador") 

b.place(relx=0.03, rely=0.1, relheight=0.8, relwidth=0.4) 
separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1) 
a.place(relx=0.5, rely=0.1, relheight=0.8, relwidth=0.4) 


mainloop()