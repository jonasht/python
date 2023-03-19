import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.constants import LEFT, RIGHT, Y
from frames.cnpj import Fr_CNPJ
from frames.cpf import Fr_cpf
from frames.cnh import Fr_CNH
from frames.cns import Fr_CNS
from frames.pis import Fr_PIS



class GeradorMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('690x400')
        self.title('Gerador de Documentos')

        # definindo thema =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.style = ttk.Style(self)
        self.tk.call('source', './forest-ttk-theme/forest-light.tcl')
        self.style.theme_use('forest-light')
        
        # lb tituo 
        self.lb_titulo = ttk.Label(self, text='Gerador de documentos\naperte q para sair')
        self.lb_titulo.configure(font='times 15 bold', foreground='dark gray')

        # definindo frames left right =-=-=-=-=-=-=-=-=-=-=-=-=
        self.fr_left = ttk.Frame(self)
        self.fr_right = ttk.Frame(self)
        
        self.fr_cpf = Fr_cpf(self)
        self.fr_cnpj = Fr_CNPJ(self)
        self.fr_cnh = Fr_CNH(self)
        
        self.fr_cns = Fr_CNS(self)
        self.fr_pis = Fr_PIS(self)
        

        self.fr_cpf.grid(row=0, column=0, padx=10)
        self.fr_cnpj.grid(row=1, column=0)
        self.fr_cnh.grid(row=2, column=0)
        self.fr_cns.grid(row=0, column=1)
        self.fr_pis.grid(row=1, column=1)
        self.lb_titulo.grid(row=2, column=1)
        
        self.bind('q', lambda x: self.destroy())
        

#? colocar esse jeito de main eh regra 
def main():
    root = GeradorMain()
    root.mainloop()
    
if __name__ == '__main__':
    main()

    
        
