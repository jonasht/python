import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, CENTER, DISABLED, EW, LEFT, RIGHT, TOP, W, Y
from frames.frameCadastroCliente import FrameCadastroCliente

from frames.frameCadastroProduto import FrameProduto
from frames.framePesquisarProduto import FrPesquisarProduto
from frames.FramePesquisarClientes import FrPesquisarCliente
from FrameVenda import FrVenda
from frames.frameHome import Fr_home
from frames.frameEntrega import Fr_entrega
from frames.frameFaturamento import Fr_faturamento


class Principal(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.frameBotoes = ttk.Frame(self)
        
        # theme =-=-====-=-====-=-====-=-====-=-====-=-====-=-====-=-
        # criando style
        self.style = ttk.Style(self)

        # chamando arquivo tcl 
        self.tk.call('source', './forest_ttk_theme/forest-light.tcl')
        

        # chamando o tema
        # self.style.theme_use('forest-light')e
        self.style.theme_use('forest-light')
        
        # botao HOME ======================================================================
        self.bt_home = ttk.Button(self.frameBotoes, text='HOME', width=15, command=self.show_fr_Home)
        self.bt_home.grid(row=0, column=0)
        
        
        # label frame venda =============================================================
        self.lbfr_venda = ttk.LabelFrame(self.frameBotoes, text='Venda')
        self.btVenda = ttk.Button(self.lbfr_venda, width=15, text='Venda', command=self.show_fr_venda)
        self.bt_entregas = ttk.Button(self.lbfr_venda, width=15,text='Entregas', command=self.show_fr_entrega)

        self.btVenda.grid(row=0, padx=10, pady=5)
        self.bt_entregas.grid(row=1, padx=10, pady=5)
        self.lbfr_venda.grid(row=1, padx=10, pady=5)
        
        # label frame produto =============================================================
        self.lbfr_produto = ttk.LabelFrame(self.frameBotoes, text='Produto')
        self.bt_cadastrarProduto = ttk.Button(self.lbfr_produto, width=15, text='Cadastrar', command=self.show_fr_CadastrarProduto)
        self.bt_pesquisarProduto = ttk.Button(self.lbfr_produto, width=15, text='Pesquisar', command=self.show_fr_pesquisarProduto)

        self.bt_cadastrarProduto.grid(row=0, padx=10, pady=5)
        self.bt_pesquisarProduto.grid(row=1, padx=10, pady=5)
        self.lbfr_produto.grid(row=2, padx=10, pady=5)

        # label frame cliente =============================================================
        self.lbfr_cliente = ttk.LabelFrame(self.frameBotoes, text='Clientes')
        self.bt_cadastrarCliente = ttk.Button(self.lbfr_cliente, text='Cadastrar', width=15, command=self.show_fr_CadstroCliente)
        self.bt_pesquisarCliente = ttk.Button(self.lbfr_cliente, text='Pesquisar', width=15, command=self.show_fr_pesquisarCliente)

        self.bt_cadastrarCliente.grid(row=0, padx=10, pady=5)
        self.bt_pesquisarCliente.grid(row=1, padx=10, pady=5)
        self.lbfr_cliente.grid(row=3, padx=10, pady=5)
        
        # faturamento ===-==-===-===-==-===-===-==-===-===-==-===-===-==-===-===-==-===-===-==-===
        self.bt_faturamento = ttk.Button(self.frameBotoes, width=15, text='Faturamento', command=self.show_fr_faturamento)
        

        self.bt_faturamento.grid(row=4, padx=10, pady=5)
        
        self.frameBotoes.pack(side=LEFT, fill=BOTH, padx=10, pady=2)
        

        # =================================================================
        self.frameDireita = ttk.Frame(self)
        self.frameCadastroProduto = FrameProduto(self.frameDireita)
        self.frameCadastroCliente = FrameCadastroCliente(self.frameDireita)
        self.framePesquisarProduto = FrPesquisarProduto(self.frameDireita)
        self.framePesquisarCliente = FrPesquisarCliente(self.frameDireita)
        self.frameVenda = FrVenda(self.frameDireita)
        self.frameHome = Fr_home(self.frameDireita)
        self.frameEntraga = Fr_entrega(self.frameDireita)
        self.frameFaturamento = Fr_faturamento(self.frameDireita)

        self.frameDireita.pack(side=TOP, fill=BOTH, anchor=CENTER)
        
        # mostrar frame home
        self.show_fr_Home()

        # desativando botoes em dev
        self.bt_faturamento.config(state=DISABLED)
        self.bt_entregas.config(state=DISABLED)
        

    def apagar_frames(self):
        self.frameCadastroCliente.forget()
        self.frameCadastroProduto.forget()
        self.framePesquisarProduto.forget()
        self.framePesquisarCliente.forget()
        self.frameVenda.forget()
        self.frameHome.forget()
        self.frameEntraga.forget()
        
        # removendo frame faturamento
        self.frameFaturamento.forget()
        self.frameFaturamento.lbfr.forget()
        
    def show_fr_faturamento(self):
        self.apagar_frames()
        self.frameFaturamento.pack()
        self.frameFaturamento.lbfr.pack()

    def show_fr_entrega(self):
        self.apagar_frames()
        self.frameEntraga.pack(side=TOP, fill=Y)
        
    def show_fr_Home(self):
        self.apagar_frames()
        self.frameHome.pack()

    def show_fr_venda(self):
        self.apagar_frames()
        self.frameVenda.pack(side=TOP, fill=Y)

    def show_fr_CadastrarProduto(self):
        self.apagar_frames()
        self.frameCadastroProduto.reset_campoCadastro()
        self.frameCadastroProduto.lb_aviso.config(text='')
        self.frameCadastroProduto.pack(side=TOP, fill=Y)
        
        
    def show_fr_CadstroCliente(self):
        self.apagar_frames()
        self.frameCadastroCliente.lb_aviso.config(text='')
        self.frameCadastroCliente.resetar()
        self.frameCadastroCliente.pack(side=TOP, fill=Y)

    def show_fr_pesquisarProduto(self):
        self.apagar_frames() 
        self.framePesquisarProduto.atualizar()
        self.framePesquisarProduto.pack(side=TOP, fill=Y)
        
    def show_fr_pesquisarCliente(self):
        self.apagar_frames()
        self.framePesquisarCliente.atualizar()
        self.framePesquisarCliente.pack(side=TOP, fill=Y)
        
        
        
def main():

    root = Principal()

    root.geometry('1280x1024')
    root.title('Sistema de Venda')
    root.mainloop()

if __name__ == '__main__':
    main()






