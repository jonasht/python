from tkinter import *

class Interface(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        bt00 = Button(self, width=10, height=5)
        bt01 = Button(self, width=10, height=5)
        bt02 = Button(self, width=10, height=5)

        bt10 = Button(self, width=10, height=5)
        bt11 = Button(self, width=10, height=5)
        bt12 = Button(self, width=10, height=5)
        
        bt20 = Button(self, width=10, height=5)
        bt21 = Button(self, width=10, height=5)
        bt22 = Button(self, width=10, height=5)
        
        # colocando com o grid
        bt00.grid(row=0, column=0)
        bt01.grid(row=0, column=1)
        bt02.grid(row=0, column=2)
        
        bt10.grid(row=1, column=0)
        bt11.grid(row=1, column=1)
        bt12.grid(row=1, column=2)
        
        bt20.grid(row=2, column=0)
        bt21.grid(row=2, column=1)
        bt22.grid(row=2, column=2)
        
if __name__ == '__main__':
    root = Tk()
    interface = Interface(root)
    interface.pack()
    root.mainloop()