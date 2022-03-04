from tkinter import ttk
from tkinter import *



class App(Tk):
    def __init__(self):
        super().__init__()
        self.text = Text(self, background='black',
                         foreground='white',
                         font='arial 20 bold',
                         height=10, width=30)
        
        self.bind('<KeyRelease>', self.event)
        
        self.text.pack()

    def event(self, event):
        print(self.text.get('1.0', END))
    
root = App()
root.mainloop()