from tkinter import *
from registradorDB import Db


def ehNumero(n):
    try:
        int(n)
        return True
    except:
        return False


db = Db()
root = Tk()
root.title('cadastro')
root.geometry('407x200+450+300')


def limpar_Entradas():
    etd_nome.delete(0, END)
    etd_idade.delete(0, END)


def proximoId():
    id = int(db.id)+1
    return id
# botao return (key=enter)


def onReturn(evento):
    cadastrar()


def cadastrar():
    nome = etd_nome.get()
    idade = etd_idade.get()

    if not ehNumero(idade) and nome:
        lb_aviso.config(text='idade precisa ser numero', fg='red')
        etd_idade.config(relief=SOLID, highlightbackground='red')

    elif nome and idade:
        db.nome = nome
        db.idade = idade

        db.cadastrar()
        db.mostrar()
        print(db.get_db()[db.id])

        # mostrando a confirmacao na tela do que foi salvo
        lb_aviso.config(text='cadastro feito com sucesso', fg='green')

        lb_id_confirmacao.config(text='Id: '+db.id, fg='green')
        lb_nome_confirmacao.config(
            text='Nome: '+db.get_db()[db.id]['nome'], fg='green')
        lb_idade_confirmacao.config(
            text='Idade: '+db.get_db()[db.id]['idade'], fg='green')

        lb_id_mostrar.config(text=db.get_nextId())

        # limpar todas as entradas/entry
        limpar_Entradas()

    else:
        lb_aviso.config(text='preencha  todos  os pontos', fg='red')


# id
lb_id = Label(root, text='Id:', width=10)
lb_id_mostrar = Label(root, text=db.get_nextId())

lb_nome = Label(root, text='Nome:', width=10)


# nome
etd_nome = Entry(root)
etd_nome.bind('<Return>', onReturn)

# # sexo
# lbsexo = Label(root, text='sexo:')
# entdSexo = Entry(root)
# lbsexo.grid(row=2, column=1, pady=2)
# entdSexo.grid(row=2, column=2, pady=2)

# idade
lb_idade = Label(root, text='Idade:', width=10)
etd_idade = Entry(root)
etd_idade.bind('<Return>', onReturn)

# label de aviso
lb_aviso = Label(root, text='   ')

# botao cadatrar, limpar, sair
bt_cadastrar = Button(root, text='Cadastrar', command=cadastrar)
bt_limpar = Button(root, text='Limpar', width=10, command=limpar_Entradas)
bt_sair = Button(root, text='Sair', command=root.quit)

# labels de confirmacao
lb_id_confirmacao = Label(root, width=15)
lb_nome_confirmacao = Label(root, width=15)
lb_idade_confirmacao = Label(root, width=15)

# --- posicoes ---------------

# id:, id_mostrar, entradaNome, lb_idade, entrada_idade
lb_id.grid(row=0, column=1, pady=2)
lb_id_mostrar.grid(row=0, column=2, pady=2)

lb_nome.grid(row=1, column=1, pady=2)
etd_nome.grid(row=1, column=2, pady=2)

lb_idade.grid(row=3, column=1, pady=2)
etd_idade.grid(row=3, column=2, pady=2)

# lb aviso
lb_aviso.grid(row=4, column=1, columnspan=3, padx=2, pady=2, sticky='news')

# botao cadastrar, limpar, sair
bt_cadastrar.grid(row=5, column=2, columnspan=3, padx=2, pady=2, sticky='news')
bt_limpar.grid(row=5, column=1, padx=2, pady=2)
bt_sair.grid(row=6, column=1, columnspan=3, pady=2, padx=2, sticky='news')

# confirmacoes
lb_id_confirmacao.grid(row=0, column=3, padx=2, pady=2)
lb_nome_confirmacao.grid(row=1, column=3, padx=2, pady=2)
lb_idade_confirmacao.grid(row=3, column=3)


root.mainloop()
