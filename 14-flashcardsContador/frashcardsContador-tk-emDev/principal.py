from tkinter import *
from frame import Interface
from conta import Conta



class Principal(Tk):
    def __init__(self):
        super().__init__()
        self.conta = Conta()
        self.frame = Interface(self)
        self.frame.pack()

        # teclas de numeros (de cima do teclado)
        self.bind('1', self.botao1)
        self.bind('2', self.botao2)
        self.bind('3', self.botao3)
        self.bind('4', self.botao4)
        self.bind('5', self.botao5)
        self.bind('6', self.botao6)
        self.bind('7', self.botao7)
        self.bind('8', self.botao8)
        self.bind('9', self.botao9)
        
        # tecla enter
        self.bind('<Return>', self.teclaEnter)
        
        # tecla backspace/apagar
        self.bind('<BackSpace>', self.apagar)
        self.recomecar = True
        
        self.mudarDeCor()
        self.mostrar()

    def botao1(self, event):
        if self.recomecar:
            self.conta.somarRecomecar(1)
        else:
            self.conta.somarComecar(1)
            
        self.mostrar()
        print('funcionando 1')
        
    def botao2(self, event):
        if self.recomecar:
            self.conta.somarRecomecar(2)
        else:
            self.conta.somarComecar(2)
        self.mostrar()
        
    def botao3(self, event):
        if self.recomecar:
            self.conta.somarRecomecar(3)
        else:
            self.conta.somarComecar(3)
        self.mostrar()
        
    def botao4(self, event):
        if self.recomecar:
            self.conta.somarRecomecar(4)
        else:
            self.conta.somarComecar(4)
        self.mostrar()
        
    def botao5(self, event):
        if self.recomecar:
            self.conta.somarRecomecar(5)
        else:
            self.conta.somarComecar(5)
        self.mostrar()
        
    def botao6(self, event):
        if self.recomecar:
            self.conta.somarRecomecar(6)
        else:
            self.conta.somarComecar(6)
        self.mostrar()
    def botao7(self, event):
        if self.recomecar:
            self.conta.somarRecomecar(7)
        else:
            self.conta.somarComecar(7)
        self.mostrar()
        
    def botao8(self, event):
        if self.recomecar:
            self.conta.somarRecomecar(8)
        else:
            self.conta.somarComecar(8)
        self.mostrar()
        
    def botao9(self, event):
        if self.recomecar:
            self.conta.somarRecomecar(9)
        else:
            self.conta.somarComecar(9)
        self.mostrar()
    def teclaEnter(self, event):
        self.recomecar = False
        print('enter apertado')
        self.mudarDeCor(2)
        
    # backspace/apagar ultimo item de lista
    def apagar(self, event):
        if self.recomecar and self.conta.recomecar:
            del(self.conta.recomecar[-1])
        elif self.conta.comecar:
            del(self.conta.comecar[-1])
        
        self.mostrar()
        print('funcionando')
    # mudar de cor as rows da frames ...
    def mudarDeCor(self, op=1):
        if op==1:
            self.frame.lb2.config(bg='lightgray')
            self.frame.lb_numero2.config(bg='lightgray')
            self.frame.lb1.config(bg='gray')
            self.frame.lb_numero1.config(bg='gray')
        if op==2:
            self.frame.lb1.config(bg='lightgray')
            self.frame.lb_numero1.config(bg='lightgray')    
                    
            self.frame.lb2.config(bg='gray')
            self.frame.lb_numero2.config(bg='gray')
            
    def mostrar(self):
        self.frame.atualizarTotal(self.conta.get_total())
        self.frame.atualizarRecomecar(self.conta.get_totalRecomecar())
        self.frame.atualizarComecar(self.conta.get_totalComecar())
        self.frame.atualizarRestanteDeCartas(self.conta.get_restanteDeCartas())

        self.frame.lb_lista1.config(text=self.conta.get_recomecar())
        self.frame.lb_lista2.config(text=self.conta.get_comecar())

        
if __name__ == '__main__':
    root = Principal()
    root.geometry('300x300')
    root.mainloop()