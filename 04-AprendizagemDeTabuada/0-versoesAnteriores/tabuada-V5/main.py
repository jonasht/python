from tkinter import *
from frameStart import FrameStart
from frameMenu import FrameMenu

class Principal(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.frameStart_on = False
        container = Frame(self)

        
        self.title('FTabuada v5')
        self.geometry('500x400')
        
    

        
        # botoes do topo da tela ====================================
        self.frameVoltarSair = Frame(self)
        
        self.bt_voltar = Button(self.frameVoltarSair, 
                                text='Voltar', width=15, font='arial 20 bold', 
                                command=lambda: self.show_frame('FrameMenu')
                                )
        self.bt_sair = Button(self.frameVoltarSair, 
                              text='Fechar X', width=20, 
                              font='arial 20 bold',
                              command=exit
                              )

        self.bt_voltar.pack(side=RIGHT)
        self.bt_sair.pack(side=LEFT)

        self.frameVoltarSair.pack(side=TOP) 
        
        container.pack()
        
        self.frames = {}
        for F in (FrameStart, FrameMenu):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")


        self.show_frame('FrameMenu')
        
        # teclas numericas 
        self.bind('1', self.tecla1)
        self.bind('2', self.tecla2)
        self.bind('3', self.tecla3)
        self.bind('4', self.tecla4)
        self.bind('5', self.tecla5)
        self.bind('6', self.tecla6)
        self.bind('7', self.tecla7)
        self.bind('8', self.tecla8)
        self.bind('9', self.tecla9)
        
        self.bind('<Return>', self.teclaEnter)
        # teclas do Num Pad
        self.bind('<KP_1>', self.tecla1)
        self.bind('<KP_2>', self.tecla2)
        self.bind('<KP_3>', self.tecla3)
        self.bind('<KP_4>', self.tecla4)
        self.bind('<KP_5>', self.tecla5)
        self.bind('<KP_6>', self.tecla6)
        self.bind('<KP_7>', self.tecla7)
        self.bind('<KP_8>', self.tecla8)
        self.bind('<KP_9>', self.tecla9)
     
        
        
        self.bind('<KP_Enter>', self.teclaEnter)
        self.bind('<BackSpace>', self.teclaBackSpace)
        self.bind('q', self.tecla_q)
        self.bind('<Escape>', self.teclaESCape)
    def teclaEnter(self, event):
        if not(self.frameStart_on):
            self.show_frame('FrameStart')

    def teclaBackSpace(self, event):
        if self.frameStart_on:
            self.show_frame('FrameMenu')
            
    def tecla_q(self, event):
        exit()
    def teclaESCape(self, event):
        if self.frameStart_on:
            self.show_frame('FrameMenu')
        else:
            exit()
    def tecla1(self, event):
        if self.frameStart_on:
            self.frames['FrameStart'].tecla1(None)
        else:
            self.frames['FrameMenu'].rbt1.select()
    def tecla2(self, event):
        if self.frameStart_on:
            self.frames['FrameStart'].tecla2(None)
        else:
            self.frames['FrameMenu'].rbt2.select()
    def tecla3(self, event):
        if self.frameStart_on:
            self.frames['FrameStart'].tecla3(None)
        else:
            self.frames['FrameMenu'].rbt3.select()            

    def tecla4(self, event):
        self.frames['FrameMenu'].rbt4.select()            
    def tecla5(self, event):
        self.frames['FrameMenu'].rbt5.select()            
    def tecla6(self, event):
        self.frames['FrameMenu'].rbt6.select()            
    def tecla7(self, event):
        self.frames['FrameMenu'].rbt7.select()            
    def tecla8(self, event):
        self.frames['FrameMenu'].rbt8.select()            
    def tecla9(self, event):
        self.frames['FrameMenu'].rbt9.select()            
        
        
        
    def show_frame(self, nomeFrame):

        frame = self.frames[nomeFrame]
        frame.tkraise()
        
        if nomeFrame == 'FrameStart':
            self.frameStart_on = True
            frame.iniciar(self.frames['FrameMenu'].valor.get())
            self.bt_voltar.config(state=NORMAL)

        else:
            self.frameStart_on = False
            self.bt_voltar.config(state=DISABLED)

  
        
            


    
root = Principal()
root.mainloop()