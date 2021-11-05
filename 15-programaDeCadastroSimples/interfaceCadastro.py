from tkinter import ttk
import tkinter as tk
from tkinter.constants import END, SOLID
from registradora import *


class FrameCadastro(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        
        # id
        self.lb_id = ttk.Label(self, text='Id:', width=10)
        self.lb_id_mostrar = ttk.Label(self, text=get_nextId())

        self.lb_nome = ttk.Label(self, text='Nome:', width=10)


        # nome
        self.etd_nome = ttk.Entry(self)
        self.etd_nome.bind('<Return>', self.onReturn)

        # sexo
        self.lb_sexo = ttk.Label(self, text='sexo:')
        self.etd_sexo = ttk.Entry(self)
        
        self.lb_sexo.grid(row=2, column=1, pady=2)
        self.etd_sexo.grid(row=2, column=2, pady=2)

        # idade
        self.lb_idade = ttk.Label(self, text='Idade:', width=10)
        self.etd_idade = ttk.Entry(self)
        self.etd_idade.bind('<Return>', self.onReturn)

        # label de aviso
        self.lb_aviso = ttk.Label(self, text='   ')

        # botao cadatrar, limpar, sair
        self.bt_cadastrar = ttk.Button(self, text='Cadastrar', command=self.cadastrar)
        self.bt_limpar = ttk.Button(self, text='Limpar', width=10, command=self.limpar_Entradas)
        

        # labels de confirmacao
        self.lb_id_confirmacao = ttk.Label(self, width=15)
        self.lb_nome_confirmacao = ttk.Label(self, width=15)
        self.lb_sexo_confirmacao = ttk.Label(self, width=15)
        self.lb_idade_confirmacao = ttk.Label(self, width=15)
        
        # --- posicoes ---------------

        # id:, id_mostrar, entradaNome, lb_idade, entrada_idade
        self.lb_id.grid(row=0, column=1, pady=2)
        self.lb_id_mostrar.grid(row=0, column=2, pady=2)

        self.lb_nome.grid(row=1, column=1, pady=2)
        self.etd_nome.grid(row=1, column=2, pady=2)

        self.lb_idade.grid(row=3, column=1, pady=2)
        self.etd_idade.grid(row=3, column=2, pady=2)

        # lb aviso
        self.lb_aviso.grid(row=4, column=1, columnspan=3, padx=2, pady=2, sticky='news')

        # botao cadastrar, limpar, sair
        self.bt_cadastrar.grid(row=5, column=2, columnspan=3, padx=2, pady=2, sticky='news')
        self.bt_limpar.grid(row=5, column=1, padx=2, pady=2)

        # confirmacoes
        self.lb_id_confirmacao.grid(row=0, column=3, padx=2, pady=2)
        self.lb_nome_confirmacao.grid(row=1, column=3, padx=2, pady=2)
        self.lb_sexo_confirmacao.grid(row=2, column=3, padx=2, pady=2)
        self.lb_idade_confirmacao.grid(row=3, column=3, padx=2, pady=2)
        

    def limpar_Entradas(self):
        self.etd_nome.delete(0, END)
        self.etd_sexo.delete(0, END)
        self.etd_idade.delete(0, END)



    # botao return (key=enter)
    def onReturn(self, evento):
        self.cadastrar()

    def cadastrar(self):
        nome = self.etd_nome.get()
        sexo = self.etd_sexo.get()
        idade = self.etd_idade.get()

        if not idade.isnumeric() and nome:
            self.lb_aviso.config(text='idade precisa ser numero', foreground='red')
            self.etd_idade.config(relief=SOLID, highlightbackground='red')

        elif nome and sexo and idade:
            get_id = get_nextId()
            
            cadastrar(nome=nome, sexo=sexo, idade=idade)
            mostrar_bd()
            
            dados = get_dados(get_id)
            nome = dados[1]
            sexo = dados[2]
            idade = dados[3]

            # mostrando a confirmacao na tela do que foi salvo
            self.lb_aviso.config(text='cadastro feito com sucesso', foreground='green')

            self.lb_id_confirmacao.config(text='Id: '+str(get_id), foreground='green')
            self.lb_nome_confirmacao.config(
                text='Nome: '+nome, foreground='green')
            self.lb_sexo_confirmacao.config(text='Sexo: '+sexo, foreground='green')
            self.lb_idade_confirmacao.config(
                text='Idade: '+str(idade), foreground='green')

            self.lb_id_mostrar.config(text=get_nextId())

            # limpar todas as entradas/entry
            self.limpar_Entradas()

        else:
            self.lb_aviso.config(text='preencha  todos  os pontos', foreground='red')

            
class Cadastro(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('cadastro')
        self.geometry('407x200+651+300')

        self.frame = FrameCadastro(self)
        self.frame.grid()
        
        

if __name__ == '__main__':
    cadastro = Cadastro()
    cadastro.mainloop()

