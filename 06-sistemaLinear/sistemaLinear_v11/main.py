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

        # self.bind('q', exit)
        self.geometry('800x665')
  
        self.fr.grid()
    
def main():
    root = app()
    root.mainloop()
    
if __name__ == '__main__':
    main()