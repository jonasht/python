from tkinter import *
from registradorDB import Db



def mostrar_info():
    db = Db()
    id = etd_id.get()
    db = db.get_db()

    lb_nome.config(text=db[id]['nome'])
    lb_idade.config(text=db[id]['idade'])



root = Tk()


lb_id = Label(root, text='id:')
etd_id = Entry(root)
bt_pesquisar = Button(root, text='pesquisar', command=mostrar_info)
lb_id.pack()
etd_id.pack()
bt_pesquisar.pack()


# informacoes
lb_nome = Label(root, text=' ')
lb_idade = Label(root, text=' ')
lb_nome.pack()
lb_idade.pack()
root.mainloop()

