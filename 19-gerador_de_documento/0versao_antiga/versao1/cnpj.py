from tkinter import ttk
from tkinter.constants import CENTER, END, EW
from validate_docbr import CNPJ

class Fr_cnpj(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


        self.cnpj = CNPJ()
        self.cnpj_num = ''


        #  cnpj ===================================================
        self.lbfr = ttk.Labelframe(self, text='CNPJ')
        self.etd_cnpj = ttk.Entry(self.lbfr)
        self.bt_cnpj = ttk.Button(self.lbfr, text='Gerar', command=self.gerar)
        self.chbt_cnpj = ttk.Checkbutton(self.lbfr, text='mask', command=self.chbt_Evento)

        self.etd_cnpj.grid(row=0, column=0, padx=2, pady=5)
        self.bt_cnpj.grid(row=0, column=1, padx=2, pady=5)
        self.chbt_cnpj.grid(row=0, column=2, padx=2, pady=5)

        
        self.lbfr.pack()

        # gerando =-=-
        self.gerar()
        


    def gerar(self):
        
        if 'selected' not in self.chbt_cnpj.state():
            self.etd_cnpj.delete(0, END)
            self.cnpj_num = self.cnpj.generate()
            self.etd_cnpj.insert(0, self.cnpj_num)
        else:
            self.chbt_Evento()



    def chbt_Evento(self):
        if 'selected' in self.chbt_cnpj.state():
            self.etd_cnpj.delete(0, END)
            self.etd_cnpj.insert(0, self.cnpj.mask(self.cnpj_num))
        else:
            self.etd_cnpj.delete(0, END)
            self.etd_cnpj.insert(0, self.cnpj_num)

    
