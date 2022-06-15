from tkinter import Tk, ttk



class Fr1(ttk.Frame):
    def __init__(self, parent, con=None):
        super().__init__(parent)
        self.lb_titulo = ttk.Label(self, text='funcionando')
        self.lb_titulo.grid()

        self.fr_meio = ttk.Frame(self)
        # linha 1 =-=-=-=-==-=-=-=-
        self.etdx11 = ttk.Entry(self.fr_meio)
        self.etdx12 = ttk.Entry(self.fr_meio)
        self.etdx13 = ttk.Entry(self.fr_meio)
        self.lbx11 = ttk.Label(self.fr_meio, text='X1')
        self.lbx12 = ttk.Label(self.fr_meio, text='X2')
        self.lbx13 = ttk.Label(self.fr_meio, text='X3')
        self.lbEg1 = ttk.Label(self.fr_meio, text='=')
        self.etdEg1 = ttk.Entry(self.fr_meio)

        # linha 2 =-=-=-=-=-
        self.etdx21 = ttk.Entry(self.fr_meio)
        self.etdx22 = ttk.Entry(self.fr_meio)
        self.etdx23 = ttk.Entry(self.fr_meio)
        self.lbx21 = ttk.Label(self.fr_meio, text='X1')
        self.lbx22 = ttk.Label(self.fr_meio, text='X2')
        self.lbx23 = ttk.Label(self.fr_meio, text='X3')
        
        self.lbEg2 = ttk.Label(self.fr_meio, text='=')
        self.etdEg2 = ttk.Entry(self.fr_meio)
        
        # linha 3 =-=-=-=-=-=-=-=-=-=--=--=
        self.etdx31 = ttk.Entry(self.fr_meio)
        self.etdx32 = ttk.Entry(self.fr_meio)
        self.etdx33 = ttk.Entry(self.fr_meio)
        self.lbx31 = ttk.Label(self.fr_meio, text='X1')
        self.lbx32 = ttk.Label(self.fr_meio, text='X2')
        self.lbx33 = ttk.Label(self.fr_meio, text='X3')
        self.lbEg3 = ttk.Label(self.fr_meio, text='=')
        self.etdEg3 = ttk.Entry(self.fr_meio)
         # colocando linha 1 =-=-=-=-==-=-=-=-
        self.etdx11.grid(row=1,column=1)
        self.lbx11.grid(row=1,column=2) 
        self.etdx12.grid(row=1,column=3)
        self.lbx12.grid(row=1,column=4) 
        self.etdx13.grid(row=1,column=5)
        self.lbx13.grid(row=1,column=6) 
        self.lbEg1.grid(row=1, column=7)
        self.etdEg1.grid(row=1, column=8)
        # # colocando linha 2 =-=-=-=-=-
        self.etdx21.grid(row=2,column=1)
        self.lbx21.grid(row=2,column=2) 
        self.etdx22.grid(row=2,column=3)
        self.lbx22.grid(row=2,column=4) 
        self.etdx23.grid(row=2,column=5)
        self.lbx23.grid(row=2,column=6) 
        
        self.lbEg2.grid(row=2, column=7)
        self.etdEg2.grid(row=2, column=8)

        # # colocando linha 3 =-=-=-=-=-=-=-=-=-=--=--=
        self.etdx31.grid(row=3,column=1)
        self.lbx31.grid(row=3,column=2) 
        self.etdx32.grid(row=3,column=3)
        self.lbx32.grid(row=3,column=4) 
        self.etdx33.grid(row=3,column=5)
        self.lbx33.grid(row=3,column=6) 
        self.lbEg3.grid(row=3, column=7)
        self.etdEg3.grid(row=3, column=8)

        self.fr_meio.grid()
if __name__ == '__main__':
    root = Tk()
    fr = Fr1(root)
    fr.pack()
    root.geometry('700x500')
    root.mainloop()