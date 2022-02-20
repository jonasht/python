from tkinter import END, Tk, ttk, Text
import uteis as u

conta3x3 = '''2x+6y-2z=24\n4x+5y-4z=24\n6x+5y-4z=28\n'''

class Fr(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
                
        self.teste = ttk.Label(self, text='teste')
        self.teste.pack()
        
        self.txt = Text(self, width=50, height=15)
        self.bt = ttk.Button(self, text='Calcular', 
                             command=self.calcular_evento)
        self.txt.pack()
        self.bt.pack()
        
        self.txt.insert(1.0, conta3x3)
        self.lb_solucao = ttk.Label(self, text='=-=-=-=')
        self.lb_solucao.pack()
        
        self.calcular_evento()
        
        
        
    def calcular_evento(self):
        conta = self.txt.get(1.0, END)

        resolucao = u.calcular(conta)
        # print(resolucao)
        print()
        
        pularLinha = 0
        solve_edit = ''
        for k, v in resolucao.items():
            solve_edit += f'{k}={v:.4f} \n'

        print(solve_edit)
        
        self.lb_solucao.config(text=solve_edit)



if __name__ == '__main__':
    root = Tk()
        
    fr = Fr(root, root)
    fr.grid()
    
    def tecla_q(event):
        from sys import exit
        exit()

    ttk.Label(root, text='algo').grid()
    
    root.bind('q', tecla_q)
    root.geometry('500x500')
    root.mainloop()
