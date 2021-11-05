import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTTOM
from frame import Interface
from conta import Conta



class Principal(tk.Tk):
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
        
        # teclado numPad / teclado do lado do teclado
        self.bind('<KP_1>', self.teclaNum1)
        self.bind('<KP_2>', self.teclaNum2)
        self.bind('<KP_3>', self.teclaNum3)
        self.bind('<KP_4>', self.teclaNum4)
        self.bind('<KP_5>', self.teclaNum5)
        self.bind('<KP_6>', self.teclaNum6)
        self.bind('<KP_7>', self.teclaNum7)
        self.bind('<KP_8>', self.teclaNum8)
        self.bind('<KP_9>', self.teclaNum9)
        
        
        # tecla enter e tecla enter NumPad
        self.bind('<Return>', self.teclaEnter)
        self.bind('<KP_Enter>', self.teclaNumEnter)
        # ====================================

        # tecla q para sair
        self.bind('q', self.teclaQ)
        
        # tecla backspace/apagar
        self.bind('<BackSpace>', self.apagar)
        
        self.bind('<Up>', self.teclaUp)
        self.bind('<Down>', self.teclaDown)


        self.bind('<Control_L>'+'<BackSpace>', self.tecla_ctrl_backspace)
        self.bind('<Control_R>'+'<BackSpace>', self.tecla_ctrl_backspace)
        
        
        # self.posicaofileira[0] = True
        self.posicaofileira = [True, False]
        self.mostrarFileira()
        self.mostrar()


        label_tuto = ttk.Label(self, text='ctrl + backspace para apagar', foreground='gray')
        label_tuto.pack(side=BOTTOM)
        
    def botao1(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(1)
        else:
            self.conta.somarComecar(1)
        self.mostrar()
        
    def botao2(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(2)
        else:
            self.conta.somarComecar(2)
        self.mostrar()
        
    def botao3(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(3)
        else:
            self.conta.somarComecar(3)
        self.mostrar()
        
    def botao4(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(4)
        else:
            self.conta.somarComecar(4)
        self.mostrar()
        
    def botao5(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(5)
        else:
            self.conta.somarComecar(5)
        self.mostrar()
        
    def botao6(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(6)
        else:
            self.conta.somarComecar(6)
        self.mostrar()
        
    def botao7(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(7)
        else:
            self.conta.somarComecar(7)
        self.mostrar()
        
    def botao8(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(8)
        else:
            self.conta.somarComecar(8)
        self.mostrar()
        
    def botao9(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(9)
        else:
            self.conta.somarComecar(9)
        self.mostrar()
    
    # funcoes das teclado numerica NumPad/ teclas numericas do lado do teclado
    def teclaNum1(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(1)
        else:
            self.conta.somarComecar(1)
        self.mostrar()

    def teclaNum2(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(2)
        else:
            self.conta.somarComecar(2)
        self.mostrar()

    def teclaNum3(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(3)
        else:
            self.conta.somarComecar(3)
        self.mostrar()

    def teclaNum4(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(4)
        else:
            self.conta.somarComecar(4)
        self.mostrar()

    def teclaNum5(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(5)
        else:
            self.conta.somarComecar(5)
        self.mostrar()


    def teclaNum6(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(6)
        else:
            self.conta.somarComecar(6)
        self.mostrar()

    def teclaNum7(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(7)
        else:
            self.conta.somarComecar(7)
        self.mostrar()

    def teclaNum8(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(8)
        else:
            self.conta.somarComecar(8)
        self.mostrar()

    def teclaNum9(self, event):
        if self.posicaofileira[0]:
            self.conta.somarRecomecar(9)
        else:
            self.conta.somarComecar(9)
        self.mostrar()

        
    def teclaEnter(self, event):
        self.posicaofileira.reverse()
        print('enter apertado')
        self.mostrarFileira()
        
    def teclaNumEnter(self, event):
        self.posicaofileira.reverse()
        print('enter apertado')
        self.mostrarFileira()
    
    
    def teclaUp(self, event=None):
        print('up')
        self.posicaofileira.reverse()
        self.mostrarFileira()
        
    def teclaDown(self, event=None):
        print('down')
        self.posicaofileira.reverse()
        self.mostrarFileira()

    # tecla q para sair        
    def teclaQ(self, event):
        self.quit()
    
    # tecla ctrl + backspace para apagar tudo
    def tecla_ctrl_backspace(self, event):
        
        print('tecla ctrl apertada')
        self.conta.recomecar.clear()
        self.conta.comecar.clear()
        if not(self.posicaofileira[0]):
            self.teclaUp()
        
        self.mostrar()
        
    # backspace/apagar ultimo item de lista
    def apagar(self, event):
        if self.posicaofileira[0] and self.conta.recomecar:
            del(self.conta.recomecar[-1])
        if self.posicaofileira[1] and self.conta.comecar:
            del(self.conta.comecar[-1])
        
        self.mostrar()
        
        
    # mudar rows da frames ...
    def mostrarFileira(self):
        if self.posicaofileira[0]:
            self.frame.lb2.config(background='lightgray')
            self.frame.lb_numero2.config(background='lightgray')
            
            self.frame.lb1.config(background='gray')
            self.frame.lb_numero1.config(background='gray')

        if self.posicaofileira[1]:
            self.frame.lb1.config(background='lightgray')
            self.frame.lb_numero1.config(background='lightgray')    
                    
            self.frame.lb2.config(background='gray')
            self.frame.lb_numero2.config(background='gray')
            
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