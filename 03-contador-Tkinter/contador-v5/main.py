from tkinter import Tk
from frame import Interface


class Principal(Tk):
    def __init__(self):
        super().__init__()
        self.frame = Interface(self)
        self.frame.pack()
        
        self.bind('<Return>', self.teclaEnter)
        
        self.bind('q', self.tecla_q)

    # tecla q para sair/quit
    def tecla_q(self, event):
        self.quit()
        
    def teclaEnter(self, event):
        self.iniciar()
    def iniciar(self):
        self.frame.Contagem()
        
        
        
        
        
if __name__ == '__main__':
    root = Principal()
    root.mainloop()