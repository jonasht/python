from tkinter import *
import uteis as u




class FrCadastro(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        # botao voltar
        self.bt_voltar = Button(self, text='Voltar', command=self.voltar)
        self.bt_voltar.pack(side=RIGHT, anchor='nw')


        self.lbfr_principal = LabelFrame(self, text='Cadastrar nova conta')
        
        self.lb_nome = Label(self.lbfr_principal, text='Nome:')
        self.etd_nome = Entry(self.lbfr_principal)

        self.lb_sobrenome = Label(self.lbfr_principal, text='sobrenome:')
        self.etd_sobrenome = Entry(self.lbfr_principal)

        self.lb_login = Label(self.lbfr_principal, text='Login:')
        self.etd_login = Entry(self.lbfr_principal)

        self.lb_senha = Label(self.lbfr_principal, text='Senha:')
        self.etd_senha = Entry(self.lbfr_principal, show='*')
        self.ckbt_senha = Checkbutton(self.lbfr_principal, command=self.mostrar_senha, text='')

        self.lb_reSenha = Label(self.lbfr_principal, text='repetir Senha:')
        self.etd_reSenha = Entry(self.lbfr_principal, show='*') 

        self.lb_email = Label(self.lbfr_principal, text='Email:')
        self.etd_email = Entry(self.lbfr_principal)

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

        self.bt_limpar = Button(self.lbfr_principal, text='Limpar', command=self.limpar)
        self.bt_cadastrar = Button(self.lbfr_principal, text='Cadastrar', command=self.cadastrar)

        self.bt_limpar.grid(row=6, column=0)
        self.bt_cadastrar.grid(row=6, column=1)

        self.lbfr_principal.pack()


        # label aviso =-=-=-=-=-=-=-=-=-=-=-=-=
        self.lb_aviso = Label(self, text='')
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
                        # u.add_data(nome=nome, sobrenome=sobrenome, login=login, senha=senha, email=email)
                        self.lb_aviso.config(text='Cadastro Feito com sucesso', fg='green')
                        print(nome, sobrenome, login, senha, resenha, email)
                    else:
                        self.lb_aviso.config(text='senhas precisam ser iguais', fg='red')
                        
                else:
                    self.lb_aviso.config(text='as duas senhas sao obrigatorias', fg='red')
            else:
                self.lb_aviso.config(text='login ja existente', fg='red')       
        else:
            self.lb_aviso.config(text='campo login eh obrigatorio', fg='red')

        
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
    root = Tk()
    root.geometry('500x500')
    frame = FrCadastro(root, None)
    frame.pack()
    root.mainloop()