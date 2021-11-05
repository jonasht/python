import tkinter as tk
from tkinter import Tk, ttk
from typing import Text


class App(Tk):
    def __init__(self) -> None:

        self.tree = ttk.Treeview(self)
        self.tree.insert(self, 'end', 'widgets', text='widgets tour')
        self.tree.insert(self, 0, 'gallery', text='applications')
        self.id = self.tree.insert(self, 'end', text='tutorial')

        self.tree.insert('widgets', 'end', text='canvas')
        self.tree.insert(id, 'end', text='tree')





App().mainloop()

        
        
        
        
