from tkinter import END, Tk, ttk
import lippy 



class Fr1(ttk.Frame):
    def __init__(self, parent, con=None):
        super().__init__(parent)
        self.lb_titulo = ttk.Label(self, text='')
        self.lb_titulo.grid()
        
        self.fr_cima = ttk.Frame(self)
        self.fr_meio = ttk.Frame(self)
        # linha z =-=-=-=-==-=-=-=-
        self.etd1x = ttk.Entry(self.fr_cima)
        self.lb1x = ttk.Label(self.fr_cima, text='x1')
        self.etd2x = ttk.Entry(self.fr_cima)
        self.lb2x = ttk.Label(self.fr_cima, text='x2')
        self.etd3x = ttk.Entry(self.fr_cima)
        self.lb3x = ttk.Label(self.fr_cima, text='x3')

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
        # botao
        self.bt_solve = ttk.Button(self, text='calcular', command=self.to_solve)
        # label solve =-=-=-=-=-=-=
        self.lb_solve = ttk.Label(self, text='')

         # colocando linha z =-=-=-=-==-=-=-=-
        self.etd1x.grid(row=0, column=0)
        self.lb1x.grid(row=0, column=1)
        self.etd2x.grid(row=0, column=2)
        self.lb2x.grid(row=0, column=3)
        self.etd3x.grid(row=0, column=4)
        self.lb3x.grid(row=0, column=5) 
        
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
        
        self.fr_cima.grid()
        self.fr_meio.grid()
        # colocando botao solve
        self.bt_solve.grid()
        self.lb_solve.config(text='resultado')
        self.lb_solve.grid()
        self.put_default()
    def put_default(self):
        self.etd1x.insert(END, 6)
        self.etd2x.insert(END, 6)
        self.etd3x.insert(END, 6)

        # Matriz
        self.etdx11.insert(END,4 )
        self.etdx12.insert(END, 1)
        self.etdx13.insert(END,1 )
        self.etdEg1.insert(END, 5)

        self.etdx21.insert(END, 1)
        self.etdx22.insert(END, 2)
        self.etdx23.insert(END, 0)
        self.etdEg2.insert(END, 3)

        self.etdx31.insert(END, 0)
        self.etdx32.insert(END, 0.5)
        self.etdx33.insert(END, 4)
        self.etdEg3.insert(END, 8)
        
    def to_solve(self):
        z1 = self.etd1x.get() 
        z2 = self.etd2x.get() 
        z3 = self.etd3x.get() 

        print(z1, z2, z3)
        
        x11  = self.etdx11.get()
        x12  = self.etdx12.get()
        x13  = self.etdx13.get()
        Eg1  = self.etdEg1.get()
        
        x21  = self.etdx21.get()
        x22  = self.etdx22.get()
        x23  = self.etdx23.get()
        Eg2  = self.etdEg2.get()

        x31  = self.etdx31.get()
        x32  = self.etdx32.get()
        x33  = self.etdx33.get()
        Eg3  = self.etdEg3.get()
        
        c = [z1, z2, z3]
        a = [
            [x11, x12, x13],
            [x21, x22, x23],
            [x31, x32, x33]
        ]
        b = [Eg1, Eg2, Eg3]

        simplex = lippy.SimplexMethod(c, a, b)
        solution, value = simplex.solve()
        
        solve = f'{solution}\n{value}'
        self.lb_solve.config(text=solve)



        
if __name__ == '__main__':
    root = Tk()
    root.title('simplex')
    fr = Fr1(root)
    fr.pack()
    root.geometry('700x500')
    root.mainloop()