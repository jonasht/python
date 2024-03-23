from validate_docbr import TituloEleitoral
import pyperclip as pc
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ttkbootstrap import BooleanVar

class Fr_TituloEleitoral(ttk.Labelframe):
    def __init__(self, parent):
        super().__init__(parent)

        self.TituloEleitoral = TituloEleitoral()
        self.TituloEleitoral_num = ''
        self.var = BooleanVar()

        #   TituloEleitoral =================================================
        self.configure(text='Titulo Eleitoral', padding=20)
        self.etd = ttk.Entry(self)
        self.bt_gerar = ttk.Button(self, text='Gerar', bootstyle=SUCCESS, command=self.gerar)
        self.chbt_mask = ttk.Checkbutton(self, text='mask', variable=self.var, bootstyle="success-round-toggle", command=self.chbt_Evento)
        self.bt_copy = ttk.Button(self, text='Copiar', bootstyle=INFO, command=self.copiar)
        
        self.etd.grid(row=0, column=0, padx=2, pady=5, columnspan=2, sticky=EW)
        self.bt_gerar.grid(row=1, column=1, padx=2, pady=5, sticky=EW)
        self.bt_copy.grid(row=1, column=0, padx=2, pady=5, sticky=EW)
        self.chbt_mask.grid(row=1, column=2, padx=2, pady=5)
        
        
        # gerando =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.gerar()

        # desativando checkbox
        # self.chbt_mask.state(['!alternate'])
        self.bind('<Enter>', self.enter_lbfr)
        self.bind('<Leave>', self.leave_lbfr)
        
    def enter_lbfr(self, event=None):
        self.config(bootstyle=SUCCESS)
        
    def leave_lbfr(self, event=None):
        self.config(bootstyle=NORMAL)
    def gerar(self):
        self.etd.delete(0, END)
        self.TituloEleitoral_num = self.TituloEleitoral.generate()
        self.etd.insert(0, self.TituloEleitoral_num)
        
        if self.var.get():
            self.chbt_Evento()

    def copiar(self):
        pc.copy(self.etd.get())

    def chbt_Evento(self):
        
        if self.var.get():
            self.etd.delete(0, END)
            self.etd.insert(0, self.TituloEleitoral.mask(self.TituloEleitoral_num))
        else:
            self.etd.delete(0, END)
            self.etd.insert(0, self.TituloEleitoral_num)
    def state(self, var):
        self.bt_copy.config(state=var)
        self.bt_gerar.config(state=var)
        self.chbt_mask.config(state=var)
        self.etd.config(state=var)

if __name__ == '__main__':
    app = ttk.Window()
    Fr_TituloEleitoral(app).pack()
    app.mainloop()