from tkinter import ttk
import tkinter as tk
from tkinter.constants import EW


class Fr_finalizacao(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con

        
        self.cbt_cpf = ttk.Checkbutton(self, text='CPF na nota')
        self.etd_cpf = ttk.Entry(self)
        self.cbt_entrega = ttk.Checkbutton(self, text='É para a entrega')
        self.bt_finalizar = ttk.Button(self, text='Finalizar', command=self.finalizar_evento)
        
        self.cbt_cpf.grid(padx=5, pady=2)
        self.etd_cpf.grid(padx=5, pady=2)
        self.cbt_entrega.grid(padx=5, pady=2)
        self.bt_finalizar.grid(sticky=EW)
        
    def finalizar_evento(self):
        self.con.apagar_tudo()
        
if __name__ == '__main__':
    root = tk.Tk()
    frame = Fr_finalizacao(root, root)
    
    frame.pack()
    root.geometry('500x500')
    root.mainloop()