from tkinter import *


root = Tk()
def espaco(evento):
    # lb.config(text='espaco apertado')
    print('funcionando')
    
lb = Label(root, text='aperte', fg='green', bg='black').pack()
root.bind('<BackSpace>', espaco)

root.geometry('400x400')
root.mainloop()