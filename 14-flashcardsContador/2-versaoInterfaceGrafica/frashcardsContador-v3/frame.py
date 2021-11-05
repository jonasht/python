from tkinter import ttk
import tkinter as tk
from tkinter.constants import LEFT, RIGHT


class Interface(ttk.Frame):
    def __init__ (self, parent):
        super().__init__(parent)
        self.frameRecomecar = ttk.Frame(self)
        self.frameComecar = ttk.Frame(self)
        self.frameTotal = ttk.Frame(self)
        

        self.lb1 = ttk.Label(self.frameRecomecar, text='Cartas para Recomeçar:', width=20, font='arial 16')
        self.lb_numero1 = ttk.Label(self.frameRecomecar, text='0', foreground='purple', font='arial 16 bold', width=2)

        self.lb2 = ttk.Label(self.frameComecar,   text='Cartas para   Começar:', width=20, font='arial 16')
        self.lb_numero2 = ttk.Label(self.frameComecar, text='0', foreground='blue', font='arial 16 bold', width=2)

        self.lb_falta = ttk.Label(self.frameTotal, text='Faltam:', width=8, font='arial 16')
        self.lb_faltaNum = ttk.Label(self.frameTotal, text='0', foreground='red', width=2, font='arial 16 bold')

        self.lb_total = ttk.Label(self.frameTotal, text='     Total:', width=9, font='arial 16')
        self.lb_totalNum = ttk.Label(self.frameTotal, text='0', foreground='blue', font='arial 16 bold')

        self.lb_lista1 = ttk.Label(self, text='', foreground='purple')
        self.lb_lista2 = ttk.Label(self, text='', foreground='blue')

        self.lb_falta.pack(side=LEFT)

        self.lb_faltaNum.pack(side=LEFT)
        self.lb_total.pack(side=LEFT)
        self.lb_totalNum.pack(side=RIGHT)

 
        
        self.lb1.pack(side=LEFT)
        self.lb_numero1.pack(side=RIGHT)

        self.lb2.pack(side=LEFT)
        self.lb_numero2.pack(side=RIGHT)

        self.frameRecomecar.pack()
        self.frameComecar.pack()
        self.frameTotal.pack()
        
        self.lb_lista1.pack()
        self.lb_lista2.pack()
        
    def atualizarTotal(self, n):
        self.lb_totalNum.config(text=n)
    
    def atualizarRecomecar(self, n):
        self.lb_numero1.config(text=n)  
        
    def atualizarComecar(self, n):
        self.lb_numero2.config(text=n)
    
    def atualizarRestanteDeCartas(self, n):
        if n > 0:
            self.lb_faltaNum.config(text=n, foreground='blue')         
        else:
            self.lb_faltaNum.config(text=n, foreground='red')
            
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x300')

    frame = Interface(root)
    frame.pack()
    root.mainloop()