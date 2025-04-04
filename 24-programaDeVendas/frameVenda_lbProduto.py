from tkinter import Tk, Text, ttk
from tkinter.constants import ANCHOR, BOTTOM, END, LEFT, NW, RIGHT, SW, W


class Fr_lbProduto(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lbfr_produto = ttk.Labelframe(self, text='Info Produto')
        self.fr = ttk.Frame(self.lbfr_produto)
        self.fr1 = ttk.Frame(self.fr)
        self.fr2 = ttk.Frame(self.fr)
        self.fr_descricao = ttk.Frame(self.lbfr_produto)
        
        self.lb_id = ttk.Label(self.fr1, text='id:', width=10)
        self.lb_nome = ttk.Label(self.fr1, text='nome:', width=10)
        self.lb_marca = ttk.Label(self.fr1, text='marca:', width=10)
        self.lb_qtd = ttk.Label(self.fr1, text='Qtd:', width=10)
        self.lb_preco = ttk.Label(self.fr1, text='R$:', width=10)
        self.lb_descricao = ttk.Label(self.fr_descricao, text='descrição:', width=10)

        self.lb_id.grid(row=0, column=0)
        self.lb_nome.grid(row=1, column=0)
        self.lb_marca.grid(row=2, column=0)
        self.lb_qtd.grid(row=3, column=0)
        self.lb_preco.grid(row=4, column=0)
        self.lb_descricao.grid(row=0, column=0)

        self.lb_idInfo = ttk.Label(self.fr2, text='', width=25)
        self.lb_nomeInfo = ttk.Label(self.fr2, text='', width=25)
        self.lb_marcaInfo = ttk.Label(self.fr2, text='', width=25)
        self.lb_qtdInfo = ttk.Label(self.fr2, text='', width=25)
        self.lb_precoInfo = ttk.Label(self.fr2, text='', width=25)
        
        self.txt_discricao = Text(self.fr_descricao, width=35, height=6)
        
        self.lb_idInfo.grid(row=0, column=1)
        self.lb_nomeInfo.grid(row=1, column=1)
        self.lb_marcaInfo.grid(row=2, column=1)
        self.lb_qtdInfo.grid(row=3, column=1)
        self.lb_precoInfo.grid(row=4, column=1)
        self.txt_discricao.grid(row=1, column=0)
        
        self.fr1.pack(side=LEFT, anchor=NW)
        self.fr2.pack(side=LEFT, anchor=NW)
        self.fr.pack()
        self.fr_descricao.pack(side=BOTTOM)
        self.lbfr_produto.pack()

    def inserir_dados(self, dados):
        id = dados[0]
        nome = dados[1]
        marca = dados[2]
        qtd = dados[3]
        preco = dados[4]
        descricao = dados[5]
        
        # print('id:', id)
        # print('nome:', nome)
        # print('marca:', marca)
        # print('qtd:', qtd)
        # print('preco:', preco)
        # print('descricao:', descricao)

        self.lb_idInfo.config(text=id)
        self.lb_nomeInfo.config(text=nome)
        self.lb_marcaInfo.config(text=marca)
        self.lb_qtdInfo.config(text=qtd)
        self.lb_precoInfo.config(text=preco)
        # self.txt_discricao.config(text=descricao)
        self.txt_discricao.delete(1.0, END)
        self.txt_discricao.insert(1.0, descricao)
    def deletar_dados(self):
        self.lb_idInfo.config(text='')
        self.lb_nomeInfo.config(text='')
        self.lb_marcaInfo.config(text='')
        self.lb_qtdInfo.config(text='')
        self.lb_precoInfo.config(text='')
        # self.txt_discricao.config(text='')
        self.txt_discricao.delete(1.0, END)




if __name__ == '__main__':
    
    # print('so um teste')

    root = Tk()
    root.geometry('500x500')
    dados = (5, 'Iphone', 'Apple', 5254, 20000.0, 'um smartphone caro, que vem carregador\n\n\n\n')
    
    frame = Fr_lbProduto(root)
    frame.inserir_dados(dados)
    frame.pack()

    root.mainloop()




