from tkinter import ttk
from tkinter import *
from validate_docbr import CNPJ
import pyperclip as pc

class Fr_CNPJ(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.CNPJ = CNPJ()
        self.CNPJ_num = ''


        #   CNPJ =================================================
        self.lbfr = ttk.Labelframe(self, text='CNPJ', border=10)
        self.etd = ttk.Entry(self.lbfr)
        self.bt_gerar = ttk.Button(self.lbfr, text='Gerar', command=self.gerar)
        self.chbt_mask = ttk.Checkbutton(self.lbfr, text='mask', command=self.chbt_Evento)
        self.bt_copy = ttk.Button(self.lbfr, text='Copiar', command=self.copiar)
        self.etd.grid(row=0, column=0, padx=2, pady=5, columnspan=2, sticky=EW)
        self.bt_gerar.grid(row=1, column=1, padx=2, pady=5)
        self.chbt_mask.grid(row=1, column=2, padx=2, pady=5)
        self.bt_copy.grid(row=1, column=0, padx=2, pady=5)
        
        self.lbfr.pack()
        
        # gerando =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.gerar()

        # desativando checkbox
        self.chbt_mask.state(['!alternate'])
        
    def gerar(self):
        self.etd.delete(0, END)
        self.CNPJ_num = self.CNPJ.generate()
        self.etd.insert(0, self.CNPJ_num)
        if 'selected' in self.chbt_mask.state():
            self.chbt_Evento()

    def copiar(self):
        pc.copy(self.etd.get())

    def chbt_Evento(self):
        if 'selected' in self.chbt_mask.state():
            self.etd.delete(0, END)
            self.etd.insert(0, self.CNPJ.mask(self.CNPJ_num))
        else:
            self.etd.delete(0, END)
            self.etd.insert(0, self.CNPJ_num)

if __name__ == '__main__':
    from tkinter import *
    app = Tk()
    Fr_CNPJ(app).pack()

    app.mainloop()