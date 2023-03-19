import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from validate_docbr import CPF
import pyperclip as pc

class Fr_cpf(ttk.Labelframe):
    def __init__(self, parent):
        super().__init__(parent)

        self.cpf = CPF()
        self.cpf_num = ''
        self.var = ttk.BooleanVar()

        #   cpf =================================================
        self.configure(text='CPF', padding=20)
        self.etd = ttk.Entry(self)
        self.bt_gerar = ttk.Button(self, text='Gerar', command=self.gerar)
        self.chbt_mask = ttk.Checkbutton(self, text='mask',variable=self.var, command=self.chbt_Evento)
        self.bt_copy = ttk.Button(self, text='Copiar', command=self.copiar)
        self.etd.grid(row=0, column=0, padx=2, pady=5, columnspan=2, sticky=EW)
        self.bt_gerar.grid(row=1, column=1, padx=2, pady=5, sticky=EW)
        self.chbt_mask.grid(row=1, column=2, padx=2, pady=5)
        self.bt_copy.grid(row=1, column=0, padx=2, pady=5, sticky=EW)
        
        
        # gerando =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.gerar()

        
    def gerar(self):
        self.etd.delete(0, END)
        self.cpf_num = self.cpf.generate()
        self.etd.insert(0, self.cpf_num)
        if self.var.get():
            self.chbt_Evento()

    def copiar(self):
        pc.copy(self.etd.get())

    def chbt_Evento(self):
        if self.var.get():
            self.etd.delete(0, END)
            self.etd.insert(0, self.cpf.mask(self.cpf_num))
        else:
            self.etd.delete(0, END)
            self.etd.insert(0, self.cpf_num)

