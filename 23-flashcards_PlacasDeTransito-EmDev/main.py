from tkinter import TOP, Tk, ttk
import customtkinter as ctk
from fr_alternativas import Fr_alternativas


class Fr_cards(ctk.CTkFrame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con

        
        self.lb = ctk.CTkLabel(self, text='teste')
        self.lb.grid()

        
        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.fr_cards = Fr_cards(self, self)
        self.fr_cards.pack(side=TOP)
        
        self.fr_alternativas = Fr_alternativas(self, self)
        self.fr_alternativas.pack(side=TOP)

        
        
        
if __name__ == '__main__':
    app = App()
    app.geometry('800x800')
    app.mainloop()
