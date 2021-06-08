from tkinter import *


root = Tk()
def espaco(evento):
    # lb.config(text='espaco apertado')
    print('funcionando')
def teclaUp(event):
    print('funcionando up')    
def teclaDown(event):
    print('funcionando Down')
 
def teclalado1(event):
    print('funcionando num 1')

def teclalado2(event):
    print('funcionando num 2')


lb = Label(root, text='aperte', fg='green', bg='black').pack()
root.bind('<Up>', teclaUp)
root.bind('<Down>', teclaDown)

root.bind('<BackSpace>', espaco)

root.bind('<KP_1>', teclalado1)
root.bind('<KP_2>', teclalado2)


root.geometry('400x400')
root.mainloop()