from tkinter import *
from interfaceStart import FrameStart
from frameMenu import Menu

class Principal(Tk):
    def __init__(self):
        super().__init__()
        
        self.title('FTabuada v5')
        self.geometry('500x400')
        
       
        # chamando classes
        
        self.menu = Menu(self)
        self.frameStart = FrameStart(self)
                
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
        
        # tecla enter
        self.bind('<Return>', self.teclaEnter)
        # botoes do topo da tela ================================
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
        
        self.mostrarMenu()
        print(self.menu.frameStartOn)

    def tecla1(self, event):
        self.menu.rbt1.select()
    def tecla2(self, event):
        self.menu.rbt2.select()
    def tecla3(self, event):
        self.menu.rbt3.select()
    def tecla4(self, event):
        self.menu.rbt4.select()
    def tecla5(self, event):
        self.menu.rbt5.select()
    def tecla6(self, event):
        self.menu.rbt6.select()
    def tecla7(self, event):
        self.menu.rbt7.select()
    def tecla8(self, event):
        self.menu.rbt8.select()
    def tecla9(self, event):
        self.menu.rbt9.select()
    
    def teclaEnter(self, event):
        self.Start()
        
    def esconderMenu(self):
        self.menu.pack_forget()
        
    def esconderFrameStart(self):
        self.frameStart.pack_forget()
        self.mostrarMenu()

    def mostrarMenu(self): 
        self.menu.pack()
        self.bt_voltar.config(state=DISABLED)   
    
    
    def Start(self):  
        self.esconderMenu()
        self.bt_voltar.config(state=NORMAL)
        self.frameStart.pack()
        self.frameStart.iniciar(self.menu.valor.get())
        


    
root = Principal()
root.mainloop()