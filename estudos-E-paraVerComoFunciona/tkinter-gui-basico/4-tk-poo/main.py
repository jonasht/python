from tkinter import *
from MeuGui import MeuGui

janela = Tk()
Label(janela, text=__name__).pack()

# janela popup
popup = Toplevel()
Label(popup, text='anexado').pack(side=LEFT)
MeuGui(popup).pack(side=RIGHT)

janela.mainloop()

