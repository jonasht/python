from tkinter import Tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import pyperclip as pc 

from frames.uteis import to_dec

class Fr_hexadecimal(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        
        self.lbfr = ttk.LabelFrame(self, text='hexadecimal')
        self.bt_copiar = ttk.Button(self.lbfr, text='Copiar', command=self.copiar)
        self.etd = ttk.Entry(self.lbfr, width=80)
        self.bt_colar = ttk.Button(self.lbfr, text='Colar', command=self.colar)

        self.etd.grid(row=0, column=0, columnspan=2, padx=6, pady=3)
        self.bt_copiar.grid(row=1, column=0, sticky=EW, padx=6, pady=3)
        self.bt_colar.grid(row=1, column=1, sticky=EW, padx=6, pady=3)

        self.lbfr.grid()
        self.etd.bind('<KeyRelease>', self.evento)

    def evento(self, event):
        numero = self.etd.get()
        
        numero = '0x'+numero if numero else ''
        self.con.evento_hexadecimal(numero)
        
    def inserir(self, num):
        if num:
            num = to_dec(num)
            num = int(num)
            num = f'{num:x}'
            self.etd.delete(0, END)
            self.etd.insert(END, num)
        else:
            self.etd.delete(0, END)
            
    def copiar(self):
        pc.copy(self.etd.get())
    
    def colar(self):
        self.etd.delete(0, END)
        self.etd.insert(END, pc.paste())
        self.evento(None)
