import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import pyperclip as pc
import util


class Lbfr_email(ttk.Labelframe):
    def __init__(self, parent, faker):
        super().__init__(parent)
        self.faker = faker
        self.nome:str = ''
        self.data:str = ''

        #   email =================================================
        self.configure(text='Email', padding=20)
        self.et = ttk.Entry(self)
        self.bt_gerar = ttk.Button(self, text='Gerar', bootstyle=SUCCESS, command=self.gerar)
        self.bt_copy = ttk.Button(self, text='Copiar', bootstyle=INFO, command=self.copiar)

        self.et.grid(row=0, column=0, padx=2, pady=5, columnspan=2, sticky=EW)
        self.bt_copy.grid(row=1, column=0, padx=2, pady=5, sticky=EW)
        self.bt_gerar.grid(row=1, column=1, padx=2, pady=5, sticky=EW)
        
        
        # gerando =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # self.gerar()

        self.bind('<Enter>', self.enter_lbfr)
        self.bind('<Leave>', self.leave_lbfr)
        
    def get_et(self) -> str:
        return self.et.get()
    def enter_lbfr(self, event=None):
        self.config(bootstyle=SUCCESS)
        
    def leave_lbfr(self, event=None):
        self.config(bootstyle=NORMAL)


    def gerar(self):
        email = util.generate_email(self.nome, self.data)
        print('email:', email)
        self.et.delete(0, END)
        self.et.insert(0, email)
        

    def copiar(self):
        pc.copy(self.etd.get())




def main():
    from faker import Faker
    faker = Faker('pt-br')

    window = ttk.Window()
    window.place_window_center()
    nome='jorge teixeira'
    data = util.gen_date()
    fr = Fr_nome(window, faker, nome, data)

    fr.pack()
    fr.et.config(width=45)
    window.style.theme_use('cyborg')
    window.bind('q', lambda x: window.quit())
    window.mainloop()
if __name__ == '__main__':
    main()