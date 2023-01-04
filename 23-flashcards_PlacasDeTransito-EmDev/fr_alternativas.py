from tkinter import Tk, ttk
import customtkinter as ctk


class Fr_alternativas(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        self.width_bts=100
        
        self.bt0 = ttk.Button(self, text='', command=lambda:self.event(0))
        self.bt1 = ttk.Button(self, text='', command=lambda:self.event(1))
        self.bt2 = ttk.Button(self, text='', command=lambda:self.event(2))
        self.bt0.configure(width=self.width_bts)
        self.bt1.configure(width=self.width_bts)
        self.bt2.configure(width=self.width_bts)


        self.bt0.grid(pady=10)
        self.bt1.grid(pady=10)
        self.bt2.grid(pady=10)
    # mostrar nos botoes
    def display(self, lista):
        self.bt0.configure(text=lista[0])
        self.bt1.configure(text=lista[1])
        self.bt2.configure(text=lista[2])
        
        
        
    def event(self, event):
        self.con.set_resposta(event)


if __name__ == '__main__':
    root = Tk()
    root.geometry('1000x500')
    frame = Fr_alternativas(root, root)
    frame.pack()
    
    lista = ['branco', 'preto', 'vermelho']
    frame.display(lista)

    root.mainloop()
