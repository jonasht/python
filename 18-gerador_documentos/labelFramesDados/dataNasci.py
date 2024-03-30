import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import pyperclip as pc



class Fr_dataNasci(ttk.Labelframe):
    def __init__(self, parent, faker):
        super().__init__(parent)
        self.faker = faker

        #   dataNasci =================================================
        self.configure(text='DataDeNascimento', padding=20)
        self.et = ttk.Entry(self)
        self.bt_gerar = ttk.Button(self, text='Gerar', bootstyle=SUCCESS, command=self.gerar)
        self.bt_copy = ttk.Button(self, text='Copiar', bootstyle=INFO, command=self.copiar)

        self.et.grid(row=0, column=0, padx=2, pady=5, columnspan=2, sticky=EW)
        self.bt_copy.grid(row=1, column=0, padx=2, pady=5, sticky=EW)
        self.bt_gerar.grid(row=1, column=1, padx=2, pady=5, sticky=EW)
        
        
        # gerando =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.gerar()
        self.bind('<Enter>', self.enter_lbfr)
        self.bind('<Leave>', self.leave_lbfr)
        

    def enter_lbfr(self, event=None):
        self.config(bootstyle=SUCCESS)
        
    def leave_lbfr(self, event=None):
        self.config(bootstyle=NORMAL)
        
    def gerar(self):
        self.et.delete(0, END)
        data = self.faker.date_of_birth(minimum_age=18, maximum_age=70, ).strftime("%d/%m/%Y")

        self.et.insert(0, data)
        

    def copiar(self):
        pc.copy(self.etd.get())



if __name__ == '__main__':
    from faker import Faker
    faker = Faker('pt-br')

    window = ttk.Window()
    window.place_window_center()
    fr = Fr_dataNasci(window, faker)
    fr.pack()
    fr.et.config(width=25)
    window.style.theme_use('cyborg')
    window.bind('q', lambda x: window.quit())
    window.mainloop()