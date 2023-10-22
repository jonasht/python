import ttkbootstrap as ttk
from ttkbootstrap.constants import *



class Fr_ (ttk.Frame):
    def __init__(self, parent, ) -> None:
        super().__init__(parent)
        
        

        self.menu = ttk.Menubutton(self, )

        
        
        
        self.menu.grid()
        
        
if __name__ == '__main__':
    window = ttk.Window('cyborg')
    fr = Fr_(window)
    fr.pack()

    window.bind('q', lambda x: window.quit())
    
    window.mainloop()
    