
from tkinter import Frame, Label, ttk
import tkinter as tk
from tkinter.constants import BOTH, DISABLED, END, EW, LEFT, NORMAL, RIGHT, W
import func_clientes as funcC



class FrPesquisarCliente(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # guardando nome
        self.nome = ''
        self.id = ''

        # definindo frames =-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
        self.lbfr_cliente = ttk.LabelFrame(self, text='Cliente')
        self.fr_cliente_p1 = ttk.Frame(self.lbfr_cliente)
        self.fr_cliente_p2 = ttk.Frame(self.lbfr_cliente)

        self.fr_esquerdo = ttk.Frame(self)

        self.lbfr = ttk.LabelFrame(self.fr_esquerdo, text='Pesquisar')
        
        self.lb_pesquisar = ttk.Label(self.lbfr, text='Nome:')
        self.lb_pesquisar.grid(row=0, column=0)
        
        self.etd_pesquisar = ttk.Entry(self.lbfr)
        self.etd_pesquisar.grid(row=0, column=1, sticky=EW)
        

        self.lb_id = ttk.Label(self.fr_cliente_p1, text='ID:')
        self.lb_nome = ttk.Label(self.fr_cliente_p1, text='Nome:')
        self.lb_cpf = ttk.Label(self.fr_cliente_p1, text='CPF:')
        self.lb_uf = ttk.Label(self.fr_cliente_p1, text='UF:')
        self.lb_cidade = ttk.Label(self.fr_cliente_p1, text='Cidade:')
        
        self.lb_rua = ttk.Label(self.fr_cliente_p2, text='Rua:')
        self.lb_numero = ttk.Label(self.fr_cliente_p2, text='Numero:')
        self.lb_fone = ttk.Label(self.fr_cliente_p2, text='Fone:')
        self.lb_email = ttk.Label(self.fr_cliente_p2, text='E-mail:')
        
        
        
        self.lb_idInfo = ttk.Label(self.fr_cliente_p1, text='')
        self.etd_nome = ttk.Entry(self.fr_cliente_p1, foreground='black')
        self.etd_cpf = ttk.Entry(self.fr_cliente_p1, foreground='black')
        self.etd_uf = ttk.Entry(self.fr_cliente_p1, foreground='black')
        self.etd_cidade = ttk.Entry(self.fr_cliente_p1, foreground='black')
        
        self.etd_rua = ttk.Entry(self.fr_cliente_p2, foreground='black')
        self.etd_numero = ttk.Entry(self.fr_cliente_p2, foreground='black')
        self.etd_fone = ttk.Entry(self.fr_cliente_p2, foreground='black')
        self.etd_email = ttk.Entry(self.fr_cliente_p2, foreground='black')
        
        
        self.bt_editar = ttk.Button(self.lbfr_cliente, text='Editar', command=self.editar_dados)

        self.lb_id.grid(row=0, column=0, padx=5, pady=2)
        self.lb_nome.grid(row=1, column=0, padx=5, pady=2)
        self.lb_cpf.grid(row=2, column=0, padx=5, pady=2)
        self.lb_uf.grid(row=3, column=0, padx=5, pady=2)
        self.lb_cidade.grid(row=4, column=0, padx=5, pady=2)
        
        self.lb_rua.grid(row=1, column=0, padx=5, pady=2)
        self.lb_numero.grid(row=2, column=0, padx=5, pady=2)
        self.lb_fone.grid(row=3, column=0, padx=5, pady=2)
        self.lb_email.grid(row=4, column=0, padx=5, pady=2)

        


        self.lb_idInfo.grid(row=0, column=1, padx=5, pady=2)
        self.etd_nome.grid(row=1, column=1, padx=5, pady=2)
        self.etd_cpf.grid(row=2, column=1, padx=5, pady=2)
        self.etd_uf.grid(row=3, column=1, padx=5, pady=2)
        self.etd_cidade.grid(row=4, column=1, padx=5, pady=2)
        
        self.etd_rua.grid(row=1, column=1, padx=5, pady=2)
        self.etd_numero.grid(row=2, column=1, padx=5, pady=2)
        self.etd_fone.grid(row=3, column=1, padx=5, pady=2)
        self.etd_email.grid(row=4, column=1, padx=5, pady=2)
                
        # colocando botao editar
        self.bt_editar.grid(row=9, columnspan=2, sticky=EW)


        # Treeview =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # definindo colunas
        self.colunas = ['id', 'nome', 'cpf', 'uf', 'cidade']
        self.treev = ttk.Treeview(self.fr_esquerdo, columns=self.colunas, show='headings' )

        # definindo heading
        self.treev.heading('id', text='ID')
        self.treev.heading('nome', text='Nome')
        self.treev.heading('cpf', text='CPF')
        self.treev.heading('uf', text='UF')
        self.treev.heading('cidade', text='Cidade')

        # definindo tamanho da coluna
        self.treev.column('id', width=10)
        self.treev.column('nome', width=150)
        self.treev.column('uf', width=50)
        self.treev.column('cidade', width=100)

        self.treev.grid(row=1, column=0, columnspan=3)
        self.lbfr.grid(row=0, column=0)
        


        # colocando frames 
        self.lbfr_cliente.pack(fill=BOTH)
        self.fr_cliente_p1.grid(row=0, column=0)
        self.fr_cliente_p2.grid(row=0, column=1)
        
        self.fr_esquerdo.pack(fill=BOTH)
        
        
        self.etd_pesquisar.bind('<KeyRelease>', self.digitar_evento)
        self.treev.bind('<<TreeviewSelect>>', self.item_selected)
        self.mostrar_tree()
        
        # desativando entradas/entry 
        self.etds_disabled()
        

  
    def etds_normal(self):
            # self.etd_id.config(state=NORMAL)
            self.etd_nome.config(state=NORMAL)
            self.etd_cpf.config(state=NORMAL)
            self.etd_uf.config(state=NORMAL)
            self.etd_cidade.config(state=NORMAL)
            self.etd_rua.config(state=NORMAL)
            self.etd_numero.configure(state=NORMAL)
            self.etd_fone.config(state=NORMAL)
            self.etd_email.config(state=NORMAL)        
    
    def etds_disabled(self):
            # self.etd_id.config(state=DISABLED)
            self.etd_nome.config(state=DISABLED)
            self.etd_cpf.config(state=DISABLED)
            self.etd_uf.config(state=DISABLED)
            self.etd_cidade.config(state=DISABLED)
            self.etd_rua.config(state=DISABLED)
            self.etd_numero.config(state=DISABLED)
            self.etd_fone.config(state=DISABLED)
            self.etd_email.config(state=DISABLED)     
            
            # mudando botao editar para editar
            self.bt_editar.config(text='Editar')   
            
    def editar_dados(self):
        if self.id != '':

            if str(self.etd_nome['state']) == NORMAL:
                # id = self.etd_id.get()
                nome = self.etd_nome.get()
                cpf = self.etd_cpf.get()
                uf = self.etd_uf.get()
                cidade = self.etd_cidade.get()
                rua = self.etd_rua.get()
                numero = self.etd_numero.get()
                fone = self.etd_fone.get()
                email = self.etd_email.get()
                
                # update dados =-=-=-=-=-=-=-=-=-=-=-=-=
                print('id:', self.id)
                print('nome:', nome)
                print('cpf:', cpf)
                print('uf:', uf)
                print('cidade:', cidade)
                print('rua:', rua)
                print('numero:', numero)
                print('fone:', fone)
                print('email:', email)
                
                funcC.update_(id=self.id, nome=nome, cpf=cpf,
                              uf=uf, cidade=cidade,
                              rua=rua, numero=numero,
                              telefone=fone, email=email)
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                
                self.etds_disabled()  
                self.bt_editar.config(text='Editar')

                self.deletar_tree()
                self.mostrar_tree()
            else:
                self.bt_editar.config(text='OK')
                self.etds_normal()

    
    def deletar_dados(self):
        # self.etd_id.delete(0, END)
        self.etd_nome.delete(0, END)
        self.etd_cpf.delete(0, END)
        self.etd_uf.delete(0, END)
        self.etd_cidade.delete(0, END)
        self.etd_rua.delete(0, END)
        self.etd_numero.delete(0, END)
        self.etd_fone.delete(0, END)
        self.etd_email.delete(0, END)
    
    def inserir_dados(self):
        # pegando dados
        dados = funcC.pesquisar(self.id)
        print(dados)
        dados = dados[0]

        # ativando entradas
        self.etds_normal()

        self.deletar_dados()
        
        self.lb_idInfo.config(text=dados[0])
        self.etd_nome.insert(END, dados[1])
        self.etd_cpf.insert(END, dados[2])
        self.etd_uf.insert(END, dados[3])
        self.etd_cidade.insert(END, dados[4])
        self.etd_rua.insert(END, dados[5])
        self.etd_numero.insert(END, dados[6])
        self.etd_fone.insert(END, dados[7])
        self.etd_email.insert(END, dados[8])


        self.etds_disabled()
    def item_selected(self, event):
        for selected_item in self.treev.selection():
            item = self.treev.item(selected_item)
            record = item['values']
            # show a message
            print(record)
            
            self.id = record[0]
            self.inserir_dados()
        
    def digitar_evento(self, event):
        variavel = event.widget.get()
        print(variavel)
        # deletar tree view
        self.deletar_tree()

        # mostrar treeview com a palavra digitada
        self.mostrar_tree(palavras=variavel)
        
    def deletar_tree(self):
        # deletar toda a tree view
        self.treev.delete(*self.treev.get_children()) 
    def mostrar_tree(self, palavras=''):

        dados = funcC.get_()
        print(dados)
        print('\n')

        dadosTree = list()
        for d in dados:
            # print(d[:5])
            dadosTree.append(d[:5])
            
            print('tree', dadosTree)
        
        print(dadosTree)
        
        if palavras != '':
            for d in dadosTree:
                # print(d)
                if palavras.lower() in d[1].lower():
                    self.treev.insert('', END, values=d)
        else:
            for d in dadosTree:
                self.treev.insert('', END, values=d)


if __name__ == '__main__':
    root = tk.Tk()
    frame = FrPesquisarCliente(root)
    frame.pack()
    root.geometry('1000x500')
    root.mainloop()