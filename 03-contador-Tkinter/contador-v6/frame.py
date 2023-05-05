import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Interface(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        
        self.label = ttk.Label(self, text="Quantos Segundos:", font='Bold')

        self.etd = ttk.Entry(self)

        self.lb_contagem = ttk.Label(self, text='0', font='Times 120 bold', bootstyle=SUCCESS)

        self.bt = ttk.Button(self, text='Começar', bootstyle=SUCCESS, command=self.Contagem)
        self.bt_stop = ttk.Button(self, text='parar', bootstyle=WARNING, command=self.set_stop)

        self.bt_sair = ttk.Button(self, text='Sair', bootstyle=DANGER, command=self.quit)
        self.lb_aviso = ttk.Label(self, text='', bootstyle=INFO)
        
        self.label.grid(row=0, column=0, sticky=E)
        self.etd.grid(row=0, column=1, pady=5)
        self.lb_contagem.grid(row=2, column=0, columnspan=2, pady=30)
        self.lb_aviso.grid(row=3, columnspan=2)
        
        self.bt.grid(row=4, column=1, columnspan=2, sticky=EW)
        self.bt_stop.grid(row=4, column=0, sticky=EW)
        self.bt_sair.grid(row=5, columnspan=2, sticky=EW)

        

        self.etd.focus()
        self.ate=0
        self.stop=[False, True]
        self.segundos = None
        self.etd.bind('<KeyRelease>', self.etd_event)
        self.bt_stop.config(state=DISABLED)
    def etd_event(self, event):
        etd = self.etd.get()
        self.lb_aviso.config(text='')
        # se digito de entrada nao eh numero, serah apagado
        if not etd.isdigit() and not etd == '':
            self.etd.delete(len(etd[:-1]), END)
            self.lb_aviso.config(text='somente numeros', bootstyle=DANGER)
        # somente 4 digitos sao permitidos
        elif len(etd) >= 5:
            self.etd.delete(len(etd[:-1]), END)
            self.lb_aviso.config(text='somente 4 digitos ', bootstyle=DANGER)
    def set_stop(self):
        
        self.stop.reverse()
        self.bt.config(state=NORMAL)
        if self.stop[0]:
            self.bt_stop.config(state=DISABLED)
        else:
            self.bt_stop.config(state=NORMAL)
        
        
    def Contagem(self):
        self.lb_aviso.config(text='')
        # entrada = self.etd.get()
        
        
        # self.bt.config(state=DISABLED)
        
        if self.segundos == None:

            if self.etd.get() != '':
                self.ate = int(self.etd.get())
            else:
                self.etd.delete(0, END)
                self.etd.insert(0, 10)
                self.ate = 10
            self.segundos = -1 
        if self.segundos == self.ate:
            self.lb_aviso.config(text='fim de contagem', bootstyle=SUCCESS)
            self.etd.config(state=NORMAL)
            self.bt.config(state=NORMAL)
            self.bt_stop.config(state=DISABLED)
            self.segundos = None
            self.ate = 0
        elif not self.stop[0]:
            self.segundos += 1
            self.lb_contagem['text'] = self.segundos
            self.lb_contagem.after(1000, self.Contagem)
            self.bt_stop.config(state=NORMAL)
            self.bt.config(state=DISABLED)
            self.etd.config(state=DISABLED)
        else:
            self.stop.reverse()
            
            


if __name__ == '__main__':
    root = ttk.Window()
    interface = Interface(root)
    interface.pack()

    root.mainloop()