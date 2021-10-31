from tkinter import *
import uteis as u
from colorama.ansi import Fore

class FrLogin(Frame):
    def __init__(self, parent, controller):
        
        Frame.__init__(self, parent)
        self.controller = controller

        self.lbfr_meio = LabelFrame(self, text='Login')
        
        self.lb_login = Label(self.lbfr_meio, text='login:')
        self.lb_senha = Label(self.lbfr_meio, text='Senha:')

        self.etd_login = Entry(self.lbfr_meio)
        self.etd_senha = Entry(self.lbfr_meio, show='*')

        self.lb_login.grid(row=0, column=0)
        self.etd_login.grid(row=0, column=1)
        self.lb_senha.grid(row=1, column=0)
        self.etd_senha.grid(row=1, column=1)

        self.bt_limpar = Button(self.lbfr_meio, text='Limpar')
        self.bt_entrar = Button(self.lbfr_meio, text='Entrar', command=self.acessar)
        self.bt_limpar.grid(row=2, column=0)
        self.bt_entrar.grid(row=2, column=1)

        
        self.lbfr_meio.pack()
        self.bt_cadastrar = Button(self, text='fazer cadastro', command=lambda:self.controller.show_frame('FrCadastro')).pack()

        self.lb_aviso = Label(self, text='aviso', fg='red')
        self.lb_aviso.pack()
 
    def acessar(self):
        login = self.etd_login.get()
        senha = self.etd_senha.get()

        print(login, senha)
        
        senhaDoSistema = u.get_senha(login)
        
        if senhaDoSistema and senhaDoSistema == senha:
            print(Fore.GREEN+'acesso permitido', Fore.RESET)
            self.controller.show_frame('FrAcesso')
            
        else:
            print(Fore.RED+'acesso negado', Fore.RESET)

    



        
        
        
if __name__ == '__main__':
    
    root = Tk()
    frame = FrLogin(root)
    root.geometry('500x500')

    frame.pack()
    root.mainloop()

