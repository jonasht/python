from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import title

text_char = '''
ashfçsafjasd
sfsdfads
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsd
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
fsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
fsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsd
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n
sdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\nsdfsd\n

'''
class Scroll(ttk.Scrollbar):
    def __init__(self, parent):
        super().__init__(parent)

        lb = ttk.Label(self, text='scroll bar')
        lb.grid()

        self.txt = Text(self)
        self.txt.grid(row=1, column=0)
        self.scbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.txt.yview) 
        self.s2 = ttk.Scrollbar(self, orient=HORIZONTAL, command=self.txt.xview)

        self.txt.config(yscrollcommand=self.scbar.set)
        self.txt.config(xscrollcommand=self.s2.set)

        self.scbar.grid(row=1, column=1, sticky=NS)
        # self.s2.grid(row=2, column=0, sticky=EW)

        self.txt.insert(END, text_char)
root = Tk()
Scroll(root).pack()
root.tk.call('source', './forest_ttk_theme/forest-dark.tcl')
style = ttk.Style(root)

    # Set the theme with the theme_use method
style.theme_use("forest-dark")

from sys import exit

root.geometry('1000x1000')

root.bind('q', exit)
root.mainloop()

