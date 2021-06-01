from tkinter import *

class InterfaceFrame (Frame):
    def __init__ (self, container):
        super().__init__(container)

        self.lb = Label(self, text='esta na frame',
                        width=25, height=10)
        self.lb.pack()

        self.bt = Button(self, text='sair', command=self.voltar)
        self.bt.pack()
        
        self.config(bg='red')
        self.lb.config(bg='red')
        
        self.variavelSair = 0

    def voltar(self):
        print('sair')
        
        
        