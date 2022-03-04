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
        self.geometry('670x400')
        self.title('gerador de documentos')

        # definindo thema =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.style = ttk.Style(self)
        self.tk.call('source', './forest-ttk-theme/forest-light.tcl')
        self.style.theme_use('forest-light')

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
        

#? colocar esse jeito de main eh regra 
def main():
    GeradorMain().mainloop()
    
if __name__ == '__main__':
    main()

    
        
