from frames.fr import Fr
from tkinter import Tk, ttk
from sys import exit


class App(Tk):
    def __init__(self):
        super().__init__()
         
        style = ttk.Style(self)

        # Import the tcl file
        self.tk.call('source', './forest_ttk_theme/forest-dark.tcl')

        # Set the theme with the theme_use method
        style.theme_use("forest-dark")

        Fr(self).pack()
        
        # aperte q para fechar a janela
        # self.bind('q', exit)
        self.title('criptografia')

        
        
def main():
    app = App()
    app.bind('<Escape>', lambda x: app.quit())
    
    app.mainloop()

    
if __name__ == '__main__':
    main()