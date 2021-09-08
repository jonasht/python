from tkinter import *


class Frames(Frame):
    def __init__(self, parent, nome, quatidade, tamanho, cor):
        super().__init__(parent)
        
        self.lb_nome = Label(self, text=f'nome:{nome}')
        self.lb_quatidade = Label(self, text=f'quatidade:{quatidade}')
        self.lb_tamanho = Label(self, text=f'tamanho:{tamanho}')
        self.lb_cor = Label(self, text=f'cor:{cor}')
        
        self.lb_nome.grid(row=1)
        self.lb_quatidade.grid(row=2)
        self.lb_tamanho.grid(row=3)
        self.lb_cor.grid(row=4)