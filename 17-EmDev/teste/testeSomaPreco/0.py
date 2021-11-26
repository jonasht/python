import tkinter as tk
from tkinter import ttk
from tkinter.constants import END


class Fr(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.valor = 9

        ttk.Label(self, text='rtee').pack()

        self.lb_valor = ttk.Label(self, text=self.valor)
        self.etd = ttk.Entry(self)
        self.lb_valor.pack()
        self.etd.pack()
        self.etd.insert(0, 1)
        
        self.etd.bind('<KeyRelease>', self.evento_somar)
    
    def evento_somar(self, event):
        # serve para somar a entrada do valor quando colocado (tempo real)
        valor_etd = self.etd.get()
        if not valor_etd:
            print('nenhum valor')
            self.lb_valor.config(text=self.valor)

            
        elif valor_etd.isnumeric():
            print(valor_etd, 'tipo:', type(valor_etd))
            valor_etd = int(valor_etd)
            self.lb_valor.config(text=valor_etd*self.valor)

        else:
            # digete apenas numeros
            print('por favor digite apenas numeros')
        
def main():
    root = tk.Tk()
    frame = Fr(root)
    frame.pack()

    root.geometry('500x500')
    root.mainloop()


if __name__ == '__main__':
    main()
