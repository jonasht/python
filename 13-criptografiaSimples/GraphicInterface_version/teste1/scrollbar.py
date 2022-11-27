from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import title
from sys import exit
from test_util import text_char


class Text_scroll(ttk.Scrollbar):
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


        
def main():
    root = Tk()
    fr1 = ttk.Frame(root)
    fr2 = ttk.Frame(root)

    scroll1 = Text_scroll(fr1)
    scroll2 = Text_scroll(fr2)
    
    scroll1.grid()
    scroll2.grid()
    scroll1.txt.insert(END, text_char)
    scroll2.txt.insert(END, text_char)
    
    fr1.grid(row=1, column=0)
    fr2.grid(row=1, column=1)

    root.tk.call('source', './forest_ttk_theme/forest-dark.tcl')
    style = ttk.Style(root)

    style.theme_use('forest-dark')


    root.mainloop()


if __name__ == '__main__':
    main()
