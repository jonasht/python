from tkinter import *
from frameMatriz import Interface

class Principal(Tk):
    def __init__(self):
        super().__init__()
        
        interfaceMatriz = Interface(self)
        interfaceMatriz.pack()

root = Principal()
root.mainloop()