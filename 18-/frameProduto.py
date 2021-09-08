from sqlite3.dbapi2 import Row
from tkinter import *
from typing import Collection
import uteis as u


class FrameProduto(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        lb_titulo = Label(self, text='Produtos').pack()

        self.frameCima = Frame(self)
        self.frameBaixo = Frame(self)
        self.bt_produtos = Button(self.frameCima, text='Produtos', width=15, command=self.show_frProdutos)
        self.bt_cadastro = Button(self.frameCima, text='Cadastrar', width=15, command= self.show_frCadastro)
        self.bt_produtos.pack(side=LEFT)
        self.bt_cadastro.pack(side=LEFT)

        
        self.frameCima.pack(side=TOP)
        self.frameBaixo.pack(side=BOTTOM)
        
        self.frameProdutos = Frame(self.frameBaixo)
        
        self.lb_pesquisarId = Label(self.frameProdutos, text='pesquisar ID nome:')
        self.etd_pesquisarId = Entry(self.frameProdutos)
        # self.lb_pesquisarNome = Label(self.frameProdutos, text='pesquisar Nome:')
        # self.etd_pesquisarNome = Entry(self.frameProdutos)    
        self.bt_pesquisar = Button(self.frameProdutos, text='pesquisar', command=self.pesquisar)
        self.lb_avisoProduto = Label(self.frameProdutos, text=' ')

        self.lb_pesquisarId.grid(row='1', column='0')
        self.etd_pesquisarId.grid(row='1', column='1')
        # self.lb_pesquisarNome.grid(row='2', column='0')
        # self.etd_pesquisarNome.grid(row='2', column='1')
        self.bt_pesquisar.grid(row=3, column=1)
        self.lb_avisoProduto.grid(row=4, column=1)
        
        # frame cadastro ===================================
        self.frameCadastro = Frame(self.frameBaixo)
        self.lb_nome = Label(self.frameCadastro, text='nome:')
        self.etd_nome = Entry(self.frameCadastro)
        self.lb_qtd = Label(self.frameCadastro, text='quantidade:')
        self.etd_qtd = Entry(self.frameCadastro)
        self.lb_tamanho = Label(self.frameCadastro, text='tamanho:')
        self.etd_tamanho = Entry(self.frameCadastro)
        self.lb_cor = Label(self.frameCadastro, text='cor:')
        self.etd_cor = Entry(self.frameCadastro)

        self.lb_nome.grid(row=1, column=0)
        self.etd_nome.grid(row=1, column=1)
        self.lb_qtd.grid(row=2, column=0)
        self.etd_qtd.grid(row=2, column=1)
        self.lb_tamanho.grid(row=3, column=0)
        self.etd_tamanho.grid(row=3, column=1)
        self.lb_cor.grid(row=4, column=0)
        self.etd_cor.grid(row=4, column=1)
        self.lb_avisoCadas = Label(self.frameCadastro, text=' ', fg='red')
        self.lb_avisoCadas.grid(row=5, column=1)

        self.bt_cadastrar = Button(self.frameCadastro, width=15, text='cadastrar', command=self.cadastrar)
        self.bt_cadastrar.grid(row=6, column=1)
        self.bt_resetar = Button(self.frameCadastro, width=15, text='resetar', command=self.reset_campoCadastro)
        self.bt_resetar.grid(row=6, column=0)

        # self.show_frProdutos()
        self.show_frCadastro()
        self.frameBaixo.pack()
    def pesquisar(self):
        opcao = self.etd_pesquisarId.get()
        dados = u.pesquisar(opcao=opcao)

        print(dados)
        
        
        for dado in dados:
            Label(None, text=f'nome:{dado[1]} quatidade:{dado[2]} tamanho:{dado[3]} cor:{dado[4]}').pack()
            
    def show_frProdutos(self):
        self.frameCadastro.forget()
        self.frameProdutos.pack()
        
    def show_frCadastro(self):
        self.frameProdutos.forget()
        self.frameCadastro.pack()
        
    def cadastrar(self):
        print('cadastrar')
        nome = self.etd_nome.get()
        qtd = self.etd_qtd.get()
        tamanho = self.etd_tamanho.get()
        cor = self.etd_cor.get()
        print(qtd)
        if not(qtd): 
            qtd = '0'
  
            
        if nome== '':
            self.lb_avisoCadas.config(text='campo nome obrigatorio', fg='red')
        elif qtd.isnumeric():
            qtd = int(qtd)
            print(nome, qtd, tamanho, cor)
            u.cadastrar_produto(nome=nome, quantidade=qtd, tamanho=tamanho, cor=cor)
            self.lb_avisoCadas.config(fg='green', text='cadastro feito com sucesso')
            self.reset_campoCadastro()

        else:
            self.lb_avisoCadas.config(text='somente numeros em quantidade', fg='red')
    def reset_campoCadastro(self):
        self.etd_nome.delete(0, END)
        self.etd_qtd.delete(0, END)
        self.etd_cor.delete(0, END)
        self.etd_tamanho.delete(0, END)

if __name__ == '__main__':
    root = Tk()
    frame = FrameProduto(root)
    frame.pack()
    root.geometry('500x500')
    root.mainloop()