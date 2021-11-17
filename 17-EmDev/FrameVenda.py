
from tkinter import ttk
import tkinter as tk
from tkinter.constants import BOTH, DISABLED, END, EW, LEFT, N, NO, NORMAL, NS, RIGHT, VERTICAL

from colorama.ansi import Fore
import func_produtos as funcP




class FrVenda(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # guardando id
        self.codigo = ''

        # definindo frames =-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=- 
        self.fr_direita = ttk.Frame(self)
        self.fr_esquerdo = ttk.Frame(self)
        self.fr_tree2 = ttk.Frame(self)
        self.frame = ttk.Frame(self.fr_esquerdo)
        self.lbfr = ttk.LabelFrame(self.frame, text='Pesquisar')
        
        self.lb_pesquisar = ttk.Label(self.lbfr, text='nome:')
        self.lb_pesquisar.grid(row=0, column=0)
        
        self.etd_pesquisar = ttk.Entry(self.lbfr)
        self.etd_pesquisar.grid(row=0, column=1, sticky=EW)
        

        self.lb_codigo = ttk.Label(self.fr_direita, text='Codigo:')
        self.lb_nome = ttk.Label(self.fr_direita, text='Nome:')
        self.lb_marca = ttk.Label(self.fr_direita, text='Marca:')
        self.lb_descricao = ttk.Label(self.fr_direita, text='Descriação:')
        self.lb_qtd = ttk.Label(self.fr_direita, text='Quantidade:')
        self.lb_preco = ttk.Label(self.fr_direita, text='Preço:')
                
        
        self.lb_codigoInfo = ttk.Label(self.fr_direita, text='')

        # self.lb_codigoInfo = ttk.Entry(self.fr_direita, foreground='black')
        
        self.lb_nomeInfo = ttk.Label(self.fr_direita, foreground='black', text='')
        self.lb_marcaInfo = ttk.Label(self.fr_direita, foreground='black', text='')
        self.lb_descricaoInfo = tk.Label(self.fr_direita, width=40, height=10, text='')
        
        self.etd_qtd = ttk.Entry(self.fr_direita, foreground='black')
        self.etd_preco = ttk.Entry(self.fr_direita, foreground='black')
        
        self.bt_editar = ttk.Button(self.fr_direita, text='adicionar >>>', command=self.editar_dados)

        self.lb_codigo.grid(row=0, column=0)
        self.lb_nome.grid(row=1, column=0)
        self.lb_marca.grid(row=2, column=0)
        self.lb_descricao.grid(row=3, column=0)
        self.lb_qtd.grid(row=4, column=0)
        self.lb_preco.grid(row=5, column=0)

        self.lb_codigoInfo.grid(row=0, column=1)
        self.lb_nomeInfo.grid(row=1, column=1)
        self.lb_marcaInfo.grid(row=2, column=1)
        self.lb_descricaoInfo.grid(row=3, column=1)

        self.etd_qtd.grid(row=4, column=1)
        self.etd_preco.grid(row=5, column=1)
        
        # colocando botao editar
        self.bt_editar.grid(row=8, columnspan=2, sticky=EW)




        # Treeview =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # definindo colunas
        self.colunas = ['cod', 'nome', 'marca', 'qtd']
        self.treev = ttk.Treeview(self.fr_esquerdo, columns=self.colunas, show='headings' )

        # definindo heading
        self.treev.heading('cod', text='ID')
        self.treev.heading('nome', text='Nome')
        self.treev.heading('marca', text='Marca')
        self.treev.heading('qtd', text='Quantidade')

        # definindo tamanho da coluna
        self.treev.column('cod', width=20)
        self.treev.column('nome', width=150)
        self.treev.column('marca', width=100)
        self.treev.column('qtd', width=100)

        self.scroll = ttk.Scrollbar(self.fr_esquerdo, orient=VERTICAL, command=self.treev.yview)
        self.treev.grid(row=1, column=0, columnspan=1)
        self.scroll.grid(row=1, column=1, rowspan=1, sticky=NS)
        self.lbfr.grid(row=0, column=0)
        
        # treeview 2 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # definindo colunas
        self.colunas2 = ['cod', 'nome', 'marca', 'preco', 'precototal']
        self.tree2 = ttk.Treeview(self.fr_tree2, columns=self.colunas2, show='headings' )

        # definindo heading
        self.tree2.heading('cod', text='ID')
        self.tree2.heading('nome', text='Nome')
        self.tree2.heading('marca', text='Marca')
        self.tree2.heading('preco', text='preço')
        self.tree2.heading('precototal', text='Preço total')

        # definindo tamanho da coluna
        self.tree2.column('cod', width=20)
        self.tree2.column('nome', width=150)
        self.tree2.column('marca', width=100)
        self.tree2.column('preco', width=50)
        self.tree2.column('precototal', width=100)

        self.scroll2 = ttk.Scrollbar(self.fr_tree2, orient=VERTICAL, command=self.tree2.yview)
        self.tree2.grid(row=1, column=0, columnspan=1)
        self.scroll2.grid(row=1, column=1, rowspan=1, sticky=NS)

        

        self.frame.grid(row=0, column=0)
        # colocando frames 
        self.fr_esquerdo.pack(side=LEFT, fill=BOTH)
        self.fr_direita.pack(side=LEFT, fill=BOTH)
        self.fr_tree2.pack(side=RIGHT, fill=BOTH)
        
        self.etd_pesquisar.bind('<KeyRelease>', self.digitar_evento)
        self.treev.bind('<<TreeviewSelect>>', self.item_selected)
        self.mostrar_tree()
        
        # desativando entradas/entry 
        self.etds_disabled()
        

  
    def etds_normal(self):
        pass
            # self.etd_codigo.config(state=NORMAL)
            # self.etd_nome.config(state=NORMAL)
            # self.etd_marca.config(state=NORMAL)
            # self.etd_qtd.config(state=NORMAL)
            # self.etd_preco.config(state=NORMAL)
            # self.txt_descricao.config(state=NORMAL, background='white')
            
            
    def etds_disabled(self):
        pass
            # self.etd_codigo.config(state=DISABLED)
            # self.etd_nome.config(state=DISABLED)
            # self.etd_marca.config(state=DISABLED)
            # self.txt_descricao.config(state=DISABLED, background='lightgray')
            # self.etd_qtd.config(state=DISABLED)
            # self.etd_preco.config(state=DISABLED)
            
  
    def editar_dados(self) -> None:
        print(self.codigo)
        if self.codigo != '':

            # if str(self.etd_nome['state']) == NORMAL:
            codigo = self.codigo
            # nome =self.etd_nome.get()
            # marca =self.etd_marca.get()
            qtd =self.etd_qtd.get()
            preco =self.etd_preco.get()
            # txt = self.txt_descricao.get("1.0", END)
            
            # add dados =-=-=-=-=-=-=-=-=-=-=-=-=

            print('codigo:', codigo)
            # print('nome:', nome)
            # print('marca:', marca)
            print('qtd:', qtd)
            print('preco:', preco)
            # print('descricao:', txt)
            

            # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            

            self.deletar_tree()
            self.mostrar_tree()


    
    def deletar_dados(self):

        # self.etd_codigo.delete(0, END)
        # self.etd_nome.delete(0, END)
        # self.etd_marca.delete(0, END)
        # self.txt_descricao.delete('1.0', END)
        
        self.etd_qtd.delete(0, END)
        self.etd_preco.delete(0, END)
    
    def inserir_dados(self):
        # pegando dados
        dados = funcP.pesquisar(self.codigo)
        print(dados)
        dados = dados[0]

        # ativando entradas
        self.etds_normal()

        self.deletar_dados()
        
        self.lb_codigoInfo.config(text=dados[0])



        self.lb_nomeInfo.config(text= dados[1])
        self.lb_marcaInfo.config(text= dados[2])
        self.lb_descricaoInfo.config(text= dados[5])
        
        self.etd_qtd.insert(END, dados[3])
        self.etd_preco.insert(END, dados[4])

        self.etds_disabled()
        
    def item_selected(self, event):
        for selected_item in self.treev.selection():
            item = self.treev.item(selected_item)
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
        self.treev.delete(*self.treev.get_children()) 
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
                    self.treev.insert('', END, values=d)
        else:
            for d in dadosTree:
                self.treev.insert('', END, values=d)


if __name__ == '__main__':
    root = tk.Tk()
    frame = FrVenda(root)
    frame.pack()
    root.geometry('1200x800')
    root.mainloop()