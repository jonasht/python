from tkinter import Frame, Label, Tk
from random import randint

matriz = [[1, 2, 8, 1, 2], [2, -1, 3, 2, -1], [3, 1, 2, 3, 1]]
print(matriz)

class Teste(Frame):
    def __init__(self, parent, matriz):
        super().__init__(parent)
        for i, im in enumerate(matriz):
            for ii, iim in enumerate(im):
                Label(self, text=f'{iim}').grid(row=i, column=ii, padx=5)

root = Tk()
root.geometry('400x400')
teste = Teste(root, matriz)
teste.pack()
root.mainloop()