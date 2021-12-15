from tkinter import Tk, ttk
from frame import Fr

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Tradutor')
        self.geometry('1150x550')
        fr = Fr(self)
        fr.pack()


def main():
    root = App()
    root.mainloop()
        
main()