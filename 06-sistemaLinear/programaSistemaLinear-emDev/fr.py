from re import S
from tkinter import BOTTOM, END, LEFT, N, NSEW, RIGHT, Tk, ttk, Text
import uteis as u
import exemplo as ex


class Fr(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        
        self.fr_left = ttk.Frame(self)
        self.txt = Text(self.fr_left, width=50, height=15)
        self.bt_calcular = ttk.Button(self.fr_left, text='Calcular', 
                             command=self.calcular_evento)
        self.bt_limpar = ttk.Button(self.fr_left, text='Limpar', command=self.delete_evento)
        self.txt.grid(row=0, column=0, sticky=NSEW, columnspan=2)
        self.bt_calcular.grid(row=1, column=1, sticky=NSEW)
        self.bt_limpar.grid(row=1, column=0, sticky=NSEW)

        # self.txt.insert(1.0, conta3x3)
        self.lb_solucao = ttk.Label(self, text='', foreground='green')
        
        
        # label frame
        self.lbfr = ttk.Labelframe(self, text='exemplo')
        self.bt_e2x2 = ttk.Button(self.lbfr, text='2x2', command=self.bt_2x2evento)
        self.bt_e3x3 = ttk.Button(self.lbfr, text='3x3', command=self.bt_3x3evento)
        self.bt_e4x4 = ttk.Button(self.lbfr, text='4x4', command=self.bt_4x4evento)
        
        self.bt_e2x2.grid(padx=8, pady=6)
        self.bt_e3x3.grid(padx=8, pady=6)
        self.bt_e4x4.grid(padx=8, pady=6)
        
        self.fr_left.grid(row=0, column=0, padx=15, pady=15)
        self.lbfr.grid(row=0, column=1, padx=12)
        self.lb_solucao.grid(row=1, column=0, columnspan=3)
        
        
    def delete_evento(self):
        self.txt.delete(1.0, END)
        
    def bt_2x2evento(self):
        self.delete_evento()
        self.txt.insert(1.0, ex.conta2x2)
        
    def bt_3x3evento(self):
        self.delete_evento()
        self.txt.insert(1.0, ex.conta3x3)
        
    def bt_4x4evento(self):
        self.delete_evento()
        self.txt.insert(1.0, ex.conta4x4) 
        # self.txt.insert(1.0, ex.conta5x5) 
        
    def calcular_evento(self):
        conta = self.txt.get(1.0, END)
        print(conta)
        solve = u.calcular(conta)
        print(solve)
        lb_solve = ''
        for c, v in solve.items():
            print(c, v)
            lb_solve += f'{c.upper()} = {v}\n'
        
        self.lb_solucao.config(text=lb_solve)



if __name__ == '__main__':
    root = Tk()
        
    fr = Fr(root, root)
    fr.grid()
    
    def tecla_q(event):
        from sys import exit
        exit()

    
    root.bind('q', tecla_q)
    root.geometry('800x500')
    root.mainloop()
