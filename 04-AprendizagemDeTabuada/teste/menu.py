from tkinter import *
from interfaceFrame import InterfaceFrame

class Menu(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x400')
        self.frameMenu = Frame(self)
        self.lb = Label(self.frameMenu, text='menu')
        self.lb.pack()
        
        self.bt = Button(self.frameMenu, text='entrar na interfaceFrame',
                         font='arial 20 bold',
                         command=self.mostrar_InterfaceFrame)
        self.bt.pack()
        
        self.frameMenu.pack()
        
    def mostrar_InterfaceFrame(self):
        self.interfaceFrame = InterfaceFrame(self)
        
        self.interfaceFrame.pack()
        self.frameMenu.pack_forget()

        
        print(self.interfaceFrame.variavelSair)
        
    def esconder_InterfaceFrame(self):
        self.interfaceFrame.pack_forget()

    def mostrar_frameMenu(self):
        self.frameMenu.pack()
        self.interfaceFrame.pack_forget()
        
    def esconder_frameMenu(self):
        self.frameMenu.pack_forget()
        

if __name__ == '__main__':
    menu = Menu()
    menu.mainloop()