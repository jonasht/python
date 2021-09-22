from tkinter import *

class FrameCadastroCliente(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lbfr_cadastrarCliente = LabelFrame(self, text='Cadastrar Cliente')

        self.lb_nome = Label(self.lbfr_cadastrarCliente, text='Nome:')
        self.etd_nome = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_cpf = Label(self.lbfr_cadastrarCliente, text='CPF:')
        self.etd_cpf = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_rua = Label(self.lbfr_cadastrarCliente, text='Rua:')
        self.etd_rua = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_numeroCasa = Label(self.lbfr_cadastrarCliente, text='Numero:')
        self.etd_numeroCasa = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_telefone = Label(self.lbfr_cadastrarCliente, text='Telefone:')
        self.etd_telefone  = Entry(self.lbfr_cadastrarCliente)
        
        self.lb_email = Label(self.lbfr_cadastrarCliente, text='Email:')
        self.etd_email = Entry(self.lbfr_cadastrarCliente)
        
        self.bt_cadastrar = Button(self.lbfr_cadastrarCliente, text='Cadastrar')
        self.bt_reset = Button(self.lbfr_cadastrarCliente, text='Resetar')

        # -------------------------
        self.lb_nome.grid(row=0, column=0)
        self.etd_nome.grid(row=0, column=1)
        
        self.lb_cpf.grid(row=1, column=0)
        self.etd_cpf.grid(row=1, column=1)
        
        self.lb_rua.grid(row=2, column=0)
        self.etd_rua.grid(row=2, column=1)
        
        self.lb_numeroCasa.grid(row=3, column=0)
        self.etd_numeroCasa.grid(row=3, column=1)

        self.lb_telefone.grid(row=4, column=0)
        self.etd_telefone .grid(row=4, column=1)

        self.lb_email.grid(row=5, column=0)
        self.etd_email.grid(row=5, column=1)

        self.bt_cadastrar.grid(row=6, column=1)
        self.bt_reset.grid(row=6, column=0)
        
        # colocando labelFrame
        self.lbfr_cadastrarCliente.pack()

if __name__ == '__main__':
    root = Tk()
    frame = FrameCadastroCliente(root)
    frame.pack()
    root.geometry('600x500')
    root.mainloop()