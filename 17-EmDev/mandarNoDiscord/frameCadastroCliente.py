from tkinter import *
import func_clientes as fc

class FrameCadastroCliente(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lbfr_cadastrarCliente = LabelFrame(self, text='Cadastrar Cliente')

        self.lb_nome = Label(self.lbfr_cadastrarCliente, text='Nome:')
        self.etd_nome = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_cpf = Label(self.lbfr_cadastrarCliente, text='CPF:')
        self.etd_cpf = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_uf = Label(self.lbfr_cadastrarCliente, text='UF:')
        self.etd_uf = Entry(self.lbfr_cadastrarCliente)

        self.lb_cidade = Label(self.lbfr_cadastrarCliente, text='Cidade:')
        self.etd_cidade = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_rua = Label(self.lbfr_cadastrarCliente, text='Rua:')
        self.etd_rua = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_numeroCasa = Label(self.lbfr_cadastrarCliente, text='Numero:')
        self.etd_numeroCasa = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_telefone = Label(self.lbfr_cadastrarCliente, text='Telefone:')
        self.etd_telefone  = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_email = Label(self.lbfr_cadastrarCliente, text='Email:')
        self.etd_email = Entry(self.lbfr_cadastrarCliente)
        
        self.bt_cadastrar = Button(self.lbfr_cadastrarCliente, text='Cadastrar', command=self.cadastrar)
        self.bt_reset = Button(self.lbfr_cadastrarCliente, text='Resetar', command=self.resetar)

        # label aviso
        self.lb_aviso = Label(self, text='')

        # -------------------------------------------------
        self.lb_nome.grid(row=0, column=0)
        self.etd_nome.grid(row=0, column=1)
        
        self.lb_cpf.grid(row=1, column=0)
        self.etd_cpf.grid(row=1, column=1)
        
        self.lb_uf.grid(row=2, column=0)
        self.etd_uf.grid(row=2, column=1)

        self.lb_cidade.grid(row=3, column=0)
        self.etd_cidade.grid(row=3, column=1)

        self.lb_rua.grid(row=4, column=0)
        self.etd_rua.grid(row=4, column=1)
        
        self.lb_numeroCasa.grid(row=5, column=0)
        self.etd_numeroCasa.grid(row=5, column=1)

        self.lb_telefone.grid(row=6, column=0)
        self.etd_telefone .grid(row=6, column=1)

        self.lb_email.grid(row=7, column=0)
        self.etd_email.grid(row=7, column=1)

        self.bt_cadastrar.grid(row=8, column=1)
        self.bt_reset.grid(row=8, column=0)
        
        # colocando labelFrame
        self.lbfr_cadastrarCliente.pack()
        self.lb_aviso.pack()
        
        # focar no nome
        self.etd_nome.focus()

    def cadastrar(self):
        print('cadastrar')
        nome = self.etd_nome.get()
        cpf = self.etd_cpf.get()
        uf = self.etd_uf.get()
        cidade = self.etd_cidade.get()
        rua = self.etd_rua.get()
        numero = self.etd_numeroCasa.get()
        telefone = self.etd_telefone.get()
        email = self.etd_email.get()


        print('dados:')
        print('nome:', nome, 'cpf:', cpf )
        print('uf:', uf, 'cidade:', cidade, 'rua:', rua, numero)
        print('fone:', telefone, 'email:', email)
        
        if nome != '':
            fc.add_(nome, cpf, uf, cidade, rua, numero, telefone, email)
            self.resetar()
            self.lb_aviso.config(text='cadastro feito com sucesso', fg='green')
        else:
            self.lb_aviso.config(text='campo nome obrigatorio', fg='red')
            
    def resetar(self):
        self.etd_nome.delete(0, END)
        self.etd_cpf.delete(0, END)
        self.etd_uf.delete(0, END)
        self.etd_cidade.delete(0, END)
        self.etd_rua.delete(0, END)
        self.etd_numeroCasa.delete(0, END)
        self.etd_telefone.delete(0, END)
        self.etd_email.delete(0, END)
        
        self.etd_nome.focus()
        
if __name__ == '__main__':
    root = Tk()
    frame = FrameCadastroCliente(root)
    frame.pack()
    root.geometry('600x500')
    root.mainloop()