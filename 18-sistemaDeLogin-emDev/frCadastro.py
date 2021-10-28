from tkinter import *

class FrCadastro(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lbfr_principal = LabelFrame(self, text='Cadastrar nova conta')
        
        
        self.lb_login = Label(self.lbfr_principal, text='Login:')
        self.etd_login = Entry(self.lbfr_principal)

        self.lb_senha = Label(self.lbfr_principal, text='Senha:')
        self.etd_senha = Entry(self.lbfr_principal)

        self.lb_reSenha = Label(self.lbfr_principal, text='repetir Senha:')
        self.etd_reSenha = Entry(self.lbfr_principal) 

        self.lb_login.grid(row=0, column=0)
        self.etd_login.grid(row=0, column=1)
        
        self.lb_senha.grid(row=1, column=0)
        self.etd_senha.grid(row=1, column=1)
        
        self.lb_reSenha.grid(row=2, column=0)
        self.etd_reSenha.grid(row=2, column=1)

        self.bt_limpar = Button(self.lbfr_principal, text='Limpar')
        self.bt_cadastrar = Button(self.lbfr_principal, text='Cadastrar')

        self.bt_limpar.grid(row=3, column=0)
        self.bt_cadastrar.grid(row=3, column=1)

        self.lbfr_principal.pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x500')
    frame = FrCadastro(root)
    frame.pack()
    root.mainloop()