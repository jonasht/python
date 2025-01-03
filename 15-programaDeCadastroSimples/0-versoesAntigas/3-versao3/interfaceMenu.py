from interfaceCadastro import FrameCadastro
from interfaceDados import FrameDados
from tkinter import *
import os

class Menu(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('600x300+450+300')
        self.title('Menu')

        # definindo botao de sair
        self.bt_sair = Button(self, text='Sair', width=15, command=os.sys.exit)
        self.bt_sair.pack(side=BOTTOM, anchor=W)
        
        # frame
        self.frame = Frame(self)
        
        self.lb_telaPricipal = Label(self.frame, text='tela principal', fg='blue')
        self.bt_cadastrar    = Button(self.frame, text='cadastrar', width=15, command=self.cadastrar)
        self.bt_pesquisar    = Button(self.frame, text='pesquisar', width=15, command=self.Pesquisar)
        
        self.lb_telaPricipal.grid(row=0)
        self.bt_cadastrar.grid(row=1)
        self.bt_pesquisar.grid(row=2)
        
        # colocando frame
        self.frame.pack(side=LEFT, anchor=N)
        
        # false ou true para as frame sair e entrarem 
        self.xCadastro = [True, False]
        self.xDados = [True, False]

        # linha entre o frame menu e a frame..
        self.risco = Label(self,text='|\n'*16, fg='darkgray', width=1, height=15).pack(side=LEFT, anchor=CENTER)

    def ehNumero(self, n):
        try:
            int(n)
            return True
        except:
            return False
        


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