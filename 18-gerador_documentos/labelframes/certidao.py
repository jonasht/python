from validate_docbr import Certidao
import pyperclip as pc
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from ttkbootstrap import BooleanVar

class Fr_Certidao(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.Certidao = Certidao()
        self.Certidao_num = ''
        self.var = BooleanVar()

        #   Certidao =================================================
        self.configure(text='Certidão', padding=20)
   
        self.etd = ttk.Entry(self, width=50, justify=CENTER, font=('arial 12 bold'))
        self.bt_copy = ttk.Button(self, text='Copiar', bootstyle=INFO, command=self.copiar)
        self.bt_gerar = ttk.Button(self, text='Gerar',bootstyle=SUCCESS, command=self.gerar)
        self.chbt_mask = ttk.Checkbutton(self, text='Mascara', variable=self.var, command=self.chbt_Evento, bootstyle="success-round-toggle")
        
        self.etd.grid(row=0, column=0, padx=2, pady=5, columnspan=2, sticky=EW)

        self.bt_copy.grid(row=1, column=0, padx=2, pady=5, sticky=EW)
        self.bt_gerar.grid(row=1, column=1, padx=2, pady=5, sticky=EW)
        self.chbt_mask.grid(row=0, column=2, sticky=E, pady=5)


        # gerando =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.gerar()

        self.bind('<Enter>', self.enter_lbfr)
        self.bind('<Leave>', self.leave_lbfr)
        
    def enter_lbfr(self, event=None):
        self.config(bootstyle=SUCCESS)
        
    def leave_lbfr(self, event=None):
        self.config(bootstyle=NORMAL)
        
    def gerar(self):
        self.etd.delete(0, END)
        self.Certidao_num = self.Certidao.generate()
        self.etd.insert(0, self.Certidao_num)
        
        if self.var.get():
            self.chbt_Evento()

    def copiar(self):
        pc.copy(self.etd.get())

    def chbt_Evento(self):
        if self.var.get():
            self.etd.delete(0, END)
            self.etd.insert(0, self.Certidao.mask(self.Certidao_num))
        else:
            self.etd.delete(0, END)
            self.etd.insert(0, self.Certidao_num)

    def state(self, var):
        self.bt_copy.config(state=var)
        self.bt_gerar.config(state=var)
        self.chbt_mask.config(state=var)
        self.etd.config(state=var)
        
if __name__ == '__main__':
    app = ttk.Window()
    fr = Fr_Certidao(app)
    fr.pack()
  
    
    app.mainloop()