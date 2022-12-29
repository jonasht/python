            
from tkinter import font as tkfont  
from tkinter import ttk
import tkinter as tk
from frAcesso import FrAcesso
from frLogin import FrLogin
from frCadastro import FrCadastro
from uteis import init_db



class Principal(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry('450x450')
        

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        
        
        # definindo style
        style = ttk.Style(self)
        self.tk.call('source', './forest_ttk_theme/forest-light.tcl')
        style.theme_use("forest-light")


        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.fr_login = FrLogin(container, self)
        self.fr_acesso = FrAcesso(container, self)
        self.fr_cadastro = FrCadastro(container, self)

        self.fr_login.grid(row=0, column=0, sticky="nsew")
        self.fr_acesso.grid(row=0, column=0, sticky="nsew")
        self.fr_cadastro.grid(row=0, column=0, sticky="nsew")

        # mostrar primeira frame (login)
        self.show_login()
        

        
    def show_acesso(self, id):
        # mostrar frame acesso
        self.fr_acesso.tkraise()
        self.fr_acesso.display(id)
        
    def show_login(self):    
        # mostrar frame login
        self.fr_login.tkraise()
        
    def show_cadastro(self):
        # mostrar frame cadastro
        self.fr_cadastro.tkraise()


def main():
    root = Principal()
    root.mainloop()
        
if __name__ == "__main__":
    init_db()
    main()