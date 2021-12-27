from tkinter import ttk, Tk
from frames.fr_decimal import Fr_decimal
from frames.fr_binario import Fr_binario
from frames.fr_octal import Fr_octal
from frames.fr_hexadecimal import Fr_hexadecimal

class App(Tk):
    def __init__(self):
        super().__init__()
        style = ttk.Style(self)
        self.tk.call('source', './forest_ttk_theme/forest-dark.tcl')
        style.theme_use("forest-dark")

        self.lb_aviso = ttk.Label(text='')
        self.fr_decimal = Fr_decimal(self, self)
        self.fr_binario = Fr_binario(self, self)
        self.fr_octal = Fr_octal(self, self)
        self.fr_hexadecimal = Fr_hexadecimal(self, self)

        self.fr_decimal.grid(padx=6, pady=3)
        self.fr_binario.grid(padx=6, pady=3)
        self.fr_octal.grid(padx=6, pady=3)
        self.fr_hexadecimal.grid(padx=6, pady=3)

        
        self.lb_aviso.grid()

    def avisar(self, aviso=''):
        self.lb_aviso.config(text=aviso, foreground='red')
        
    def evento_decimal(self, num):
        try:
            self.avisar()
            self.fr_binario.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_hexadecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em decimal')

    def evento_binario(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_hexadecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em binario')
            
    def evento_octal(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_hexadecimal.inserir(num)
            self.fr_binario.inserir(num)
        except:
            self.avisar('erro de digitaçao em octal')
            
    def evento_hexadecimal(self, num):
        try:
            self.fr_decimal.inserir(num)
            self.fr_binario.inserir(num)
            self.fr_octal.inserir(num)
        except:
            self.avisar('erro de digitaçao em hexadecimal')
            
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()