from tkinter import ttk
from tkinter.constants import CENTER, EW, NSEW, NW, TOP



class Fr_faturamento(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lbfr = ttk.LabelFrame(text='Lucro')

        self.lb_lucro = ttk.Label(self.lbfr, text=' Lucro Total R$:')
        self.lb_lucroInfo = ttk.Label(self.lbfr, text='18521,45  ')
        
        self.lb_lucro.grid(row=0, column=0, sticky=EW, padx=5, pady=2)
        self.lb_lucroInfo.grid(row=0, column=1, sticky=EW, padx=5, pady=2)

        


        