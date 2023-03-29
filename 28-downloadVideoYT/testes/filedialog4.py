# import tkinter as tk
# from tkinter import ttk

import ttkbootstrap as ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from util import write, read
from ttkbootstrap.constants import *


class Window(ttk.Window):
    def __init__(self) -> None:
        super().__init__()
    
        self.style.theme_use('darkly')
        self.title(' Open File Dialog')
        self.resizable(False, False)
        self.geometry('500x500')

        # text ttk
        self.text = ttk.Text(self)
        self.lb_fileName = ttk.Label(self, text='arquivo:', bootstyle='success')
        
        self.bt_open= ttk.Button(self, text='Open a File',command=self.select_file)

        self.bt_open.pack(expand=True)
        self.lb_fileName.pack(expand=True)
        self.text.pack(expand=True)

    def select_file(self):
        filetypes = (
            ('imagem', '*.txt'),
            ('todos arquivos', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='.',
            filetypes=filetypes)

        # showinfo(
        #     title='Selected File',
        #     message=filename
        # )
        # ttk.showinfo()

        self.lb_fileName.configure(text=f'arquivo:{filename}')
        txt = read(filename)
        
        self.text.insert(1.0, txt)


    
    
def main():
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()

