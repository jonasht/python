from tkinter import Tk, ttk
from tkinter.constants import CENTER
from frame import Fr

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Tradutor')
        self.geometry('1310x550')
        self.style = ttk.Style(self)
        self.tk.call('source', './theme/forest-dark.tcl')
        self.style.theme_use('forest-dark')

        fr = Fr(self)
        fr.pack(anchor=CENTER)

        
def main():
    root = App()
    root.mainloop()
    
if __name__ == '__main__':
    main()