from tkinter import Tk
from fr import Fr
from sys import exit


class app(Tk):
    def __init__(self):
        super().__init__()
        self.title('SistemaLinear')
        self.fr = Fr(self, self)

        self.bind('q', self.tecla_q)
        self.geometry('800x500')
        # self.mainloop()
        self.fr.grid()
    
    def tecla_q(self, event):
        from sys import exit
        exit()

if __name__ == '__main__':
        
    root = app()
    root.mainloop()