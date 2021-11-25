from tkinter import ttk
import tkinter as tk


class Fr_finalizacao(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)


        # self.lb_entrega = ttk.Label(self, text='É para entrega:')
        
        self.cbt_cpf = ttk.Checkbutton(self, text='CPF na nota')
        self.cbt_entrega = ttk.Checkbutton(self, text='É para a entrega')
        
        # self.lb_cpf.grid()
        self.cbt_cpf.grid()
        self.cbt_entrega.grid()
        
        
        
if __name__ == '__main__':
    root = tk.Tk()
    frame = Fr_finalizacao(root)
    frame.pack()
    root.geometry('500x500')
    root.mainloop()