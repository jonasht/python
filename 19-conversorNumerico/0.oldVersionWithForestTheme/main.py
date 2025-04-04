from tkinter import ttk, Tk, END, EW
from frames.fr_decimal import Fr_decimal
from frames.fr_binario import Fr_binario
from frames.fr_octal import Fr_octal
from frames.fr_hexadecimal import Fr_hexadecimal
from frames.fr_duodecimal import Fr_duodecimal


class App(Tk):
    def __init__(self):
        super().__init__()
        style = ttk.Style(self)
        self.tk.call('source', './forest_ttk_theme/forest-dark.tcl')
        style.theme_use("forest-dark")

        # chamando frames = 1-self eh parent, 2-self eh controller 
        self.lb_aviso = ttk.Label(text='')
        
        self.lb_apagarTudo = ttk.Button(self, text='Apagar tudo', command=self.apagarTudo)
        self.fr_decimal = Fr_decimal(self, self)
        self.fr_binario = Fr_binario(self, self)
        self.fr_octal = Fr_octal(self, self)
        self.fr_hexadecimal = Fr_hexadecimal(self, self)
        self.fr_duodecimal = Fr_duodecimal(self, self)

        self.lb_apagarTudo.grid(pady=6, padx=6, sticky=EW)
        self.fr_decimal.grid(padx=6, pady=3)
        self.fr_binario.grid(padx=6, pady=3)
        self.fr_octal.grid(padx=6, pady=3)
        self.fr_duodecimal.grid(padx=6, pady=3)
        self.fr_hexadecimal.grid(padx=6, pady=3)
        
        self.lb_aviso.grid()

        # aperte q para fechar a tela
        # self.bind('q', lambda event: self.destroy())
    
        
    def apagarTudo(self):
        self.fr_decimal.etd.delete(0, END)
        self.fr_binario.etd.delete(0, END)
        self.fr_octal.etd.delete(0, END)
        self.fr_duodecimal.etd.delete(0, END)
        self.fr_hexadecimal.etd.delete(0, END)




    def avisar(self, aviso=''):
        self.lb_aviso.config(text=aviso, foreground='red')
        
    def evento_decimal(self, num):
        try:
            self.avisar()
            self.fr_binario.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_hexadecimal.inserir(num)
            self.fr_duodecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em decimal')

    def evento_binario(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_hexadecimal.inserir(num)
            self.fr_duodecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em binario')
            
    def evento_octal(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_hexadecimal.inserir(num)
            self.fr_binario.inserir(num)
            self.fr_duodecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em octal')
            
    def evento_duodecimal(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_binario.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_hexadecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em duodecimal')
                  
    def evento_hexadecimal(self, num):
        try:
            self.avisar()
            self.fr_decimal.inserir(num)
            self.fr_binario.inserir(num)
            self.fr_octal.inserir(num)
            self.fr_duodecimal.inserir(num)
        except:
            self.avisar('erro de digitaçao em hexadecimal')
            
def main():
    app = App()
    # app.geometry('500x700')
    app.mainloop()

if __name__ == '__main__':
    main()