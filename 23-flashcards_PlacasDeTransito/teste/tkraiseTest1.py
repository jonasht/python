from tkinter import ttk, Tk



class App(Tk):
    def __init__(self):
        super().__init__()
 
        self.container = ttk.Frame(self)
        
            

        self.fr_bt = ttk.Frame(self)
        self.bt1 = ttk.Button(self.fr_bt, text='<<<')
        self.bt2 = ttk.Button(self.fr_bt, text='>>>')
        
        self.bt1.grid(row=0, column=0)
        self.bt2.grid(row=0, column=1)
        self.fr_bt.pack()
        
        
class Fr1(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        self.lb = ttk.Label(self, text='')
        self.lb.pack()
        
class Fr2(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con  
        self.lb = ttk.Label(self, text='')
        self.lb.pack()

class Fr3(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        self.lb = ttk.Label(self, text='')
        self.lb.pack()

# class Fr1(ttk.Frame):
#     def __init__(self, parent, con):
#         super().__init__(parent)
#         self.con = con                
if __name__ == '__main__':
    app = App()
    app.title('teste')
    app.geometry('500x500')
    app.mainloop()