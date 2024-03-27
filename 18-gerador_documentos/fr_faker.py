
from tkinter import Misc
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap import Window



class Fr_faker(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.fr_left = ttk.Frame(self)
        self.fr_right = ttk.Frame(self)

        # frame left ==================
        self.lb_nome = ttk.Label(self.fr_left, text='Nome:')
        self.lb_fone = ttk.Label(self.fr_left, text='Telefone:')
        self.lb_email = ttk.Label(self.fr_left, text='Email')
        self.lb_dataNasc = ttk.Label(self.fr_left, text='Data Nascimento:')
        self.et_nome = ttk.Entry(self.fr_left)
        self.et_fone = ttk.Entry(self.fr_left)
        self.et_email = ttk.Entry(self.fr_left)
        self.et_dataNasc = ttk.Entry(self.fr_left)

        # frame right ==================
        self.lb_rua = ttk.Label(self.fr_right, text='Rua:')
        self.lb_numero = ttk.Label(self.fr_right, text='Número:')
        self.lb_bairro = ttk.Label(self.fr_right, text='Bairro:')
        self.lb_cidade = ttk.Label(self.fr_right, text='Cidade:')
        self.lb_estado = ttk.Label(self.fr_right, text='Estado:')
        self.et_rua = ttk.Entry(self.fr_right)
        self.et_numero = ttk.Entry(self.fr_right)
        self.et_bairro = ttk.Entry(self.fr_right)
        self.et_cidade = ttk.Entry(self.fr_right)
        self.et_estado = ttk.Entry(self.fr_right)

        # grid ========================
        # frame left
        self.lb_nome.grid(row=1, column=1)
        self.lb_fone.grid(row=2, column=1)
        self.lb_email.grid(row=3, column=1)
        self.lb_dataNasc.grid(row=4, column=1)
        self.et_nome.grid(row=1, column=2)
        self.et_fone.grid(row=2, column=2)
        self.et_email.grid(row=3, column=2)
        self.et_dataNasc.grid(row=4, column=2)
        # frame right
        self.lb_rua.grid(row=1, column=1)
        self.lb_numero.grid(row=2, column=1)
        self.lb_bairro.grid(row=3, column=1)
        self.lb_cidade.grid(row=4, column=1)
        self.lb_estado.grid(row=5, column=1)
        self.et_rua.grid(row=1, column=2)
        self.et_numero.grid(row=2, column=2)
        self.et_bairro.grid(row=3, column=2)
        self.et_cidade.grid(row=4, column=2)
        self.et_estado.grid(row=5, column=2)

        self.fr_left.grid(row=1, column=1)
        self.fr_right.grid(row=1, column=2)

if __name__ == '__main__':
    window = Window()
    frame = Fr_faker(window)
    frame.pack()
    window.style.theme_use('darkly')

    window.mainloop()