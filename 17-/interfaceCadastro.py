from tkinter import *
from registradorDB import Db
db = Db()
root = Tk()
root.title('cadastro')
def proximoId():
    id = int(db.id)+1
    return id
# botao return (key=enter)
def onReturn(evento):
    cadastrar()

def cadastrar():
    nome = entdNome.get()
    idade = entdIdade.get()


    if nome and idade:
        db.nome = nome
        db.idade = idade

        db.cadastrar()
        db.mostrar()
        print(db.get_db()[db.id])
        lb_aviso.config(text='cadastro feito com sucesso', fg='green')
        
        lb_id_confirmacao.config(text='id: '+db.id)
        lb_nome_confirmacao.config(text='>>> '+db.get_db()[db.id]['nome'], fg='green')
        lb_idade_confirmacao.config(text='>>> '+db.get_db()[db.id]['idade'], fg='green')
        
        lb_id_mostrar.config(text=db.get_nextId())
    else:
        lb_aviso.config(text='preencha  todos  os pontos', fg='red')
        
    # apagar campo de entrada/entry
    entdNome.delete(0, END)
    entdIdade.delete(0, END)

    # mostrando a confirmacao na tela do que foi salvo
    
# root.geometry('200x150+400+300')
root.geometry('400x150+450+300')

# id
lb_id = Label(root, text='id:')
lb_id_mostrar = Label(root, text=db.get_nextId())
lb_id.grid(row=0, column=1, pady=2)
lb_id_mostrar.grid(row=0, column=2, pady=2)

lbnome = Label(root, text='nome:')
lbnome.grid(row=1, column=1, pady=2)


# nome
entdNome = Entry(root)
entdNome.bind('<Return>', cadastrar)
entdNome.grid(row=1, column=2, pady=2)

# # sexo
# lbsexo = Label(root, text='sexo:')
# entdSexo = Entry(root)
# lbsexo.grid(row=2, column=1, pady=2)
# entdSexo.grid(row=2, column=2, pady=2)

# idade
lbidade = Label(root, text='idade:')
entdIdade = Entry(root)
entdIdade.bind('<Return>', onReturn)
lbidade.grid(row=3, column=1, pady=2)
entdIdade.grid(row=3, column=2, pady=2)

# label de aviso
lb_aviso = Label(root, text='   ')
lb_aviso.grid(row=4, column=1, columnspan=3, padx=2, pady=2, sticky='news')

# botao cadatrar
btcadastrar = Button(root, text='cadastrar', command=cadastrar)
btcadastrar.grid(row=5, column=2, columnspan=3, padx=2, pady=2, sticky='news')

# botao sair
btsair = Button(root, text='sair', command=root.quit)
btsair.grid(row=5, column=1, pady=2, padx=2, sticky='news')

# labels de confirmacao
lb_id_confirmacao = Label(root, text='  ---   ')
lb_nome_confirmacao = Label(root, text='     ')
lb_idade_confirmacao = Label(root, text='     ')

lb_id_confirmacao.grid(row=0, column=3)
lb_nome_confirmacao.grid(row=1, column=3)
lb_idade_confirmacao.grid(row=3, column=3)



root.mainloop()