from tkinter import ttk
from tkinter.constants import CENTER, END, EW
from validate_docbr import CPF

class Fr_cpf(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.cpf = CPF()
        self.cpf_num = ''


        #   cpf =================================================
        self.lbfr = ttk.Labelframe(self, text='CPF')
        self.etd = ttk.Entry(self.lbfr)
        self.bt_gerar = ttk.Button(self.lbfr, text='Gerar', command=self.gerar)
        self.chbt_mask = ttk.Checkbutton(self.lbfr, text='mark', command=self.chbt_Evento)

        self.etd.grid(row=0, column=0, padx=2, pady=5)
        self.bt_gerar.grid(row=0, column=1, padx=2, pady=5)
        self.chbt_mask.grid(row=0, column=2, padx=2, pady=5)
        self.lbfr.pack()
        
        # gerando =-=-
        self.gerar()

        

    def gerar(self):
        if 'selected' not in self.chbt_mask.state():
            self.etd.delete(0, END)
            self.cpf_num = self.cpf.generate()
            self.etd.insert(0, self.cpf_num)
        else:
            self.chbt_Evento()


    def chbt_Evento(self):
        if 'selected' in self.chbt_mask.state():
            self.etd.delete(0, END)
            self.etd.insert(0, self.cpf.mask(self.cpf_num))
        else:
            self.etd.delete(0, END)
            self.etd.insert(0, self.cpf_num)

