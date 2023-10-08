from frame import Interface
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Window(ttk.Window):
    def __init__(self):
        super().__init__()
        self.frame = Interface(self)
        self.frame.pack(fill=BOTH, expand=True, padx=2, pady=2)
        
        self.bind('<Return>', self.teclaEnter)
        
        # tecla q para sair/quit
        self.bind('q', lambda x: self.quit)

        
    def teclaEnter(self, event):
        self.iniciar()
        
    def iniciar(self):
        self.frame.Contagem()
        
        
        
        
        
if __name__ == '__main__':
    window = Window()
    window.style.theme_use('cyborg')
    window.bind('<Escape>', lambda x: window.quit())
    
    window.mainloop()