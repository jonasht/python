from tkinter import *
import uteis as u


class FrameProduto(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        lb_titulo = Label(self, text='Cadastro de Produto').pack()
        self.frBaixo = Frame(self)

        self.bt_cadastrar = Button(self.frBaixo, text='Cadastrar')
        self.bt_resetar = Button(self.frBaixo, text='Resetar')
        self.bt_cadastrar.pack(side=RIGHT)
        self.bt_resetar.pack(side=LEFT)
        
        # frame cadastro =====================================
        self.frCadastro = Frame(self)
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
        self.lb_nome.grid(row=0,column=0)
        self.etd_nome.grid(row=0,column=1)
        self.lb_marca.grid(row=1,column=0)
        self.etd_marca.grid(row=1,column=1)
        self.lb_qtd.grid(row=2,column=0)
        self.etd_qtd.grid(row= 2,column=1)
        self.lb_preco.grid(row= 3,column=0)
        self.etd_preco.grid(row=3 ,column=1)
        
        # colocando frame dados
        self.frDados.grid()
        
        # frame descricao
        self.lb_descricao = Label(self.frDescricao, text='Descricao:')
        self.text_descricao = Text(self.frDescricao, width=50, height=10)
        self.lb_descricao.grid(row= 5,column=2)
        self.text_descricao.grid(row=6 ,column=2)
        
        
        # colocando todos as fremes principais
        self.frDescricao.grid()

        self.frCadastro.pack()
        self.frBaixo.pack()

        
        
        
        self.etd_nome.focus()
        
        # label aviso
        self.lb_aviso = Label(self, text='isso eh uma aviso', fg='red')
        self.lb_aviso.pack()
    def cadastrar(self):
        print('cadastrar')
        nome = self.etd_nome.get()
        preco = self.etd_preco.get()
        qtd = self.etd_qtd.get()
        tamanho = self.etd_tamanho.get()
        cor = self.etd_cor.get()
        
        print(qtd)
        if not(qtd): 
            qtd = '0'
  
        if not(preco):
            preco = 0
            
        if nome== '':
            self.lb_avisoCadas.config(text='campo nome obrigatorio', fg='red')
        elif qtd.isnumeric():
            qtd = int(qtd)
            preco = float(preco)
            
            print('preco', preco, 'tipo:', type(preco))
            print(nome, qtd, tamanho, cor)
            u.cadastrar_produto(nome=nome, preco=preco, quantidade=qtd, tamanho=tamanho, cor=cor)
            
            self.lb_avisoCadas.config(fg='green', text='cadastro feito com sucesso')
            self.reset_campoCadastro()

        else:
            self.lb_avisoCadas.config(text='somente numeros em quantidade', fg='red')
            
    
    def reset_campoCadastro(self):
        self.etd_nome.delete(0, END)
        self.etd_preco.delete(0, END)
        self.etd_qtd.delete(0, END)
        self.etd_cor.delete(0, END)
        self.etd_tamanho.delete(0, END)
        
        self.etd_nome.focus()

if __name__ == '__main__':
    root = Tk()
    frame = FrameProduto(root)
    frame.pack()
    root.geometry('700x500')
    root.mainloop()