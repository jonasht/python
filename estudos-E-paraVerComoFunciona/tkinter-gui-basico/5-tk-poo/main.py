from tkinter import *
from tkinter.messagebox import showinfo 
from MeuGui import MeuGui


class GuiCostumizado(MeuGui):
    def reply(self):
        showinfo(title='popup', message='Certo')

if __name__ == '__main__':
    GuiCostumizado().pack()
    mainloop()

