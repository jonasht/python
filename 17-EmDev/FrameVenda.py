
from tkinter import ttk
import tkinter as tk
from tkinter.constants import BOTH, DISABLED, END, EW, LEFT, N, NO, NORMAL, NS, RIGHT, VERTICAL

from colorama.ansi import Fore
import func_produtos as funcP
from frameVenda_treeProduto import Fr_treeProduto
from frameVenda_treeCliente import Fr_treeCliente
from frameVenda_lbCliente import Fr_lbCliente
from frameVenda_lbProduto import Fr_lbProduto
from frameVenda_treeVenda import Fr_treeVenda
from frameVenda_frFinalizacao import Fr_finalizacao



class FrVenda(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.dados_produto = ''
        self.dados_cliente = ''

        self.nt = ttk.Notebook(self)

        self.fr_treeProduto = Fr_treeProduto(self.nt, self)
        self.fr_treeCliente = Fr_treeCliente(self.nt, self)

        self.nt.add(self.fr_treeProduto, text='Produto')
        self.nt.add(self.fr_treeCliente, text='Cliente')

        # chamando frame cliente
        self.fr_lbCliente = Fr_lbCliente(self)
        
        # chamando frame produto
        self.fr_produtoInfo = ttk.Frame(self)
        self.fr_lbProduto = Fr_lbProduto(self.fr_produtoInfo)

        self.lb_qtd_prod = ttk.Label(self.fr_produtoInfo, text='quantidade:')
        self.etd_qtd_prod = ttk.Entry(self.fr_produtoInfo)
        self.lb_preco_prod = ttk.Label(self.fr_produtoInfo, text='R$')
        self.etd_preco_prod = ttk.Entry(self.fr_produtoInfo)
        self.bt_prod = ttk.Button(self.fr_produtoInfo, text='add >>> ')
        
        self.fr_lbProduto.grid(row=0, column=0, columnspan=2)
        self.lb_qtd_prod.grid(row=1, column=0)
        self.etd_qtd_prod.grid(row=1, column=1)
        self.lb_preco_prod.grid(row=2, column=0)
        self.etd_preco_prod.grid(row=2, column=1)
        self.bt_prod.grid(row=3, column=0, columnspan=2)

        # chamando a tree da venda 
        self.fr_treeVenda = Fr_treeVenda(self)
        
        self.fr_daFinalizacao = ttk.Frame(self)
        self.fr_finalizacao = Fr_finalizacao(self.fr_daFinalizacao)
        self.bt_finalizar = ttk.Button(self.fr_daFinalizacao, text='Finalizar')
        self.fr_finalizacao.grid(row=0, column=0)
        self.bt_finalizar.grid(row=1, column=0)

        
        # colocando as frames principais
        self.nt.grid(row=0, column=0)
        self.fr_produtoInfo.grid(row=0, column=1)
        self.fr_lbCliente.grid(row=1, column=0)
        self.fr_daFinalizacao.grid(row=1, column=1)
        self.fr_treeVenda.grid(row=0, column=2)
    def inserir_produto(self, dados):
        print('produto:', dados)
        self.fr_lbProduto.inserir_dados(dados)

    def inserir_cliente(self, dados):
        print('clientes:', dados)
        self.fr_lbCliente.inserir_dados(dados)
        self.dados_cliente = dados

  

if __name__ == '__main__':
    root = tk.Tk()
    frame = FrVenda(root)
    frame.pack()
    root.geometry('1200x800')
    root.mainloop()
