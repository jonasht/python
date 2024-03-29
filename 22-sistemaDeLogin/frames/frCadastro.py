import tkinter as tk
from tkinter import IntVar, ttk, BooleanVar
from tkinter.constants import END, EW, LEFT, RIGHT, TOP, W, X

import uteis as u




class FrCadastro(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.lbfr_principal = ttk.LabelFrame(self, text='Cadastrar nova conta')

             
        # botao voltar
        self.bt_voltar = ttk.Button(self, text='Voltar', command=self.voltar)


        self.lb_nome = ttk.Label(self.lbfr_principal, text='Nome:')
        self.etd_nome = ttk.Entry(self.lbfr_principal)

        self.lb_sobrenome = ttk.Label(self.lbfr_principal, text='Sobrenome:')
        self.etd_sobrenome = ttk.Entry(self.lbfr_principal)

        self.lb_login = ttk.Label(self.lbfr_principal, text='Login:')
        self.etd_login = ttk.Entry(self.lbfr_principal)

        self.lb_senha = ttk.Label(self.lbfr_principal, text='Senha:')
        self.etd_senha = ttk.Entry(self.lbfr_principal, show='*')
        
        self.check_var = BooleanVar()
        self.ckbt_senha = ttk.Checkbutton(self.lbfr_principal, 
                                          variable=self.check_var,
                                          command=self.check_event)

        self.lb_reSenha = ttk.Label(self.lbfr_principal, text='Repetir Senha:')
        self.etd_reSenha = ttk.Entry(self.lbfr_principal, show='*') 

        self.lb_email = ttk.Label(self.lbfr_principal, text='Email:')
        self.etd_email = ttk.Entry(self.lbfr_principal)

        self.lb_nome.grid(row=0, column=0, pady=6)
        self.etd_nome.grid(row=0, column=1, pady=6)
        self.lb_sobrenome.grid(row=1, column=0, pady=6)
        self.etd_sobrenome.grid(row=1, column=1, pady=6)


        self.lb_login.grid(row=2, column=0, pady=6)
        self.etd_login.grid(row=2, column=1, pady=6)
        
        self.lb_senha.grid(row=3, column=0, pady=6)
        self.etd_senha.grid(row=3, column=1, pady=6)
        self.ckbt_senha.grid(row=3, column=2, pady=6, padx=10)

        self.lb_reSenha.grid(row=4, column=0, pady=6)
        self.etd_reSenha.grid(row=4, column=1, pady=6)

        self.lb_email.grid(row=5, column=0, pady=6)
        self.etd_email.grid(row=5, column=1, pady=6)
        
        # label aviso =-=-=-=-=-=-=-=-=-=-=-=-=
        self.lb_aviso = ttk.Label(self.lbfr_principal, text='')
        self.lb_aviso.grid(row=6, column=0, columnspan=3)

        # bottons =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.bt_limpar = ttk.Button(self.lbfr_principal, text='Limpar', command=self.limpar)
        self.bt_cadastrar = ttk.Button(self.lbfr_principal, text='Cadastrar', command=self.cadastrar)

        self.bt_limpar.grid(row=7, column=0, sticky=EW, padx=3, pady=6)
        self.bt_limpar.config(width=15)
        self.bt_cadastrar.grid(row=7, column=1, sticky=EW, padx=3, pady=6, columnspan=1)
        

        self.lbfr_principal.pack(side=TOP)
        self.bt_voltar.pack(side=TOP, pady=15)
 


        
        # entry windth -=-=-=-=-=-=-=-=-=-=-=-=
        entry_width = 40
        self.etd_nome.config(width=entry_width)
        self.etd_sobrenome.config(width=entry_width)
        self.etd_login.config(width=entry_width)
        self.etd_senha.config(width=entry_width)
        self.etd_reSenha.config(width=entry_width)
        self.etd_email.config(width=entry_width)
        
        
        self.lbfr_principal.config(padding=20)
        
        self.bt_voltar.config(width=entry_width+30)

    def check_event(self):
        char = '' if self.check_var.get() else '*'
        self.etd_senha.config(show=char)
        self.etd_reSenha.config(show=char)
    
    def cadastrar(self):
        nome = self.etd_nome.get()
        sobrenome = self.etd_sobrenome.get()
        login = self.etd_login.get()
        senha = self.etd_senha.get()
        resenha = self.etd_reSenha.get()
        email = self.etd_email.get()

 

        if login:
            if not(u.login_in_data(login)):
                if senha and resenha:
                    if senha == resenha:
                        u.add_data(nome=nome, sobrenome=sobrenome, login=login, senha=senha, email=email)
                        self.lb_aviso.config(text='Cadastro Feito com sucesso', foreground='green')
                        self.limpar()
                        
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
        self.check_var.set(False)
        
    def voltar(self):
        # self.controller.show_frame('FrLogin')
        self.controller.show_login()
        self.limpar()

if __name__ == '__main__':
    # root = tk.Tk()
    # root.geometry('500x500')
    # frame = FrCadastro(root, None)
    # frame.pack()
    # root.mainloop()
    import main
    root = main.Principal()
    root.show_cadastro()
    root.mainloop()