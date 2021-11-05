import tkinter as tk
from tkinter import ttk
from frAcesso import FrAcesso
import uteis as u
from colorama.ansi import Fore

class FrLogin(ttk.Frame):
    def __init__(self, parent, controller):
        
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.lbfr_meio = ttk.LabelFrame(self, text='Login')
        
        self.lb_login = ttk.Label(self.lbfr_meio, text='login:')
        self.lb_senha = ttk.Label(self.lbfr_meio, text='Senha:')

        self.etd_login = ttk.Entry(self.lbfr_meio)
        self.etd_senha = ttk.Entry(self.lbfr_meio, show='*')

        self.lb_login.grid(row=0, column=0)
        self.etd_login.grid(row=0, column=1)
        self.lb_senha.grid(row=1, column=0)
        self.etd_senha.grid(row=1, column=1)

        self.bt_limpar = ttk.Button(self.lbfr_meio, text='Limpar')
        self.bt_entrar = ttk.Button(self.lbfr_meio, text='Entrar', command=self.acessar)
        self.bt_limpar.grid(row=2, column=0)
        self.bt_entrar.grid(row=2, column=1)

        
        self.lbfr_meio.pack()
        self.bt_cadastrar = ttk.Button(self, text='fazer cadastro', command=lambda:self.controller.show_frame('FrCadastro')).pack()

        self.lb_aviso = ttk.Label(self, text='')
        self.lb_aviso.pack()
 
    def acessar(self):
        login = self.etd_login.get()
        senha = self.etd_senha.get()

        if login == '':
            self.lb_aviso.config(text='por favor insira o login')
        elif senha == '':
            self.lb_aviso.config(text='por favor insira o senha')
            
        print(login, senha)
        
        senhaDoSistema = u.get_senha(login)
        print('senhaDoSistema:', senhaDoSistema)


        if senhaDoSistema and senhaDoSistema == senha:
            print(Fore.GREEN+'acesso permitido', Fore.RESET)
            self.controller.show_frame('FrAcesso')
            # FrAcesso.set_login(login=login)
            FrAcesso.set_login(self.controller, login)
        else:
            print(Fore.RED+'acesso negado', Fore.RESET)
            self.lb_aviso.config(text='senha ou login invalido')

    



        
        
        
if __name__ == '__main__':
    
    root = tk.Tk()
    frame = FrLogin(root, None)
    root.geometry('500x500')

    frame.pack()
    root.mainloop()

