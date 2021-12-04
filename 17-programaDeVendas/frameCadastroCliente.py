from tkinter import Pack, ttk
import tkinter as tk
from tkinter.constants import BOTH, END, LEFT, RIGHT, W, EW
import func_clientes as fc


class FrameCadastroCliente(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lbfr_cadastrarCliente = ttk.LabelFrame(self, text='Cadastrar Cliente')

        self.lb_nome = ttk.Label(self.lbfr_cadastrarCliente, text='Nome:')
        self.etd_nome = ttk.Entry(self.lbfr_cadastrarCliente)
        
        self.lb_cpf = ttk.Label(self.lbfr_cadastrarCliente, text='CPF:')
        self.etd_cpf = ttk.Entry(self.lbfr_cadastrarCliente)
        
        self.lb_uf = ttk.Label(self.lbfr_cadastrarCliente, text='UF:')
        self.etd_uf = ttk.Entry(self.lbfr_cadastrarCliente)

        self.lb_cidade = ttk.Label(self.lbfr_cadastrarCliente, text='Cidade:')
        self.etd_cidade = ttk.Entry(self.lbfr_cadastrarCliente)
        
        self.lb_rua = ttk.Label(self.lbfr_cadastrarCliente, text='Rua:')
        self.etd_rua = ttk.Entry(self.lbfr_cadastrarCliente)
        
        self.lb_numeroCasa = ttk.Label(self.lbfr_cadastrarCliente, text='Numero:')
        self.etd_numeroCasa = ttk.Entry(self.lbfr_cadastrarCliente)
        
        self.lb_telefone = ttk.Label(self.lbfr_cadastrarCliente, text='Telefone:')
        self.etd_telefone  = ttk.Entry(self.lbfr_cadastrarCliente)
        
        self.lb_email = ttk.Label(self.lbfr_cadastrarCliente, text='Email:')
        self.etd_email = ttk.Entry(self.lbfr_cadastrarCliente)
        
        self.fr_bts = ttk.Frame(self)
        
        self.bt_cadastrar = ttk.Button(self.fr_bts, text='Cadastrar', command=self.cadastrar)
        self.bt_resetar = ttk.Button(self.fr_bts, text='Resetar', command=self.resetar)

        # label aviso
        self.lb_aviso = ttk.Label(self, text='')

        # -------------------------------------------------
        self.lb_nome.grid(row=0, column=0, padx=5, pady=2)
        self.etd_nome.grid(row=0, column=1, padx=5, pady=2)
        
        self.lb_cpf.grid(row=1, column=0, padx=5, pady=2)
        self.etd_cpf.grid(row=1, column=1, padx=5, pady=2)
        
        self.lb_uf.grid(row=2, column=0, padx=5, pady=2)
        self.etd_uf.grid(row=2, column=1, padx=5, pady=2)

        self.lb_cidade.grid(row=3, column=0, padx=5, pady=2)
        self.etd_cidade.grid(row=3, column=1, padx=5, pady=2)

        self.lb_rua.grid(row=4, column=0, padx=5, pady=2)
        self.etd_rua.grid(row=4, column=1, padx=5, pady=2)
        
        self.lb_numeroCasa.grid(row=5, column=0, padx=5, pady=2)
        self.etd_numeroCasa.grid(row=5, column=1, padx=5, pady=2)

        self.lb_telefone.grid(row=6, column=0, padx=5, pady=2)
        self.etd_telefone .grid(row=6, column=1, padx=5, pady=2)

        self.lb_email.grid(row=7, column=0, padx=5, pady=2)
        self.etd_email.grid(row=7, column=1, padx=5, pady=2)

        self.bt_cadastrar.pack(side=RIGHT, fill=BOTH, expand=True, padx=1, pady=2)
        self.bt_resetar.pack(side=LEFT, fill=BOTH, expand=True, padx=1, pady=2)
        
        # colocando labelFrame
        self.lbfr_cadastrarCliente.pack()
        self.fr_bts.pack(fill=BOTH, expand=True)
        self.lb_aviso.pack()
        
        
        
        # focar no nome
        self.etd_nome.focus()

    def cadastrar(self):
        nome = self.etd_nome.get()
        cpf = self.etd_cpf.get()
        uf = self.etd_uf.get()
        cidade = self.etd_cidade.get()
        rua = self.etd_rua.get()
        numero = self.etd_numeroCasa.get()
        telefone = self.etd_telefone.get()
        email = self.etd_email.get()


        # print('dados:')
        # print('nome:', nome, 'cpf:', cpf )
        # print('uf:', uf, 'cidade:', cidade, 'rua:', rua, numero)
        # print('fone:', telefone, 'email:', email)
        
        if nome != '':
            fc.add_(nome, cpf, uf, cidade, rua, numero, telefone, email)
            self.resetar()
            self.lb_aviso.config(text='cadastro feito com sucesso', foreground='green')
        else:
            self.lb_aviso.config(text='campo nome obrigatorio', foreground='red')
            
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
    root = tk.Tk()
    frame = FrameCadastroCliente(root)
    frame.pack()
    root.geometry('600x500')
    root.mainloop()