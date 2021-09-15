from tkinter import *


class Teste(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.botao = []
        for i in range(5):
            self.botao.append(Button(self, text=f'botao {i}'))
            self.botao[i].pack()
            
root = Tk()
t = Teste(root)
t.pack()
root.mainloop()