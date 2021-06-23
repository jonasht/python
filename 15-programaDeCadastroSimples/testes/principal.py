from tkinter import *
from Frame import MainFrame

class teste(Tk):
    def __init__(self):
        super().__init__()
        
        self.title('teste')
        self.geometry('407x200+651+300')

root = teste()
frameTeste = MainFrame(root)
root.mainloop()