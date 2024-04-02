import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Window
from faker import Faker 

# imports labels frames 
from dataNasci import Lbfr_dataNasci
from lrEmail import Lbfr_email
from fone import Lbfr_fone
from nome import Lbfr_nome



class Fr_dados(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # faker
        self.faker = Faker('pt-br')

        self.lbfr_nome = Lbfr_nome(self, self.faker, self)
        self.lbfr_dataNasci = Lbfr_dataNasci(self, self.faker, self)
        self.nome = self.lbfr_nome.et.get()
        self.data = self.lbfr_dataNasci.et.get()

        self.lbfr_email = Lbfr_email(self, self.faker)

        self.lbfr_email.nome = self.nome
        self.lbfr_email.data = self.data
        self.lbfr_email.gerar()

        self.lbfr_fone = Lbfr_fone(self, self.faker)
        
        # grid labelframes 
        self.lbfr_nome.grid()
        self.lbfr_dataNasci.grid()
        self.lbfr_email.grid()
        self.lbfr_fone.grid()

    def gen_email(self):
        print('gen_email funcionando')
        self.nome = self.lbfr_nome.et.get()
        self.data = self.lbfr_dataNasci.et.get()
        self.lbfr_email.nome = self.nome
        self.lbfr_dataNasci = self.data
        self.lbfr_email.gerar()

def main():
    
    window = Window()

    fr = Fr_dados(window)
    fr.pack()
    window.style.theme_use('cyborg')
    window.place_window_center()
    window.mainloop()

if __name__ == '__main__':
    main()