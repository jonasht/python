from tkinter import *


class Frame_matriz(Frame):
    def __init__(self, parent, titulo, matriz, resposta = ''):
        super().__init__(parent)
        
        self.frameMatriz = LabelFrame(self, text=titulo.title())
        # colocando as labels
        for i, im in enumerate(matriz):
            for ii, iim in enumerate(im):
                Label(self.frameMatriz, text=f'{iim}').grid(row=i, column=ii, padx=5)
        self.frameMatriz.grid()
        self.lb_resposta = Label(self,text=resposta, fg='green').grid()
