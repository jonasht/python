from tkinter import Tk, ttk



class Fr_alternativas(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con

        self.bt0 = ttk.Button(self, text='bt 0', command=lambda:self.event(0))
        self.bt1 = ttk.Button(self, text='bt 1', command=lambda:self.event(1))
        self.bt2 = ttk.Button(self, text='bt 2', command=lambda:self.event(2))
        self.bt3 = ttk.Button(self, text='bt 3', command=lambda:self.event(3))
        
        
        
        self.bt0.grid(row=1, column=0)
        self.bt1.grid(row=2, column=0)
        self.bt2.grid(row=1, column=1)
        self.bt3.grid(row=2, column=1)

    def event(self, event):
        print(event)


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x500')
    frame = Fr_alternativas(root, root)
    frame.pack()
    

    root.mainloop()
