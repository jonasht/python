from tkinter import Tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from frames.fr_decimal import Fr_decimal
from frames.fr_binario import Fr_binario
from frames.fr_octal import Fr_octal
from frames.fr_hexadecimal import Fr_hexadecimal
from frames.fr_duodecimal import Fr_duodecimal


class App(Tk):
    def __init__(self):
        super().__init__()


        # chamando frames = 1-self eh parent, 2-self eh controller 
        self.lb_aviso = ttk.Label(text='')
        
        self.bt_apagarTudo = ttk.Button(self, text='Apagar tudo', bootstyle=OUTLINE, command=self.apagarTudo)
        self.fr_decimal = Fr_decimal(self, self)
        self.fr_binario = Fr_binario(self, self)
        self.fr_octal = Fr_octal(self, self)
        self.fr_hexadecimal = Fr_hexadecimal(self, self)
        self.fr_duodecimal = Fr_duodecimal(self, self)

        self.bt_apagarTudo.grid(padx=1, pady=1, sticky=EW)
        self.fr_decimal.grid(padx=6, pady=15)
        self.fr_binario.grid(padx=6, pady=15)
        self.fr_octal.grid(padx=6, pady=15)
        self.fr_duodecimal.grid(padx=6, pady=15)
        self.fr_hexadecimal.grid(padx=6, pady=15)
        
        self.lb_aviso.grid()


    
        
    def apagarTudo(self):
        self.fr_decimal.etd.delete(0, END)
        self.fr_binario.etd.delete(0, END)
        self.fr_octal.etd.delete(0, END)
        self.fr_duodecimal.etd.delete(0, END)
        self.fr_hexadecimal.etd.delete(0, END)




    def avisar(self, aviso=''):
        self.lb_aviso.configure(text=aviso, bootstyle=DANGER)
        
    def evento_decimal(self, num):
        self.fr_decimal.etd.configure(bootstyle=DANGER)
        
        try:
            self.avisar()
            self.fr_binario.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_hexadecimal.inserir(num)
            self.fr_duodecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em decimal')
            self.fr_decimal.etd.configure(bootstyle=DANGER)
        else:
            self.fr_decimal.etd.configure(bootstyle=PRIMARY)
            

    def evento_binario(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_hexadecimal.inserir(num)
            self.fr_duodecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em binario')
            self.fr_binario.etd.configure(bootstyle=DANGER)
        else:
            self.fr_binario.etd.configure(bootstyle=PRIMARY)
            
    def evento_octal(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_hexadecimal.inserir(num)
            self.fr_binario.inserir(num)
            self.fr_duodecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em octal')
            self.fr_octal.etd.configure(bootstyle=DANGER)
        else:
            self.fr_octal.etd.configure(bootstyle=PRIMARY)
            
    def evento_duodecimal(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_binario.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_hexadecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em duodecimal')
            self.fr_duodecimal.etd.configure(bootstyle=DANGER)
        else:
            self.fr_duodecimal.etd.configure(bootstyle=PRIMARY)
                  
    def evento_hexadecimal(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_binario.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_duodecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em hexadecimal')
            self.fr_hexadecimal.etd.configure(bootstyle=DANGER)
        else:
            self.fr_hexadecimal.etd.configure(bootstyle=PRIMARY)


def main():
    app = App()
    app.bind('q', lambda x: app.destroy())
    app.geometry('+550+200')
    app.mainloop()

if __name__ == '__main__':
    main()