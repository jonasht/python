from tkinter.constants import BOTTOM, CENTER, LEFT, N, W
from interfaceCadastro import FrameCadastro
from interfaceDados import FrameDados
import tkinter as tk
from tkinter import ttk
import os

class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('600x300+450+300')
        self.title('Menu')
        
        # definindo botao de sair
        self.bt_sair = ttk.Button(self, text='Sair', width=15, command=os.sys.exit)
        self.bt_sair.pack(side=BOTTOM, anchor=W)
        
        # frame
        self.frame = ttk.Frame(self)
        
        self.lb_telaPricipal = ttk.Label(self.frame, text='tela principal', foreground='blue')
        self.bt_cadastrar    = ttk.Button(self.frame, text='cadastrar', width=15, command=self.cadastrar)
        self.bt_pesquisar    = ttk.Button(self.frame, text='pesquisar', width=15, command=self.Pesquisar)
        
        self.lb_telaPricipal.grid(row=0)
        self.bt_cadastrar.grid(row=1)
        self.bt_pesquisar.grid(row=2)
        
        # colocando frame
        self.frame.pack(side=LEFT, anchor=N)
        
        # false ou true para as frame sair e entrarem 
        self.xCadastro = [True, False]
        self.xDados = [True, False]

        # linha entre o frame menu e a frame..
        self.risco = ttk.Label(self,text='|\n'*16, foreground='darkgray', width=1).pack(side=LEFT, anchor=CENTER)



    def cadastrar(self):
        if self.xCadastro[0]:
            if self.xDados[1]:
                self.Pesquisar()
                
            self.frameCadastro = FrameCadastro(self)
            self.frameCadastro.pack(side=LEFT, anchor=N)
            self.xCadastro.reverse()

        else:
            self.frameCadastro.pack_forget()
            self.xCadastro.reverse()
        
    def Pesquisar(self):
        if self.xDados[0]:
            if self.xCadastro[1]:
                self.cadastrar()

            self.framedados = FrameDados(self)
            self.framedados.pack(side=LEFT, anchor=N)
            self.xDados.reverse()
        else:
            self.framedados.pack_forget()
            self.xDados.reverse()


if __name__ == '__main__':
    menu = Menu()
    menu.mainloop()