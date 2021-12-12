from tkinter import ttk
import tkinter as tk
from tkinter.constants import END, EW, NS, VERTICAL
# import func_produtos as funcP
import func.produtos as funcP


class Fr_treeProduto(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        
        self.fr_pesProduto = ttk.Frame(self)
        self.lbfr = ttk.LabelFrame(self, text='Pesquisar')
        

        self.etd_pesquisar = ttk.Entry(self.lbfr)
        self.etd_pesquisar.grid(row=0, column=1, sticky=EW, padx=5, pady=2)
        

        
        # Treeview produto ------------------------------------
        # definindo colunas
        self.fr_tree = ttk.Frame(self)
        self.colunas = ['cod', 'nome', 'marca', 'qtd']
        self.tree_produto = ttk.Treeview(self.fr_tree, columns=self.colunas, show='headings' )

        # definindo heading
        self.tree_produto.heading('cod', text='ID')
        self.tree_produto.heading('nome', text='Nome')
        self.tree_produto.heading('marca', text='Marca')
        self.tree_produto.heading('qtd', text='Quantidade')

        # definindo tamanho da coluna
        self.tree_produto.column('cod', width=30)
        self.tree_produto.column('nome', width=180)
        self.tree_produto.column('marca', width=150)
        self.tree_produto.column('qtd', width=100)

        self.scroll = ttk.Scrollbar(self.fr_tree, orient=VERTICAL, command=self.tree_produto.yview)
        
        self.tree_produto.grid(row=0, column=0, columnspan=1)
        self.scroll.grid(row=0, column=1, rowspan=1, sticky=NS)

        # colocando frames principais
        self.lbfr.grid(row=0, column=0, sticky=EW, padx=5, pady=2)
        #tree + scroll
        self.fr_tree.grid(row=1, column=0, padx=5, pady=2)
        

        self.fr_pesProduto.grid(row=0, column=0)

        
        self.etd_pesquisar.bind('<KeyRelease>', self.digitar_evento)
        self.tree_produto.bind('<<TreeviewSelect>>', self.item_selected)
        self.mostrar_tree()
        
  

    def editar_dados(self) -> None:
        print(self.codigo)
        if self.codigo != '':


            codigo = self.codigo

            qtd =self.etd_qtd.get()
            preco =self.etd_preco.get()
            
            # add dados =-=-=-=-=-=-=-=-=-=-=-=-=
            print('codigo:', codigo)
            # print('nome:', nome)
            # print('marca:', marca)
            print('qtd:', qtd)
            print('preco:', preco)


            self.deletar_tree()
            self.mostrar_tree()
    

    def inserir_dados(self):
        # pegando dados
        dados = funcP.pesquisar(self.codigo)
        print(dados)
        dados = dados[0]

        # mandar dados para o pai 
        self.con.inserir_produto(dados)
        

    def item_selected(self, event):
        for selected_item in self.tree_produto.selection():
            item = self.tree_produto.item(selected_item)
            record = item['values']

            print(record)
            
            self.codigo = record[0]
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
        self.tree_produto.delete(*self.tree_produto.get_children()) 
    def mostrar_tree(self, palavras=''):

        dados = funcP.get_()
        print(dados)
        print('\n')

        dadosTree = list()
        for d in dados:
            dadosTree.append(d[:4])
            
            print('tree', dadosTree)
        
        print(dadosTree)
        
        if palavras != '':
            for d in dadosTree:
                # print(d)
                if palavras.lower() in d[1].lower():
                    self.tree_produto.insert('', END, values=d)
        else:
            for d in dadosTree:
                self.tree_produto.insert('', END, values=d)

if __name__ == '__main__':
    root = tk.Tk()
    frame = Fr_treeProduto(root, root)
    frame.pack()

    root.geometry('500x500')

    root.mainloop()