from tkinter import *                
from tkinter import font as tkfont  
from tkinter import ttk
import tkinter as tk
from frAcesso import FrAcesso
from frLogin import FrLogin
from frCadastro import FrCadastro


class Principal(Tk):
    
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.login = ''

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # Create a style
        style = ttk.Style(self)

        # Import the tcl file
        self.tk.call("source", "forest-dark.tcl")

        # Set the theme with the theme_use method
        style.theme_use("forest-dark")

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FrLogin, FrAcesso, FrCadastro):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('FrLogin') 


    def set_login(self, login):
        self.login = login
    def show_frame(self, page_name):
        if page_name == 'FrAcesso':
            frame = self.frames[page_name]
            
            print('login main:', self.login)
            frame.tkraise()
            FrAcesso.set_login(self, self.login)

        else:
            
            frame = self.frames[page_name]
            frame.tkraise()

    


if __name__ == "__main__":
    root = Principal()
    root.geometry('500x300')
    root.mainloop()
    