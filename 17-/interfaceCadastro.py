from tkinter import *
from registradorDB import Db

class FrameCadastro(Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.db = Db()
        
        # id
        self.lb_id = Label(self, text='Id:', width=10)
        self.lb_id_mostrar = Label(self, text=self.db.get_nextId())

        self.lb_nome = Label(self, text='Nome:', width=10)


        # nome
        self.etd_nome = Entry(self)
        self.etd_nome.bind('<Return>', self.onReturn)

        # # sexo
        # lbsexo = Label(self, text='sexo:')
        # entdSexo = Entry(self)
        # lbsexo.grid(row=2, column=1, pady=2)
        # entdSexo.grid(row=2, column=2, pady=2)

        # idade
        self.lb_idade = Label(self, text='Idade:', width=10)
        self.etd_idade = Entry(self)
        self.etd_idade.bind('<Return>', self.onReturn)

        # label de aviso
        self.lb_aviso = Label(self, text='   ')

        # botao cadatrar, limpar, sair
        self.bt_cadastrar = Button(self, text='Cadastrar', command=self.cadastrar)
        self.bt_limpar = Button(self, text='Limpar', width=10, command=self.limpar_Entradas)
        

        # labels de confirmacao
        self.lb_id_confirmacao = Label(self, width=15)
        self.lb_nome_confirmacao = Label(self, width=15)
        self.lb_idade_confirmacao = Label(self, width=15)

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
        self.lb_idade_confirmacao.grid(row=3, column=3)

    def ehNumero(self, n):
        try:
            int(n)
            return True
        except:
            return False




    def limpar_Entradas(self):
        self.etd_nome.delete(0, END)
        self.etd_idade.delete(0, END)


    def proximoId(self):
        id = int(self.db.id)+1
        return id



    # botao return (key=enter)
    def onReturn(self, evento):
        self.cadastrar()

    def cadastrar(self):
        nome = self.etd_nome.get()
        idade = self.etd_idade.get()

        if not self.ehNumero(idade) and nome:
            self.lb_aviso.config(text='idade precisa ser numero', fg='red')
            self.etd_idade.config(relief=SOLID, highlightbackground='red')

        elif nome and idade:
            self.db.nome = nome
            self.db.idade = idade

            self.db.cadastrar()
            self.db.mostrar()
            print(self.db.get_db()[self.db.id])

            # mostrando a confirmacao na tela do que foi salvo
            self.lb_aviso.config(text='cadastro feito com sucesso', fg='green')

            self.lb_id_confirmacao.config(text='Id: '+self.db.id, fg='green')
            self.lb_nome_confirmacao.config(
                text='Nome: '+self.db.get_db()[self.db.id]['nome'], fg='green')
            self.lb_idade_confirmacao.config(
                text='Idade: '+self.db.get_db()[self.db.id]['idade'], fg='green')

            self.lb_id_mostrar.config(text=self.db.get_nextId())

            # limpar todas as entradas/entry
            self.limpar_Entradas()

        else:
            self.lb_aviso.config(text='preencha  todos  os pontos', fg='red')

            
class Cadastro(Tk):
    
    def __init__(self):
        super().__init__()
        self.title('cadastro')
        self.geometry('407x200+651+300')

        self.frame = FrameCadastro(self)
        self.frame.grid()
        
        

if __name__ == '__main__':
    cadastro = Cadastro()
    cadastro.mainloop()

