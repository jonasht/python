from tkinter import Tk
import ttkbootstrap as ttk 
from ttkbootstrap.constants import * 
from utils import get_configGeometry
from frameStart import FrameStart
from frameMenu import FrameMenu



class Principal(Tk):
    def __init__(self):
        super().__init__()
        self.frameStart_on = False
        container = ttk.Frame(self)

        
        self.title('FTabuada v5')
        
        
        self.lb_aviso = ttk.Label(self, text='q p/ sair', bootstyle=WARNING)
        self.bt_voltar = ttk.Button(self, text='Voltar', bootstyle=OUTLINE,  command=lambda: self.show_frame('FrameMenu'))



        container.pack(expand=True)

        self.bt_voltar.pack(side=BOTTOM, fill=X)
        self.lb_aviso.pack(side=BOTTOM, anchor=SE)


     
        
        
        self.frames = {}
        
        for F in (FrameStart, FrameMenu):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky=NSEW)
            

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
            self.frames['FrameMenu'].var_1.set(not(self.frames['FrameMenu'].var_1.get()))
            
            
    def tecla2(self, event):
        if self.frameStart_on:
            self.frames['FrameStart'].tecla2(None)
        else:
            self.frames['FrameMenu'].var_2.set(not(self.frames['FrameMenu'].var_2.get()))
            
    def tecla3(self, event):
        if self.frameStart_on:
            self.frames['FrameStart'].tecla3(None)
        else:
            self.frames['FrameMenu'].var_3.set(not(self.frames['FrameMenu'].var_3.get()))            

    def tecla4(self, event):
        self.frames['FrameMenu'].var_4.set(not(self.frames['FrameMenu'].var_4.get()))
                    
    def tecla5(self, event):
        self.frames['FrameMenu'].var_5.set(not(self.frames['FrameMenu'].var_5.get())) 
                   
    def tecla6(self, event):
        self.frames['FrameMenu'].var_6.set(not(self.frames['FrameMenu'].var_6.get())) 
                   
    def tecla7(self, event):
        self.frames['FrameMenu'].var_7.set(not(self.frames['FrameMenu'].var_7.get())) 
                   
    def tecla8(self, event):
        self.frames['FrameMenu'].var_8.set(not(self.frames['FrameMenu'].var_8.get()))  
                  
    def tecla9(self, event):
        self.frames['FrameMenu'].var_9.set(not(self.frames['FrameMenu'].var_9.get()))            
        
        
        
    def show_frame(self, nomeFrame):
        numbers = self.frames['FrameMenu'].get_numbers()
        
        print('numbers:', numbers)
        
        if nomeFrame == 'FrameStart' and numbers:
            
            frame = self.frames[nomeFrame]
            frame.tkraise()
            

            self.frameStart_on = True
            
            frame.iniciar(self.frames['FrameMenu'].get_numbers())
            
            self.bt_voltar.config(state=NORMAL)

        else:
            frame = self.frames[nomeFrame]
            frame.tkraise()
            
            
            self.frameStart_on = False
            self.bt_voltar.config(state=DISABLED)

  
        
            


def main():    
    root = Principal()
    root.geometry(get_configGeometry(root, 1000, 800))
    root.mainloop()

if __name__ == '__main__':
    main()