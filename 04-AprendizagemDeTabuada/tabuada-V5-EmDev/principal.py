from tkinter import *
from interfaceStart import FrameStart
from sys import builtin_module_names, exit

print('feito no gnu/linux, fedora 34')


class Tabuada(Tk):
    def __init__(self):
        super().__init__()
        self.title('FTabuada v4')
        self.geometry('500x400')
        
        self.opcaoMenu = Frame(self)
    
        self.bt_start = Button(self, text='start', command=self.Start, font='arial 20')
        self.bind('<Return>', self.teclaEnter)
        self.valor = IntVar()

        self.lb_op = Label(self.opcaoMenu, text='qual tabuada?:')
        self.lb_op.pack()


        # ======= radio Button ===========================================
        # radio button das opcao para escolher
        self.rbt1 = Radiobutton(self.opcaoMenu, text='1', variable=self.valor, value=1, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt2 = Radiobutton(self.opcaoMenu, text='2', variable=self.valor, value=2, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt3 = Radiobutton(self.opcaoMenu, text='3', variable=self.valor, value=3, indicatoron=0, padx=10, pady=10,bg='green')
        self.rbt4 = Radiobutton(self.opcaoMenu, text='4', variable=self.valor, value=4, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt5 = Radiobutton(self.opcaoMenu, text='5', variable=self.valor, value=5, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt6 = Radiobutton(self.opcaoMenu, text='6', variable=self.valor, value=6, indicatoron=0, padx=10, pady=10,bg='green')
        self.rbt7 = Radiobutton(self.opcaoMenu, text='7', variable=self.valor, value=7, indicatoron=0, padx=10, pady=10,bg='green')
        self.rbt8 = Radiobutton(self.opcaoMenu, text='8', variable=self.valor, value=8, indicatoron=0, padx=10, pady=10,bg='green')
        self.rbt9 = Radiobutton(self.opcaoMenu, text='9', variable=self.valor, value=9, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt10 = Radiobutton(self.opcaoMenu, text='10', variable=self.valor, value=10, indicatoron=0, padx=10, pady=10, bg='green')

        self.rbt1.pack (side=LEFT)
        self.rbt2.pack (side=LEFT)
        self.rbt3.pack (side=LEFT)
        self.rbt4.pack (side=LEFT)
        self.rbt5.pack (side=LEFT)
        self.rbt6.pack (side=LEFT)
        self.rbt7.pack (side=LEFT)
        self.rbt8.pack (side=LEFT)
        self.rbt9.pack (side=LEFT)
        self.rbt10.pack(side=LEFT)

        self.rbt9.select()
        # ========================================================
        
        # teclado dos numeros das tabuadas
        self.bind('1', self.tecla1)
        self.bind('2', self.tecla2)
        self.bind('3', self.tecla3)
        self.bind('4', self.tecla4)
        self.bind('5', self.tecla5)
        self.bind('6', self.tecla6)
        self.bind('7', self.tecla7)
        self.bind('8', self.tecla8)
        self.bind('9', self.tecla9)
        
        self.frameVoltarSair = Frame(self)
        self.bt_voltar = Button(self.frameVoltarSair, 
                                text='Voltar', width=15, font='arial 20 bold', 
                                command=self.esconderFrameStart)
        self.bt_sair = Button(self.frameVoltarSair, 
                              text='Sair', width=20, 
                              font='arial 20 bold',
                              command=exit
                              )

        self.bt_voltar.pack(side=RIGHT)
        self.bt_sair.pack(side=LEFT)

        self.frameVoltarSair.pack(side=TOP) 
    
        # mostrar menu - chamando a funcao
        self.mostrarMenu()

    # funcoes de aperto de teclas
    def tecla1(self, event):
        self.rbt1.select()
    def tecla2(self, event):
        self.rbt2.select()
    def tecla3(self, event):
        self.rbt3.select()
    def tecla4(self, event):
        self.rbt4.select()
    def tecla5(self, event):
        self.rbt5.select()
    def tecla6(self, event):
        self.rbt6.select()
    def tecla7(self, event):
        self.rbt7.select()
    def tecla8(self, event):
        self.rbt8.select()
    def tecla9(self, event):
        self.rbt9.select()
        
        
    def teclaEnter(self, event):
        self.Start()
        
    def esconder(self):
        self.opcaoMenu.pack_forget()
        self.bt_start.pack_forget()
        
    def esconderFrameStart(self):
        self.frameStart.pack_forget()
        self.mostrarMenu()

    def mostrarMenu(self): 
        self.opcaoMenu.pack()
        self.opcaoMenu.pack(anchor=CENTER, padx=10, pady=20)
        self.bt_start.pack(anchor=CENTER)
        self.bt_voltar.config(state=DISABLED)
    
    
    def Start(self):  
        self.esconder()
        self.bt_voltar.config(state=NORMAL)
        
        self.frameStart = FrameStart(self)
        self.frameStart.pack()
        self.frameStart.iniciar(self.valor.get())




if __name__ == '__main__':
    root = Tabuada()
    root.mainloop()