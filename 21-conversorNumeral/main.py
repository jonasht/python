from tkinter import ttk, Tk
from frames.fr_decimal import Fr_decimal
from frames.fr_binario import Fr_binario
from frames.fr_octal import Fr_octal
from frames.fr_hexadecimal import Fr_hexadecimal

class App(Tk):
    def __init__(self):
        super().__init__()
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

    def avisar(self, aviso):
        self.lb_aviso.config(text=aviso, foreground='red')
        
    def evento_decimal(self, num):
        self.fr_binario.inserir(num)
        self.fr_octal.inserir(num)
        self.fr_hexadecimal.inserir(num)
    
    def evento_binario(self, num):
        self.fr_decimal.inserir(num)
        self.fr_octal.inserir(num)
        self.fr_hexadecimal.inserir(num)
        
    def evento_octal(self, num):
        self.fr_decimal.inserir(num)
        self.fr_hexadecimal.inserir(num)
        self.fr_binario.inserir(num)
    
    def evento_hexadecimal(self, num):
        self.fr_decimal.inserir(num)
        self.fr_binario.inserir(num)
        self.fr_octal.inserir(num)
        
def main():
    app = App()
    app.mainloop()

main()