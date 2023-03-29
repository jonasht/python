# from tkinter import ttk, Tk
# from tkinter.constants import BOTTOM
from frame import Interface
from conta import Conta

import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Window(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title('Contador de Flashcard')
        self.conta = Conta()
        self.frame = Interface(self)
        self.frame.pack()

        # teclas de numeros (de cima do teclado)
        self.bind('1', self.key_1)
        self.bind('2', self.key_2)
        self.bind('3', self.key_3)
        self.bind('4', self.key_4)
        self.bind('5', self.key_5)
        self.bind('6', self.key_6)
        self.bind('7', self.key_7)
        self.bind('8', self.key_8)
        self.bind('9', self.key_9)

        # teclado numPad / teclado do lado do teclado
        self.bind('<KP_1>', self.key_Num1)
        self.bind('<KP_2>', self.key_Num2)
        self.bind('<KP_3>', self.key_Num3)
        self.bind('<KP_4>', self.key_Num4)
        self.bind('<KP_5>', self.key_Num5)
        self.bind('<KP_6>', self.key_Num6)
        self.bind('<KP_7>', self.key_Num7)
        self.bind('<KP_8>', self.key_Num8)
        self.bind('<KP_9>', self.key_Num9)

        # tecla enter e tecla enter
        self.bind('<Return>', self.key_enter)
        # tecla enter e tecla enter NumPad
        self.bind('<KP_Enter>', self.key_NumEnter)
        # ====================================

        # tecla q para sair
        self.bind('q', self.teclaQ)

        # tecla backspace/apagar
        self.bind('<BackSpace>', self.apagar)

        self.bind('<Up>', self.teclaUp)
        self.bind('<Down>', self.teclaDown)

        self.bind('<Control_L>'+'<BackSpace>', self.tecla_ctrl_backspace)
        self.bind('<Control_R>'+'<BackSpace>', self.tecla_ctrl_backspace)

        # self.rowPosition[0] = True
        self.rowPosition = [True, False]
        self.showRow()
        self.show()

        label_tuto = ttk.Label(
            self, text='ctrl + backspace p/ apagar tudo\nq para sair', foreground='gray')
        label_tuto.pack(side=BOTTOM)

    def key_1(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(1)
        else:
            self.conta.somarComecar(1)
        self.show()

    def key_2(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(2)
        else:
            self.conta.somarComecar(2)
        self.show()

    def key_3(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(3)
        else:
            self.conta.somarComecar(3)
        self.show()

    def key_4(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(4)
        else:
            self.conta.somarComecar(4)
        self.show()

    def key_5(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(5)
        else:
            self.conta.somarComecar(5)
        self.show()

    def key_6(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(6)
        else:
            self.conta.somarComecar(6)
        self.show()

    def key_7(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(7)
        else:
            self.conta.somarComecar(7)
        self.show()

    def key_8(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(8)
        else:
            self.conta.somarComecar(8)
        self.show()

    def key_9(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(9)
        else:
            self.conta.somarComecar(9)
        self.show()

    # funcoes das teclado numerica NumPad/ teclas numericas do lado do teclado
    def key_Num1(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(1)
        else:
            self.conta.somarComecar(1)
        self.show()

    def key_Num2(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(2)
        else:
            self.conta.somarComecar(2)
        self.show()

    def key_Num3(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(3)
        else:
            self.conta.somarComecar(3)
        self.show()

    def key_Num4(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(4)
        else:
            self.conta.somarComecar(4)
        self.show()

    def key_Num5(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(5)
        else:
            self.conta.somarComecar(5)
        self.show()

    def key_Num6(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(6)
        else:
            self.conta.somarComecar(6)
        self.show()

    def key_Num7(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(7)
        else:
            self.conta.somarComecar(7)
        self.show()

    def key_Num8(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(8)
        else:
            self.conta.somarComecar(8)
        self.show()

    def key_Num9(self, event):
        if self.rowPosition[0]:
            self.conta.somarRecomecar(9)
        else:
            self.conta.somarComecar(9)
        self.show()

    def key_enter(self, event):
        self.rowPosition.reverse()
        self.showRow()

    def key_NumEnter(self, event):
        self.rowPosition.reverse()
        self.showRow()

    def teclaUp(self, event=None):

        self.rowPosition.reverse()
        self.showRow()

    def teclaDown(self, event=None):

        self.rowPosition.reverse()
        self.showRow()

    # tecla q para sair
    def teclaQ(self, event):
        self.quit()

    # tecla ctrl + backspace para apagar tudo
    def tecla_ctrl_backspace(self, event):

        self.conta.recomecar.clear()
        self.conta.comecar.clear()
        if not (self.rowPosition[0]):
            self.teclaUp()

        self.show()

    # backspace/apagar ultimo item de lista
    def apagar(self, event):
        if self.rowPosition[0] and self.conta.recomecar:
            del (self.conta.recomecar[-1])
        if self.rowPosition[1] and self.conta.comecar:
            del (self.conta.comecar[-1])

        self.show()

    # show rows frames

    def showRow(self):
        if self.rowPosition[0]:
            self.frame.lb2.config(background='lightgray')
            self.frame.lb_numero2.config(background='lightgray')

            self.frame.lb1.config(background='gray')
            self.frame.lb_numero1.config(background='gray')

        if self.rowPosition[1]:
            self.frame.lb1.config(background='lightgray')
            self.frame.lb_numero1.config(background='lightgray')

            self.frame.lb2.config(background='gray')
            self.frame.lb_numero2.config(background='gray')

    def show(self):
        self.frame.atualizarTotal(self.conta.get_total())
        self.frame.atualizarRecomecar(self.conta.get_totalRecomecar())
        self.frame.atualizarComecar(self.conta.get_totalComecar())

        self.frame.atualizarRestanteDeCartas(self.conta.get_restanteDeCartas())

        recomecar = self.conta.get_recomecar().copy()
        comecar = self.conta.get_comecar().copy()
        # print(f'recomecar tipo: {type(recomecar)}')
        # comecar = self.conta.get_comecar()
        # self.frame.lb_lista1.config(text=self.conta.get_recomecar())
        if len(recomecar) > 14:
            recomecar.insert(15, '\n')
            recomecar = ' '.join(list(map(str, recomecar)))

            self.frame.lb_lista1.config(text=recomecar)
        else:
            self.frame.lb_lista1.config(text=self.conta.get_recomecar())

        if len(comecar) > 14:
            comecar.insert(15, '\n')
            comecar = ' '.join(list(map(str, comecar)))

            self.frame.lb_lista2.config(text=comecar)
        else:
            self.frame.lb_lista2.config(text=self.conta.get_comecar())


def main():
    window = Window()
    window.geometry('600x350')
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    main()
