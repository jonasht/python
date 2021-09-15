from tkinter import *
from frameProduto import FrameProduto
from frameVenda import FrameVenda


class Principal(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry('1000x600')
        self.frameBotoes = Frame(self)
        self.btVenda = Button(self.frameBotoes, width=10, text='Venda', command=self.show_frVenda)
        self.btProduto = Button(self.frameBotoes, width=10, text='Produto', command=self.show_frProduto)
        self.btFaturamento = Button(self.frameBotoes,width=10, text='Faturamento')
        self.btVenda.grid(row=0, sticky=N+W)
        self.btProduto.grid(row=1)
        self.btFaturamento.grid(row=2)
        
        self.frameBotoes.pack(side=LEFT, fill=BOTH)
        

        # =================================================================
        self.frameDireita = Frame(self)
        self.frProduto = FrameProduto(self.frameDireita)
        self.frVenda = FrameVenda(self.frameDireita)
        
        self.frameDireita.pack(side=LEFT, fill=BOTH)
        
    def show_frProduto(self):
        self.frVenda.pack_forget()
        self.frProduto.pack()
    def show_frVenda(self):
        self.frProduto.pack_forget()
        self.frVenda.pack()
        
        
        
        
root = Principal()
root.mainloop()