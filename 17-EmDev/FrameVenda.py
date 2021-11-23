
from tkinter import ttk
import tkinter as tk
from tkinter.constants import BOTH, DISABLED, END, EW, LEFT, N, NO, NORMAL, NS, RIGHT, VERTICAL

from colorama.ansi import Fore
import func_produtos as funcP
from frameVenda_treeProduto import Fr_treeProduto
from frameVenda_treeCliente import Fr_treeCliente
from frameVenda_lbCliente import Fr_lbCliente

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
        self.nt.grid()

        # chamando frame cliente
        self.fr_lbCliente = Fr_lbCliente(self)
        self.fr_lbCliente.grid()
    
    def inserir_produto(self, dados):
        print('produto:', dados)

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
