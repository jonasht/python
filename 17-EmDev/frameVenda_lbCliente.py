from tkinter import ttk
import tkinter as tk



class Fr_lbCliente(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lbfr_dadosClientes = ttk.LabelFrame(self, text='Info clientes')
        self.fr1 = ttk.Frame(self.lbfr_dadosClientes)
        self.fr2 = ttk.Frame(self.lbfr_dadosClientes)
        
        self.lb_id = ttk.Label(self.fr1, text='id:', width=7)
        self.lb_nome = ttk.Label(self.fr1, text='nome:', width=7)
        self.lb_cpf = ttk.Label(self.fr1, text='cpf:', width=7)
        self.lb_uf = ttk.Label(self.fr1, text='uf:', width=7)
        self.lb_cidade = ttk.Label(self.fr1, text='cidade:', width=7)
        self.lb_rua = ttk.Label(self.fr1, text='rua:', width=7)
        self.lb_numero = ttk.Label(self.fr1, text='numero:', width=7)
        self.lb_telefone = ttk.Label(self.fr1, text='telefone:', width=7)
        self.lb_email = ttk.Label(self.fr1, text='email:', width=7)
        
        self.lb_id.grid(row=0, column=0, padx=5, pady=2)
        self.lb_nome.grid(row=1, column=0, padx=5, pady=2)
        self.lb_cpf.grid(row=2, column=0, padx=5, pady=2)
        self.lb_uf.grid(row=3, column=0, padx=5, pady=2)
        self.lb_cidade.grid(row=4, column=0, padx=5, pady=2)
        self.lb_rua.grid(row=5, column=0, padx=5, pady=2)
        self.lb_numero.grid(row=6, column=0, padx=5, pady=2)
        self.lb_telefone.grid(row=7, column=0, padx=5, pady=2)
        self.lb_email.grid(row=8, column=0, padx=5, pady=2)

        
        self.lb_idInfo = ttk.Label(self.fr2, text='', width=30)
        self.lb_nomeInfo = ttk.Label(self.fr2, text='', width=30)
        self.lb_cpfInfo = ttk.Label(self.fr2, text='', width=30)
        self.lb_ufInfo = ttk.Label(self.fr2, text='', width=30)
        self.lb_cidadeInfo = ttk.Label(self.fr2, text='', width=30)
        self.lb_ruaInfo = ttk.Label(self.fr2, text='', width=30)
        self.lb_numeroInfo = ttk.Label(self.fr2, text='', width=30)
        self.lb_telefoneInfo = ttk.Label(self.fr2, text='', width=30)
        self.lb_emailInfo = ttk.Label(self.fr2, text='', width=30)

        self.lb_idInfo.grid(row=0, column=1, padx=5, pady=2)
        self.lb_nomeInfo.grid(row=1, column=1, padx=5, pady=2)
        self.lb_cpfInfo.grid(row=2, column=1, padx=5, pady=2)
        self.lb_ufInfo.grid(row=3, column=1, padx=5, pady=2)
        self.lb_cidadeInfo.grid(row=4, column=1, padx=5, pady=2)
        self.lb_ruaInfo.grid(row=5, column=1, padx=5, pady=2)
        self.lb_numeroInfo.grid(row=6, column=1, padx=5, pady=2)
        self.lb_telefoneInfo.grid(row=7, column=1, padx=5, pady=2)
        self.lb_emailInfo.grid(row=8, column=1, padx=5, pady=2)
        
        self.fr1.grid(row=0, column=0)
        self.fr2.grid(row=0, column=1)
        
        self.lbfr_dadosClientes.pack()
        

    def inserir_dados(self, dados):
        # dados = dados[0]
        print(dados)
        
        id = dados[0]
        nome = dados[1]
        cpf = dados[2]
        uf = dados[3]
        cidade = dados[4]
        rua = dados[5]
        numero = dados[6]
        telefone = dados[7]
        email = dados[8]
        
        # print('id:', id)
        # print('nome:', nome)
        # print('cpf:', cpf)
        # print('uf:', uf)
        # print('cidade:', cidade)
        # print('rua:', rua)
        # print('numero:', numero)
        # print('telefone:', telefone)
        # print('email:', email)
        
        self.lb_idInfo.config(text=id)
        self.lb_nomeInfo.config(text=nome)
        self.lb_cpfInfo.config(text=cpf)
        self.lb_ufInfo.config(text=uf)
        self.lb_cidadeInfo.config(text=cidade)
        self.lb_ruaInfo.config(text=rua)
        self.lb_numeroInfo.config(text=numero)
        self.lb_telefoneInfo.config(text=telefone)
        self.lb_emailInfo.config(text=email)

    def deletar_dados(self):
        self.lb_idInfo.config(text='')
        self.lb_nomeInfo.config(text='')
        self.lb_cpfInfo.config(text='')
        self.lb_ufInfo.config(text='')
        self.lb_cidadeInfo.config(text='')
        self.lb_ruaInfo.config(text='')
        self.lb_numeroInfo.config(text='')
        self.lb_telefoneInfo.config(text='')
        self.lb_emailInfo.config(text='')
       
        
        
if __name__ == '__main__':
    print('=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('so um teste')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=')
    dados = (5, 'Henrique', '522', 'SP', 'CAMPINAS', 
             'Carlos De Andrades', '896', '1938363132', 
             'henrique@outlook.com.br')    
    
    root = tk.Tk()
    root.geometry('500x500')
    frame = Fr_lbCliente(root)
    frame.inserir_dados(dados)
    frame.pack()

    root.mainloop()


