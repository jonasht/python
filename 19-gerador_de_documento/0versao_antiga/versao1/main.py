import tkinter as tk
from tkinter.constants import EW, Y
from cnpj import Fr_cnpj
from cpf import Fr_cpf
from fr_cnh import Fr_cnh

class GeradorMain(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x200')
        self.title('gerador de documentos')
        
        fr_cpf = Fr_cpf(self)
        fr_cnpj = Fr_cnpj(self)
        fr_cnh = Fr_cnh(self)

        
        fr_cpf.pack(fill=Y)
        fr_cnpj.pack(fill=Y)
        fr_cnh.pack(fill=Y)
        
def main():
    GeradorMain().mainloop()
    
if __name__ == '__main__':
    main()

    
        
