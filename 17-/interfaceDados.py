from tkinter import *
from registradorDB import Db


def ehNumero(n):
    try:
        int(n)
        return True
    except:
        return False
    
# botao return (key=enter)
def onReturn(evento):
    mostrar_info()



def limpar_Entradas():
    etd_id.delete(0, END)

def limpar_labels():
    lb_idMostrar.config(text='')
    lb_nome.config(text='')
    lb_idade.config(text='')

def mostrar_info():
    limpar_labels()

    db = Db()
    
    id = etd_id.get()
    db = db.get_db()
    
    limpar_Entradas()

    if id:
        print(f'entrou {id}')
        if ehNumero(id):
            try:
                lb_nome.config(text='Nome: '+db[id]['nome'].title())
                lb_idade.config(text='Idade: '+db[id]['idade'])
                lb_idMostrar.config(text='Id: ' + id)
                
                lb_aviso.config(text='')
            except:
                lb_aviso.config(text='Id não encontrado', fg='red')
        else:
            lb_aviso.config(text='Id precisa ser um numero', fg='red')
    else:
        lb_aviso.config(text='por favor, digite algum Id', fg='red')


root = Tk()
root.geometry('407x200+651+300')



# labels titulo, id
lb_titulo = Label(root, text='pesquisar por Id')

lb_id = Label(root, text='Id:', width=5)

# entrada id
etd_id = Entry(root)
etd_id.bind('<Return>', onReturn)

# botao pesquisar
bt_pesquisar = Button(root, text='pesquisar', command=mostrar_info)

# label aviso
lb_aviso = Label(root, text='')

# informacoes
lb_idMostrar = Label(root, text=' ')
lb_nome = Label(root, text=' ')
lb_idade = Label(root, text=' ')

lb_titulo.grid(row=0, column=1,columnspan=2, sticky='news')
lb_id.grid(row=1, column=0)
etd_id.grid(row=1, column=1)

bt_pesquisar.grid(row=1, column=2)

lb_aviso.grid(row=2, column=1)

lb_idMostrar.grid(row=3, column=1)
lb_nome.grid(row=4, column=1)
lb_idade.grid(row=5, column=1)


root.mainloop()

