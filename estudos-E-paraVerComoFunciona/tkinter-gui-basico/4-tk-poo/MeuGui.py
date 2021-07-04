from tkinter import *
from tkinter.messagebox import showinfo


class MeuGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        botao = Button(self, text='Aperte aqui', width=50, height=25, command=self.reply)
        botao.pack()

    def reply(self):
        showinfo(title='popup', message='botao apertado')

if __name__ == '__main__':
    janela = MeuGui()
    janela.pack()
    janela.mainloop()


