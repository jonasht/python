import ttkbootstrap as ttk
from tkinter import ttk as tt
from ttkbootstrap import font



class Window(ttk.Window):
    def __init__(self, parent):
        super().__init__(parent)
        
        # self.s = ttk.Style()
        # self.s.configure('TButton', font=('Helvetica', 22), foreground='green')
        self.font = ('Courier', 20, 'bold')
        self.bt = ttk.Button(self, text='teste', font=self.font)
        
        
        self.bt.pack()
        

window = Window(None)

window.geometry('500x500')
window.style.theme_use('darkly')
window.bind('q', lambda x: window.quit())

window.mainloop()
