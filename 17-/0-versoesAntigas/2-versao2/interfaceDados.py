from tkinter import *
from registradorDB import Db

class Dados(Tk):
    def __init__(self):
        super().__init__()
        
        self.geometry('407x200+651+300')
        self.title('Pesquisar')

        # labels titulo, id
        self.lb_titulo = Label(self, text='pesquisar por Id')

        self.lb_id = Label(self, text='Id:', width=5)

        # entrada id
        self.etd_id = Entry(self)
        self.etd_id.bind('<Return>', self.onReturn)

        # botao pesquisar
        self.bt_pesquisar = Button(self, text='pesquisar', command=self.mostrar_info)

        # label aviso
        self.lb_aviso = Label(self, text='')

        # informacoes
        self.lb_idMostrar = Label(self, text=' ')
        self.lb_nome = Label(self, text=' ')
        self.lb_idade = Label(self, text=' ')

        self.lb_titulo.grid(row=0, column=1,columnspan=2, sticky='news')
        self.lb_id.grid(row=1, column=0)
        self.etd_id.grid(row=1, column=1)

        self.bt_pesquisar.grid(row=1, column=2)

        self.lb_aviso.grid(row=2, column=1)

        self.lb_idMostrar.grid(row=3, column=1)
        self.lb_nome.grid(row=4, column=1)
        self.lb_idade.grid(row=5, column=1)
    
    def ehNumero(self, n):
        try:
            int(n)
            return True
        except:
            return False
    
    # botao return (key=enter)
    def onReturn(self, evento):
        self.mostrar_info()



    def limpar_Entradas(self):
        self.etd_id.delete(0, END)

    def limpar_labels(self):
        self.lb_idMostrar.config(text='')
        self.lb_nome.config(text='')
        self.lb_idade.config(text='')

    def mostrar_info(self):
        self.limpar_labels()

        db = Db()
        
        id = self.etd_id.get()
        db = db.get_db()
        
        self.limpar_Entradas()

        if id:
            if self.ehNumero(id):
                try:
                    self.lb_nome.config(text='Nome: '+db[id]['nome'].title())
                    self.lb_idade.config(text='Idade: '+db[id]['idade'])
                    self.lb_idMostrar.config(text='Id: ' + id)
                    self.lb_aviso.config(text='')
                except:
                    self.lb_aviso.config(text='Id não encontrado', fg='red')
            else:
                self.lb_aviso.config(text='Id precisa ser um numero', fg='red')
        else:
            self.lb_aviso.config(text='por favor, digite algum Id', fg='red')



if __name__ == '__main__':
    root = Dados()
    root.mainloop()

