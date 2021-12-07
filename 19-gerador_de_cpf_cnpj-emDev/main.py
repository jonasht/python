from tkinter import ttk
import tkinter as tk
from tkinter.constants import END
from validate_docbr import CPF, CNPJ

from cnpj import Fr_cnpj
from cpf import Fr_cpf

class GeradorMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x200')
        self.title('gerador de cpf/cnpj')
        
        fr_cpf = Fr_cpf(self)
        fr_cnpj = Fr_cnpj(self)
        fr_cpf.grid(row=0, column=0)
        fr_cnpj.grid(row=1, column=0)

def main():
    
    root = GeradorMain()
    
    root.mainloop()
    
if __name__ == '__main__':
    main()

    
        
