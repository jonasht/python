from tkinter import ttk
import tkinter as tk
from tkinter.constants import END
from validate_docbr import CPF, CNPJ



class Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.cpf = CPF()
        self.cnpj = CNPJ()
        self.cpf_num = ''
        self.cnpj_num = ''

        #   cpf =================================================
        self.lbfr_cpf = ttk.Labelframe(self, text='gerar CPF')
        self.etd_cpf = ttk.Entry(self.lbfr_cpf)
        self.bt_cpf = ttk.Button(self.lbfr_cpf, text='Gerar', command=self.gerar_cpf)
        self.chbt_cpf = ttk.Checkbutton(self.lbfr_cpf, text='mark', command=self.chbt_cpfEvento)

        self.etd_cpf.grid(row=0, column=0, padx=2, pady=5)
        self.bt_cpf.grid(row=0, column=1, padx=2, pady=5)
        self.chbt_cpf.grid(row=0, column=2, padx=2, pady=5)
        
        #  cnpj ===================================================
        self.lbfr_cnpj = ttk.Labelframe(self, text='gerar CNPJ')
        self.etd_cnpj = ttk.Entry(self.lbfr_cnpj)
        self.bt_cnpj = ttk.Button(self.lbfr_cnpj, text='Gerar', command=self.gerar_cnpj)
        self.chbt_cnpj = ttk.Checkbutton(self.lbfr_cnpj, text='mask', command=self.chbt_cnpjEvento)

        self.etd_cnpj.grid(row=0, column=0, padx=2, pady=5)
        self.bt_cnpj.grid(row=0, column=1, padx=2, pady=5)
        self.chbt_cnpj.grid(row=0, column=2, padx=2, pady=5)

        
        self.lbfr_cpf.grid(row=0, pady=10)
        self.lbfr_cnpj.grid(row=1, pady=   10)

        # gerando =-=-
        self.gerar_cpf()
        self.gerar_cnpj()
        
        self.chbt_cpf.selection_clear()

    def gerar_cpf(self):
        self.etd_cpf.delete(0, END)
        self.cpf_num = self.cpf.generate()
        self.etd_cpf.insert(0, self.cpf_num)
        if 'selected' in self.chbt_cpf.state():
            self.chbt_cpfEvento()

    def gerar_cnpj(self):
        self.etd_cnpj.delete(0, END)
        self.cnpj_num = self.cnpj.generate()
        self.etd_cnpj.insert(0, self.cnpj_num)
        if 'selected' in self.chbt_cnpj.state():
            self.chbt_cnpjEvento()

    def chbt_cpfEvento(self):
        if 'selected' in self.chbt_cpf.state():
            self.etd_cpf.delete(0, END)
            self.etd_cpf.insert(0, self.cpf.mask(self.cpf_num))
        else:
            self.etd_cpf.delete(0, END)
            self.etd_cpf.insert(0, self.cpf_num)

    def chbt_cnpjEvento(self):
        if 'selected' in self.chbt_cnpj.state():
            self.etd_cnpj.delete(0, END)
            self.etd_cnpj.insert(0, self.cnpj.mask(self.cnpj_num))
        else:
            self.etd_cnpj.delete(0, END)
            self.etd_cnpj.insert(0, self.cnpj_num)

    

def main():
    
    root = tk.Tk()
    root.geometry('500x200')
    root.title('gerador de cpf/cnpj')

    frame = Frame(root)
    
    frame.pack()
    root.mainloop()
    
if __name__ == '__main__':
    main()

    
        
