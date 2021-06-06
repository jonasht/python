from tkinter import *


class Interface(Frame):
    def __init__ (self, parent):
        super().__init__(parent)
        self.frameRecomecar = Frame(self)
        self.frameComecar = Frame(self)
        self.frameTotal = Frame(self)

        self.lb1 = Label(self.frameRecomecar, text='Cartas para Recomeçar:')
        self.lb_numero1 = Label(self.frameRecomecar, text='0', fg='green')

        self.lb2 = Label(self.frameComecar, text='Cartas para   Começar:')
        self.lb_numero2 = Label(self.frameComecar, text='0', fg='blue')

        self.lb_falta = Label(self.frameTotal, text='Faltam')
        self.lb_faltaNum = Label(self.frameTotal, text='0', fg='red')

        self.lb_total = Label(self.frameTotal, text='Total')
        self.lb_totalNum = Label(self.frameTotal, text='0', fg='blue')

        self.lb_falta.pack(side=LEFT)
        self.lb_faltaNum.pack(side=LEFT)
        self.lb_total.pack(side=LEFT)
        self.lb_totalNum.pack(side=RIGHT)

 
        
        self.lb1.pack(side=LEFT)
        self.lb_numero1.pack(side=RIGHT)

        self.lb2.pack(side=LEFT)
        self.lb_numero2.pack(side=RIGHT)

        self.frameRecomecar.pack()
        self.frameComecar.pack()
        self.frameTotal.pack()
        
    def atualizarTotal(self, n):
        self.lb_totalNum.config(text=n)
    
    def atualizarRecomecar(self, n):
        self.lb_numero1.config(text=n)  
        
    def atualizarComecar(self, n):
        self.lb_numero2.config(text=n)
    
    def atualizarRestanteDeCartas(self, n):
        self.lb_faltaNum.config(text=n)         
    
if __name__ == '__main__':
    root = Tk()
    root.geometry('300x300')

    frame = Interface(root)
    frame.pack()
    root.mainloop()