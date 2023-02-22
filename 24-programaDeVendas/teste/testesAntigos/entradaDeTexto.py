from tkinter import *

root = Tk()
root.geometry('500x500')
def enviar_msn():
    print(entranda.get('1.0', END))
    
def resetar():
    entranda.delete('1.0', END)
entranda = Text(root, bg='yellow')

entranda.pack()
bt = Button(root, text='enviar' ,command=enviar_msn)
bt.pack()

bt_resetar = Button(root, text='resetar', command=resetar)
bt_resetar.pack()
root.mainloop()
