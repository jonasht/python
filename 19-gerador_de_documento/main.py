import tkinter as tk
from tkinter import ttk
from tkinter.constants import EW, LEFT, RIGHT, Y

from validate_docbr.CNH import CNH
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
        
        self.fr_cpf = Fr_cpf(self.fr_left)
        self.fr_cnpj = Fr_CNPJ(self.fr_left)
        self.fr_cnh = Fr_CNH(self.fr_left)
        
        self.fr_cns = Fr_CNS(self.fr_right)
        self.fr_pis = Fr_PIS(self.fr_right)
        

        self.fr_cpf.pack(fill=Y)
        self.fr_cnpj.pack(fill=Y)
        self.fr_cnh.pack(fill=Y)
        
        self.fr_cns.pack(fill=Y)
        self.fr_pis.pack(fill=Y)      
        
        # colocando frames
        self.fr_left.pack(side=LEFT, padx=20)
        self.fr_right.pack(side=RIGHT, padx=20) 
        
def main():
    GeradorMain().mainloop()
    
if __name__ == '__main__':
    main()

    
        
