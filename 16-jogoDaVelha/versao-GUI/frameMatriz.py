from tkinter import *
import uteis

class Interface(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # colocando vez x e O
        self.vez = ['X', 'O']
        self.matriz = [[str(i)+str(ii) for ii in range(3)] for i in range(3)]
        self.xGanhou = False
        self.oGanhou = False

        self.frameCima = Frame(self)
        self.lb_vez = Label(self.frameCima, text=f'vez do {self.vez[0]}')
        self.lb_aviso = Label(self.frameCima, text='')

        self.lb_vez.grid(row=0, column=0)
        self.lb_aviso.grid(row=0, column=1)
        
        # 'freme meio' onde fica os botoes com a matriz
        self.frameMeio = Frame(self)
        
        # botoes ...
        self.bt00 = Button(self.frameMeio, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('00'))
        self.bt01 = Button(self.frameMeio, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('01'))
        self.bt02 = Button(self.frameMeio, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('02'))
        self.bt10 = Button(self.frameMeio, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('10'))
        self.bt11 = Button(self.frameMeio, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('11'))
        self.bt12 = Button(self.frameMeio, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('12'))
        self.bt20 = Button(self.frameMeio, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('20'))
        self.bt21 = Button(self.frameMeio, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('21'))
        self.bt22 = Button(self.frameMeio, width=10, height=5, font='arial 15 bold', command=lambda : self.marcar('22'))
        
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
        
        # colocando as frames
        self.frameCima.pack()
        self.frameMeio.pack()
        
    def marcar(self, opcao):
        if opcao == '00':
            print(00)
            self.bt00.config(state=DISABLED, text=self.vez[0], disabledforeground=self.colorirBts())
            self.matriz = uteis.colocar(self.vez[0], 0, 0, self.matriz)
            
        if opcao == '01':
            self.bt01.config(state=DISABLED, text=self.vez[0], disabledforeground=self.colorirBts())
            self.matriz = uteis.colocar(self.vez[0], 0, 1, self.matriz)

        if opcao == '02':
            self.bt02.config(state=DISABLED, text=self.vez[0], disabledforeground=self.colorirBts())
            self.matriz = uteis.colocar(self.vez[0], 0, 2, self.matriz)

        if opcao == '10':
            self.bt10.config(state=DISABLED, text=self.vez[0], disabledforeground=self.colorirBts())
            self.matriz = uteis.colocar(self.vez[0], 1, 0, self.matriz)

        if opcao == '11':
            self.bt11.config(state=DISABLED, text=self.vez[0], disabledforeground=self.colorirBts())
            self.matriz = uteis.colocar(self.vez[0], 1, 1, self.matriz)

        if opcao == '12':
            self.bt12.config(state=DISABLED, text=self.vez[0], disabledforeground=self.colorirBts())
            self.matriz = uteis.colocar(self.vez[0], 1, 2, self.matriz)
            
        if opcao == '20':
            self.bt20.config(state=DISABLED, text=self.vez[0], disabledforeground=self.colorirBts())
            self.matriz = uteis.colocar(self.vez[0], 2, 0, self.matriz)

        if opcao == '21':
            self.bt21.config(state=DISABLED, text=self.vez[0], disabledforeground=self.colorirBts())
            self.matriz = uteis.colocar(self.vez[0], 2, 1, self.matriz)

        if opcao == '22':
            self.bt22.config(state=DISABLED, text=self.vez[0], disabledforeground=self.colorirBts())
            self.matriz = uteis.colocar(self.vez[0], 2, 2, self.matriz)

        
        uteis.mostrar(self.matriz)
        self.xGanhou, self.oGanhou = uteis.verificarXO(self.matriz)
        
        if self.xGanhou:
            self.lb_aviso.config(text='X venceu')
            self.lb_vez.config(text='')
            self.desativar_TdsBts()
            
        elif self.oGanhou:
            self.lb_aviso.config(text='O venceu')
            self.lb_vez.config(text='')
            self.desativar_TdsBts()

        else:
            self.MudarVez()

    def MudarVez(self):
        # mudando a vez  
        self.vez.reverse()
        self.lb_vez.config(text=f'vez do {self.vez[0]}')
    
    def colorirBts(self):
        if self.vez[0] == 'X':
            return 'red'
        else:
            return 'blue'
    # desativar todos os botoes
    def desativar_TdsBts(self):
        self.bt00.config(state=DISABLED)
        self.bt01.config(state=DISABLED)
        self.bt02.config(state=DISABLED)
        self.bt10.config(state=DISABLED)
        self.bt11.config(state=DISABLED)
        self.bt12.config(state=DISABLED)
        self.bt20.config(state=DISABLED)
        self.bt21.config(state=DISABLED)
        self.bt22.config(state=DISABLED)

        
        
        
if __name__ == '__main__':
    root = Tk()
    interface = Interface(root)
    interface.pack()
    root.mainloop()