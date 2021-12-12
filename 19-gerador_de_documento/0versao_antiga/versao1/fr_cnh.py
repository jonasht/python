from tkinter import ttk
from tkinter.constants import END, EW
from validate_docbr import CNH

class Fr_cnh(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.cnh = CNH()
        self.cnh_num = ''


        #   cnh =================================================
        self.lbfr = ttk.Labelframe(self, text='CNH')
        self.etd = ttk.Entry(self.lbfr)
        self.bt_gerar = ttk.Button(self.lbfr, text='Gerar', command=self.gerar)
        self.chbt_mask = ttk.Checkbutton(self.lbfr, text='mask', command=self.chbt_Evento)

        self.etd.grid(row=0, column=0, padx=2, pady=5)
        self.bt_gerar.grid(row=0, column=1, padx=2, pady=5)
        self.chbt_mask.grid(row=0, column=2, padx=2, pady=5)
        self.lbfr.pack()
        
        # gerando =-=-
        self.gerar()

        

    def gerar(self):
        if 'selected' not in self.chbt_mask.state():
            self.etd.delete(0, END)
            self.cnh_num = self.cnh.generate()
            self.etd.insert(0, self.cnh_num)
        else:
            self.chbt_Evento()


    def chbt_Evento(self):
        if 'selected' in self.chbt_mask.state():
            self.etd.delete(0, END)
            self.etd.insert(0, self.cnh.mask(self.cnh_num))
        else:
            self.etd.delete(0, END)
            self.etd.insert(0, self.cnh_num)

