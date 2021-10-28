from tkinter import *

class FrLogin(Frame):
    def __init__(self, parents):
        super().__init__(parents)

        self.lbfr_meio = LabelFrame(self, text='Login')
        
        self.lb_login = Label(self.lbfr_meio, text='login:')
        self.lb_senha = Label(self.lbfr_meio, text='Senha:')

        self.etd_login = Entry(self.lbfr_meio)
        self.etd_senha = Entry(self.lbfr_meio)

        self.lb_login.grid(row=0, column=0)
        self.etd_login.grid(row=0, column=1)
        self.lb_senha.grid(row=1, column=0)
        self.etd_senha.grid(row=1, column=1)

        self.bt_limpar = Button(self.lbfr_meio, text='Limpar')
        self.bt_entrar = Button(self.lbfr_meio, text='Entrar')
        self.bt_limpar.grid(row=2, column=0)
        self.bt_entrar.grid(row=2, column=1)

        
        self.lbfr_meio.pack()

 
        
if __name__ == '__main__':
    
    root = Tk()
    frame = FrLogin(root)
    root.geometry('500x500')

    frame.pack()
    root.mainloop()

