from tkinter import Tk, ttk
from fr import Fr
from sys import exit
    

class app(Tk):
    def __init__(self):
        super().__init__()
        self.title('SistemaLinear')
        
        style = ttk.Style(self)
        self.tk.call('source', './forest_ttk_theme/forest-dark.tcl')
        style.theme_use("forest-dark")
        self.fr = Fr(self, self)

        self.bind('q', self.tecla_q)
        self.geometry('800x500')
        # self.mainloop()
        self.fr.grid()
    
    def tecla_q(self, event):
        from sys import exit
        exit()
def main():
    root = app()
    root.mainloop()
    
if __name__ == '__main__':
    main()