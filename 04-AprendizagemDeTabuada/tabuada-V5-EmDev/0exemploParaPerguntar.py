from tkinter import *

class classeFrame(Frame):
    def __init__(self, container):
        super().__init__(container)
        

        lb = Label(self, text='frame')
        lb.pack()

        bt = Button(text='aperte aqui')
        bt.pack()

        
        
        
        
class principal(Tk):
    def __init__ (self):
        super().__init__()
        
        
        self.bt_iniciar = Button(self, text='inciar', command=self.iniciar)
        self.bt_iniciar.pack()

        
    def iniciar(self):
        self.frame = classeFrame(self)
        self.frame.pack()
        
    def funcaoDaClassePrincipal(self):
        print('conseguiu')
        
if __name__ == '__main__':
    root = principal()
    root.geometry('400x400')
    root.mainloop()
    
    