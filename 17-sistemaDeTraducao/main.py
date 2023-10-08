# from tkinter import Tk, ttk
import ttkbootstrap as ttk

from tkinter.constants import CENTER
from frame import Fr

class App(ttk.Window):
    def __init__(self):
        super().__init__()
        self.title('Tradutor')
        
  

        fr = Fr(self)
        fr.pack(anchor=CENTER)

        
def main():
    root = App()
    root.place_window_center()
    root.style.theme_use('darkly')
    
    root.bind('<Escape>', lambda x: root.quit())
    
    root.mainloop()
    
if __name__ == '__main__':
    main()