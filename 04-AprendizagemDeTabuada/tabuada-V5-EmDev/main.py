from tkinter import *
from frameStart import FrameStart
from frameMenu import FrameMenu

class Principal(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

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
        
    def show_frame(self, nomeFrame):

        frame = self.frames[nomeFrame]
        frame.tkraise()
        
        if nomeFrame == 'FrameStart':
            frame.iniciar(self.frames['FrameMenu'].valor.get())
            self.bt_voltar.config(state=NORMAL)

        else:
            self.bt_voltar.config(state=DISABLED)

  
        
            


    
root = Principal()
root.mainloop()