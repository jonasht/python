import tkinter as tk
from tkinter import ttk
from tkinter.constants import END, RIGHT

import uteis as u




class FrCadastro(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        # botao voltar
        self.bt_voltar = ttk.Button(self, text='Voltar', command=self.voltar)
        self.bt_voltar.pack(side=RIGHT, anchor='nw')


        self.lbfr_principal = ttk.LabelFrame(self, text='Cadastrar nova conta')
        
        self.lb_nome = ttk.Label(self.lbfr_principal, text='Nome:')
        self.etd_nome = ttk.Entry(self.lbfr_principal)

        self.lb_sobrenome = ttk.Label(self.lbfr_principal, text='sobrenome:')
        self.etd_sobrenome = ttk.Entry(self.lbfr_principal)

        self.lb_login = ttk.Label(self.lbfr_principal, text='Login:')
        self.etd_login = ttk.Entry(self.lbfr_principal)

        self.lb_senha = ttk.Label(self.lbfr_principal, text='Senha:')
        self.etd_senha = ttk.Entry(self.lbfr_principal, show='*')
        self.ckbt_senha = ttk.Checkbutton(self.lbfr_principal, command=self.mostrar_senha, text='')

        self.lb_reSenha = ttk.Label(self.lbfr_principal, text='repetir Senha:')
        self.etd_reSenha = ttk.Entry(self.lbfr_principal, show='*') 

        self.lb_email = ttk.Label(self.lbfr_principal, text='Email:')
        self.etd_email = ttk.Entry(self.lbfr_principal)

        self.lb_nome.grid(row=0, column=0)
        self.etd_nome.grid(row=0, column=1)
        self.lb_sobrenome.grid(row=1, column=0)
        self.etd_sobrenome.grid(row=1, column=1)


        self.lb_login.grid(row=2, column=0)
        self.etd_login.grid(row=2, column=1)
        
        self.lb_senha.grid(row=3, column=0)
        self.etd_senha.grid(row=3, column=1)
        self.ckbt_senha.grid(row=3, column=2)

        self.lb_reSenha.grid(row=4, column=0)
        self.etd_reSenha.grid(row=4, column=1)

        self.lb_email.grid(row=5, column=0)
        self.etd_email.grid(row=5, column=1)

        self.bt_limpar = ttk.Button(self.lbfr_principal, text='Limpar', command=self.limpar)
        self.bt_cadastrar = ttk.Button(self.lbfr_principal, text='Cadastrar', command=self.cadastrar)

        self.bt_limpar.grid(row=6, column=0)
        self.bt_cadastrar.grid(row=6, column=1)

        self.lbfr_principal.pack()


        # label aviso =-=-=-=-=-=-=-=-=-=-=-=-=
        self.lb_aviso = ttk.Label(self, text='')
        self.lb_aviso.pack()

    def mostrar_senha(self):

        self.etd_senha.config(show='')
        self.etd_reSenha.config(show='')
        self.ckbt_senha.config(command=self.esconder_senha)
    

        
    def esconder_senha(self, op=0):

        self.etd_senha.config(show='*')
        self.etd_reSenha.config(show='*')
        self.ckbt_senha.config(command=self.mostrar_senha)
    
    def cadastrar(self):
        nome = self.etd_nome.get()
        sobrenome = self.etd_sobrenome.get()
        login = self.etd_login.get()
        senha = self.etd_senha.get()
        resenha = self.etd_reSenha.get()
        email = self.etd_email.get()

        mensagem = ''

        if login:
            if not(u.login_in_data(login)):
                if senha and resenha:
                    if senha == resenha:
                        u.add_data(nome=nome, sobrenome=sobrenome, login=login, senha=senha, email=email)
                        self.lb_aviso.config(text='Cadastro Feito com sucesso', foreground='green')
                        print(nome, sobrenome, login, senha, resenha, email)
                    else:
                        self.lb_aviso.config(text='senhas precisam ser iguais', foreground='red')
                        
                else:
                    self.lb_aviso.config(text='as duas senhas sao obrigatorias', foreground='red')
            else:
                self.lb_aviso.config(text='login ja existente', foreground='red')       
        else:
            self.lb_aviso.config(text='campo login eh obrigatorio', foreground='red')

        
    def limpar(self):
        self.etd_nome.delete(0, END)
        self.etd_sobrenome.delete(0, END)
        self.etd_login.delete(0, END)
        self.etd_senha.delete(0, END)
        self.etd_reSenha.delete(0, END)
        self.etd_email.delete(0, END)

    def voltar(self):
        self.controller.show_frame('FrLogin')

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x500')
    frame = FrCadastro(root, None)
    frame.pack()
    root.mainloop()