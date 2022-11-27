from tkinter import *
from tkinter import ttk
from webbrowser import BackgroundBrowser



root = Tk()
chbt_value = BooleanVar()
lb = ttk.Label(root, text='=-=-=')

def c_evento():
    print('checkbt:', chbt_value.get())
    if chbt_value.get():
        print('ch ativado')
        lb.config(foreground='green', text='ativado')
    else:
        print('ch desativado')
        lb.config(foreground='red', text='desativado')

        
root.geometry('500x500')

chbt = ttk.Checkbutton(root, text='teste', variable=chbt_value, command=c_evento)

chbt.pack(anchor=CENTER)
lb.pack(anchor=CENTER)
root.config(background='orange')


lb.config(font='gothic 40 bold', background='orange')
c_evento()
from sys import exit
root.bind('q', exit)

root.mainloop()