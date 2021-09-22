from tkinter import *
from frameCadastroCliente import FrameCadastroCliente
from frameVenda import FrameVenda
from frameCadastroProduto import FrameProduto

class Principal(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry('1000x600')
        self.frameBotoes = Frame(self)
        
        # label frame venda =============================================================
        self.lbfr_venda = LabelFrame(self.frameBotoes, text='Venda')
        self.btVenda = Button(self.lbfr_venda, width=10, text='Venda')
        self.bt_entregas = Button(self.lbfr_venda, text='Entregas', width=10)
        self.btVenda.grid(row=0)
        self.bt_entregas.grid(row=1)
        self.lbfr_venda.grid(row=0)
        
        # label frame produto =============================================================
        self.lbfr_produto = LabelFrame(self.frameBotoes, text='Produto')
        self.bt_cadastrarProduto = Button(self.lbfr_produto, width=10, text='Cadastrar', command=self.show_fr_CadastrarProduto)
        self.bt_pesquisarProduto = Button(self.lbfr_produto, width=10, text='Pesquisar')

        self.bt_cadastrarProduto.grid(row=0)
        self.bt_pesquisarProduto.grid(row=1)
        self.lbfr_produto.grid(row=1)

        # label frame cliente =============================================================
        self.lbfr_cliente = LabelFrame(self.frameBotoes, text='Clientes')
        self.bt_cadastrarCliente = Button(self.lbfr_cliente, text='Cadastrar', width=10, command=self.show_fr_CadstroCliente)
        self.bt_pesquisarCliente = Button(self.lbfr_cliente, text='Pesquisar', width=10)

        self.bt_cadastrarCliente.grid(row=0)
        self.bt_pesquisarCliente.grid(row=1)
        self.lbfr_cliente.grid(row=2)
        
        self.btFaturamento = Button(self.frameBotoes,width=10, text='Faturamento')
        

        self.btFaturamento.grid(row=3)
        
        self.frameBotoes.pack(side=LEFT, fill=BOTH)
        

        # =================================================================
        self.frameDireita = Frame(self)
        self.frameCadastroProduto = FrameProduto(self.frameDireita)
        self.frameCadastroCliente = FrameCadastroCliente(self.frameDireita)

        self.frameDireita.pack(side=LEFT, fill=BOTH)
        
    def show_fr_CadastrarProduto(self):
        self.frameCadastroCliente.forget()
        
        self.frameCadastroProduto.pack()
        
    def show_fr_CadstroCliente(self):
        self.frameCadastroProduto.forget()
        
        self.frameCadastroCliente.pack()
        
        
        
root = Principal()
root.mainloop()