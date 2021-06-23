from interfaceCadastro import Cadastro
from interfaceDados import Dados
from tkinter import *

class Menu(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('200x200+450+300')
        self.title('Menu')
        
        self.lb_telaPricipal = Label(self, text='tela principal', fg='blue')
        self.bt_cadastrar    = Button(self, text='cadastrar', width=15, command=self.cadastrar)
        self.bt_pesquisar    = Button(self, text='pesquisar', width=15, command=self.Pesquisar)
        
        self.lb_telaPricipal.pack(pady=2)
        self.bt_cadastrar.pack(pady=2)
        self.bt_pesquisar.pack(pady=2)
        
    def ehNumero(self, n):
        try:
            int(n)
            return True
        except:
            return False

    def cadastrar(self):
        print("entrando em cadastro")
        cadastro = Cadastro()
        cadastro.mainloop()
        
    def Pesquisar(self):
        dados = Dados()
        dados.mainloop()



if __name__ == '__main__':
    menu = Menu()
    menu.mainloop()