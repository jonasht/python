
from tkinter import ttk
import tkinter as tk
from tkinter.constants import BOTH, DISABLED, END, EW, LEFT, N, NO, NORMAL, NS, RIGHT, VERTICAL

from colorama.ansi import Fore
import func_produtos as funcP
 



class FrPesquisarProduto(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # guardando id
        self.codigo = ''

        # definindo frames =-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
        self.lbfr_produto = ttk.LabelFrame(self, text='Produto')
        self.fr_baixo = ttk.Frame(self)

        self.fr_cima_p1 = ttk.Frame(self.lbfr_produto)
        self.fr_cima_p2 = ttk.Frame(self.lbfr_produto)


        self.lbfr = ttk.LabelFrame(self.fr_baixo, text='Pesquisar')
        
        self.lb_pesquisar = ttk.Label(self.lbfr, text='Nome:')
        self.lb_pesquisar.grid(row=0, column=0)
        
        self.etd_pesquisar = ttk.Entry(self.lbfr)
        self.etd_pesquisar.grid(row=0, column=1, sticky=EW)
        

        self.lb_codigo = ttk.Label(self.fr_cima_p1, text='Codigo:')
        self.lb_nome = ttk.Label(self.fr_cima_p1, text='Nome:')
        self.lb_marca = ttk.Label(self.fr_cima_p1, text='Marca:')
        self.lb_qtd = ttk.Label(self.fr_cima_p1, text='Quantidade:')
        self.lb_preco = ttk.Label(self.fr_cima_p1, text='Preço:')
        self.lb_descricao = ttk.Label(self.fr_cima_p2, text='Descriação:')
        
        
        
        self.lb_codigoInfo = ttk.Label(self.fr_cima_p1, text='', background='lightgray', width=20)

        # self.etd_codigo = ttk.Entry(self.fr_cima_p1, foreground='black')
        self.etd_nome = ttk.Entry(self.fr_cima_p1, foreground='black')
        self.etd_marca = ttk.Entry(self.fr_cima_p1, foreground='black')
        self.etd_qtd = ttk.Entry(self.fr_cima_p1, foreground='black')
        self.etd_preco = ttk.Entry(self.fr_cima_p1, foreground='black')
        
        self.txt_descricao = tk.Text(self.fr_cima_p2, width=50, height=10)
        
        self.bt_editar = ttk.Button(self.lbfr_produto, text='Editar', command=self.editar_dados)

        self.lb_codigo.grid(row=0, column=0)
        self.lb_nome.grid(row=1, column=0)
        self.lb_marca.grid(row=2, column=0)
        self.lb_qtd.grid(row=3, column=0)
        self.lb_preco.grid(row=4, column=0)
        self.lb_descricao.grid(row=0, column=2)

        self.lb_codigoInfo.grid(row=0, column=1, padx=5, pady=2)
        self.etd_nome.grid(row=1, column=1, padx=5, pady=2)
        self.etd_marca.grid(row=2, column=1, padx=5, pady=2)
        self.etd_qtd.grid(row=3, column=1, padx=5, pady=2)
        self.etd_preco.grid(row=4, column=1, padx=5, pady=2)
        self.txt_descricao.grid(row=1, column=2, padx=5, pady=2)

        
        # colocando botao editar
        self.bt_editar.grid(row=8, columnspan=2, sticky=EW, padx=5, pady=5)




        # Treeview =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # definindo colunas
        self.colunas = ['cod', 'nome', 'marca', 'qtd', 'preco']
        self.treev = ttk.Treeview(self.fr_baixo, columns=self.colunas, show='headings' )

        # definindo heading
        self.treev.heading('cod', text='ID')
        self.treev.heading('nome', text='Nome')
        self.treev.heading('marca', text='Marca')
        self.treev.heading('qtd', text='Quantidade')
        self.treev.heading('preco', text='R$')


        # definindo tamanho da coluna
        self.treev.column('cod', width=25)
        self.treev.column('nome', width=200)
        self.treev.column('marca', width=200)
        self.treev.column('qtd', width=95)
        self.treev.column('preco', width=95)

        self.scroll = ttk.Scrollbar(self.fr_baixo, orient=VERTICAL, command=self.treev.yview)
        self.treev.grid(row=1, column=0, columnspan=1)
        self.scroll.grid(row=1, column=1, sticky=NS, rowspan=1)
        #  
        self.lbfr.grid(row=0, column=0, sticky=EW)
        

        # colocando frames 
        
        self.lbfr_produto.pack()
        self.fr_cima_p1.grid(row=0,column=0)
        self.fr_cima_p2.grid(row=0,column=1)
        

        self.fr_baixo.pack()
        
        
        self.etd_pesquisar.bind('<KeyRelease>', self.digitar_evento)
        self.treev.bind('<<TreeviewSelect>>', self.item_selected)
        self.mostrar_tree()
        
        # desativando entradas/entry 
        self.etds_disabled()
        

    def atualizar(self): 
        # so um teste 
        self.deletar_tree()
        self.mostrar_tree()
    
    
    def etds_normal(self):
            # self.etd_codigo.config(state=NORMAL)
            self.etd_nome.config(state=NORMAL)
            self.etd_marca.config(state=NORMAL)
            self.etd_qtd.config(state=NORMAL)
            self.etd_preco.config(state=NORMAL)
            self.txt_descricao.config(state=NORMAL, background='white')
            
            
    def etds_disabled(self):

            # self.etd_codigo.config(state=DISABLED)
            self.etd_nome.config(state=DISABLED)
            self.etd_marca.config(state=DISABLED)
            self.etd_qtd.config(state=DISABLED)
            self.etd_preco.config(state=DISABLED)
            self.txt_descricao.config(state=DISABLED, background='lightgray')
            
            # mudar botao para editar
            self.bt_editar.config(text='Editar')
            
    def editar_dados(self):
        if self.codigo != '':

            if str(self.etd_nome['state']) == NORMAL:
                codigo = self.codigo
                nome =self.etd_nome.get()
                marca =self.etd_marca.get()
                qtd =self.etd_qtd.get()
                preco =self.etd_preco.get()
                txt = self.txt_descricao.get("1.0", END)
                
                # update dados =-=-=-=-=-=-=-=-=-=-=-=-=

                print('codigo:', codigo)
                print('nome:', nome)
                print('marca:', marca)
                print('qtd:', qtd)
                print('preco:', preco)
                print('descricao:', txt)
                
                funcP.update_(codigo=codigo, nome=nome,
                              marca=marca, quantidade=qtd,
                              preco=preco, descricao=txt)
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                
                self.etds_disabled()  
                self.bt_editar.config(text='Editar')

                self.deletar_tree()
                self.mostrar_tree()
            else:
                self.bt_editar.config(text='OK')
                self.etds_normal()

    
    def deletar_dados(self):

        # self.etd_codigo.delete(0, END)
        self.etd_nome.delete(0, END)
        self.etd_marca.delete(0, END)
        self.etd_qtd.delete(0, END)
        self.etd_preco.delete(0, END)
        self.txt_descricao.delete('1.0', END)
    
    def inserir_dados(self):
        # pegando dados
        dados = funcP.pesquisar(self.codigo)
        print(dados)
        dados = dados[0]

        # ativando entradas
        self.etds_normal()

        self.deletar_dados()
        
        self.lb_codigoInfo.config(text=dados[0])



        self.etd_nome.insert(END, dados[1])
        self.etd_marca.insert(END, dados[2])
        self.etd_qtd.insert(END, dados[3])
        self.etd_preco.insert(END, dados[4])
        self.txt_descricao.insert(END, dados[5])

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
            # dadosTree.append(d[:4])
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
    frame = FrPesquisarProduto(root)
    frame.pack()
    root.geometry('1000x500')
    root.mainloop()