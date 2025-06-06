import tkinter as tk
from tkinter.constants import BOTH, END, RIGHT, LEFT

from tkinter.ttk import *
# import func_produtos as fp
import func.produtos as fp


class FrameProduto(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.lbfr = LabelFrame(self, text='Cadastro de Produto')
        self.frBaixo = Frame(self)

        self.bt_cadastrar = Button(self.frBaixo, text='Cadastrar', command=self.cadastrar)
        self.bt_resetar = Button(self.frBaixo, text='Resetar')
        self.bt_cadastrar.pack(side=RIGHT, fill=BOTH, expand=True, padx=1, pady=2)
        self.bt_resetar.pack(side=LEFT, fill=BOTH, expand=True, padx=1, pady=2)
        
        # frame cadastro =====================================
        self.frCadastro = Frame(self.lbfr)
        self.frDados = Frame(self.frCadastro)
        self.frDescricao = Frame(self.frCadastro)
        
        self.lb_nome = Label(self.frDados, text='Nome:')
        self.etd_nome = Entry(self.frDados)
        self.lb_marca = Label(self.frDados, text='Marca:')
        self.etd_marca = Entry(self.frDados)
        self.lb_qtd = Label(self.frDados, text='Quantidade:')
        self.etd_qtd = Entry(self.frDados)
        self.lb_preco = Label(self.frDados, text='Preco')
        self.etd_preco = Entry(self.frDados)

        # colocando dados 
        self.lb_nome.grid(row=0, column=0, padx=5, pady=2)
        self.etd_nome.grid(row=0, column=1, padx=5, pady=2)
        self.lb_marca.grid(row=1, column=0, padx=5, pady=2)
        self.etd_marca.grid(row=1, column=1, padx=5, pady=2)
        self.lb_qtd.grid(row=2, column=0, padx=5, pady=2)
        self.etd_qtd.grid(row= 2, column=1, padx=5, pady=2)
        self.lb_preco.grid(row= 3, column=0, padx=5, pady=2)
        self.etd_preco.grid(row=3 , column=1, padx=5, pady=2)
        
        # colocando frame dados
        self.frDados.grid()
        
        # frame descricao
        self.lb_descricao = Label(self.frDescricao, text='Descricao:')
        self.text_descricao = tk.Text(self.frDescricao, width=50, height=10)
        self.lb_descricao.grid(row= 5,column=2, padx=5, pady=2)
        self.text_descricao.grid(row=6 ,column=2, padx=10, pady=5)
        
        
        # colocando todos as fremes principais
        self.frDescricao.grid()

        self.frCadastro.pack()
        self.lbfr.pack()
        self.frBaixo.pack(fill=BOTH, expand=True)

        
        
        
        self.etd_nome.focus()
        
        # label aviso
        self.lb_aviso = Label(self, text=' ', foreground='red')
        self.lb_aviso.pack()
        
    def cadastrar(self):
    
        nome = self.etd_nome.get()
        marca = self.etd_marca.get()
        qtd = self.etd_qtd.get()

        preco = self.etd_preco.get()
        descricao = self.text_descricao.get('1.0', END)    
  
        if not(qtd): 
            qtd = '0'
  
        if not(preco):
            preco = 0
            
        if nome== '':
            self.lb_aviso.config(text='campo nome obrigatorio', foreground='red')
        elif qtd.isnumeric():
            qtd = int(qtd)
            preco = float(preco)
            

            # u.cadastrar_produto(nome=nome, preco=preco, quantidade=qtd, tamanho=tamanho, cor=cor)
            fp.add_(nome=nome, marca=marca, quantidade=qtd, preco=preco, descricao=descricao)
            
            self.lb_aviso.config(foreground='green', text='cadastro feito com sucesso')
            self.reset_campoCadastro()

        else:
            self.lb_avisoCadas.config(text='somente numeros em quantidade', foreground= 'red')
            
    
    def reset_campoCadastro(self):
        self.etd_nome.delete(0, END)
        self.etd_marca.delete(0, END)
        self.etd_qtd.delete(0, END)
        self.etd_preco.delete(0, END)
        self.text_descricao.delete('1.0', END)  
        self.etd_nome.focus()

if __name__ == '__main__':
    root = tk.Tk()
    frame = FrameProduto(root)
    frame.pack()
    root.geometry('700x500')
    root.mainloop()