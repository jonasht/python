from tkinter import *

class Interface(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # colocando vez x e O
        self.vez = ['X', 'O']
        
        # botoes ...
        self.bt00 = Button(self, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('00'))
        self.bt01 = Button(self, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('01'))
        self.bt02 = Button(self, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('02'))
        self.bt10 = Button(self, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('10'))
        self.bt11 = Button(self, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('11'))
        self.bt12 = Button(self, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('12'))
        self.bt20 = Button(self, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('20'))
        self.bt21 = Button(self, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('21'))
        self.bt22 = Button(self, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('22'))
        
        # colocando botoes com o grid
        self.bt00.grid(row=0, column=0)
        self.bt01.grid(row=0, column=1)
        self.bt02.grid(row=0, column=2)
        
        self.bt10.grid(row=1, column=0)
        self.bt11.grid(row=1, column=1)
        self.bt12.grid(row=1, column=2)
        
        self.bt20.grid(row=2, column=0)
        self.bt21.grid(row=2, column=1)
        self.bt22.grid(row=2, column=2)
        
        
    def marcar(self, opcao):
        if opcao == '00':
            print(00)
            self.bt00.config(state=DISABLED, text=self.vez[0])
        if opcao == '01':
            self.bt01.config(state=DISABLED, text=self.vez[0])
        if opcao == '02':
            self.bt02.config(state=DISABLED, text=self.vez[0])

        if opcao == '10':
            self.bt10.config(state=DISABLED, text=self.vez[0])
        if opcao == '11':
            self.bt11.config(state=DISABLED, text=self.vez[0])
        if opcao == '12':
            self.bt12.config(state=DISABLED, text=self.vez[0])
            
        if opcao == '20':
            self.bt20.config(state=DISABLED, text=self.vez[0])
        if opcao == '21':
            self.bt21.config(state=DISABLED, text=self.vez[0])
        if opcao == '22':
            self.bt22.config(state=DISABLED, text=self.vez[0])

        # mudando a vez  
        self.vez.reverse()
if __name__ == '__main__':
    root = Tk()
    interface = Interface(root)
    interface.pack()
    root.mainloop()