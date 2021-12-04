from tkinter import ttk
import tkinter as tk
from tkinter.constants import END, EW
from frameVenda_lbCliente import Fr_lbCliente
import func_clientes as funcC



class Fr_treeCliente(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        self.lbfr_pesqCliente = ttk.Labelframe(self, text='Pesquisar')
        self.etd_pesquisar = ttk.Entry(self.lbfr_pesqCliente)
        # Treeview cliente =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # definindo colunas
        self.colunas = ['id', 'nome', 'cpf', 'uf', 'cidade']
        self.treev = ttk.Treeview(self, columns=self.colunas, show='headings')

        # definindo heading
        self.treev.heading('id', text='ID')
        self.treev.heading('nome', text='Nome')
        self.treev.heading('cpf', text='CPF')
        self.treev.heading('uf', text='UF')
        self.treev.heading('cidade', text='Cidade')

        # definindo tamanho da coluna
        self.treev.column('id', width=10)
        self.treev.column('nome', width=150)
        self.treev.column('cpf', width=150)
        self.treev.column('uf', width=50)
        self.treev.column('cidade', width=100)

        self.etd_pesquisar.grid(row=0, column=0, padx=5, pady=2)
        self.treev.grid(row=1, column=0, padx=5, pady=2)
        self.lbfr_pesqCliente.grid(row=0, column=0, sticky=EW, padx=5, pady=2)
        


        self.etd_pesquisar.bind('<KeyRelease>', self.digitar_evento)
        self.treev.bind('<<TreeviewSelect>>', self.item_selected)
        self.mostrar_tree()
        
 

    def inserir_dados(self):
        # pegando dados
        dados = funcC.pesquisar(self.id)
        print(dados)
        dados = dados[0]

        # mandar os dados para o pai
        self.con.inserir_cliente(dados)
       
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
    frame = Fr_treeCliente(root, root)
    frame.pack()
    root.geometry('500x500')
    root.mainloop()

