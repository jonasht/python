from tkinter import *

from tkinter.messagebox import showinfo

def replay():
    showinfo(title='popup', message = 'botão apertado')

janela = Tk()

botao = Button(janela, text='press', command=replay)
botao.pack()

janela.mainloop()