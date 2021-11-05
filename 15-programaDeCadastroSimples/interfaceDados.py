from tkinter import ttk
import tkinter as tk
from tkinter.constants import END
from registradora import *


class FrameDados(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        

        # labels titulo, id
        # self.lb_titulo = Label(self, text='pesquisar por Id')

        self.lb_id = ttk.Label(self, text='Id:', width=10)

        # entrada id
        self.etd_id = ttk.Entry(self)
        self.etd_id.bind('<Return>', self.onReturn)

        # botao pesquisar
        self.bt_pesquisar = ttk.Button(self, text='Pesquisar', width=10, command=self.mostrar_info)

        # label aviso
        self.lb_aviso = ttk.Label(self, text='')

        # informacoes
        self.lb_idMostrar = ttk.Label(self, text=' ')
        self.lb_nome = ttk.Label(self, text=' ')
        self.lb_idade = ttk.Label(self, text=' ')
        self.lb_sexo = ttk.Label(self, text=' ')

        # self.lb_titulo.grid(row=0, column=1,columnspan=2, sticky='news')
        self.lb_id.grid(row=1, column=0)
        self.etd_id.grid(row=1, column=1)

        self.bt_pesquisar.grid(row=1, column=2)

        self.lb_aviso.grid(row=2, column=1)

        self.lb_idMostrar.grid(row=3, column=1)
        self.lb_nome.grid(row=4, column=1)
        self.lb_idade.grid(row=5, column=1)
        self.lb_sexo.grid(row=6, column=1)
    

    # botao return (key=enter)
    def onReturn(self, evento):
        self.mostrar_info()



    def limpar_Entradas(self):
        self.etd_id.delete(0, END)

    def limpar_labels(self):
        self.lb_idMostrar.config(text='')
        self.lb_nome.config(text='')
        self.lb_idade.config(text='')
        self.lb_sexo.config(text='')

    def mostrar_info(self):
        self.limpar_labels()

    
        
        id = self.etd_id.get()
        db = get_dados(id)
        
        
        self.limpar_Entradas()

        if id:
            if id.isnumeric():
                try:
                    self.lb_nome.config(text='Nome: '+db[1].title())
                    self.lb_sexo.config(text='Sexo: '+db[2].title())
                    self.lb_idade.config(text='Idade: '+str(db[3]))
                    self.lb_idMostrar.config(text='Id: ' + id)
                    self.lb_aviso.config(text='')
                except:
                    self.lb_aviso.config(text='Id não encontrado', fg='red')
            else:
                self.lb_aviso.config(text='Id precisa ser um numero', fg='red')
        else:
            self.lb_aviso.config(text='por favor, digite algum Id', fg='red')

class Dados(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('407x200+651+300')
        self.title('Pesquisar')
        
        self.frame = FrameDados(self)
        self.frame.grid()

if __name__ == '__main__':
    root = Dados()
    root.mainloop()

