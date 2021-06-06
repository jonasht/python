from tkinter import *
from frame import Interface
from conta import Conta



class Principal(Tk):
    def __init__(self):
        super().__init__()
        self.conta = Conta()
        self.frame = Interface(self)
        self.frame.pack()

        self.bind('1', self.botao1)
        self.bind('2', self.botao2)
        self.bind('3', self.botao3)
        self.bind('4', self.botao4)
        self.bind('5', self.botao5)
        self.bind('6', self.botao6)
        self.bind('7', self.botao7)
        self.bind('8', self.botao8)
        self.bind('9', self.botao9)

    def botao1(self, event):
        self.conta.somar(1)
        self.mostrar()
        print('funcionando 1')
        
    def botao2(self, event):
        self.conta.somar(2)
        self.mostrar()
        
    def botao3(self, event):
        self.conta.somar(3)
        self.mostrar()
        
    def botao4(self, event):
        self.conta.somar(4)
        self.mostrar()
        
    def botao5(self, event):
        self.conta.somar(5)
        self.mostrar()
        
    def botao6(self, event):
        self.conta.somar(6)
        self.mostrar()
    def botao7(self, event):
        self.conta.somar(7)
        self.mostrar()
    def botao8(self, event):
        self.conta.somar(8)
        self.mostrar()
        
    def botao9(self, event):
        self.conta.somar(9)
        self.mostrar()
        
    def mostrar(self):
        self.frame.atualizarTotal(self.conta.get_total())
        
if __name__ == '__main__':
    root = Principal()
    root.geometry('300x300')
    root.mainloop()