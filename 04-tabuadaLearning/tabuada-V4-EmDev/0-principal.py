from tkinter import *
from conta import Conta
from interfaceStart import FrameStart
from time import sleep

print('feito no linux')

class Tabuada(Tk):
    def __init__(self):
        super().__init__()
        self.title('FTabuada v4')
        self.geometry('500x500')
        
    
        self.bt_start = Button(self, text='start', command=self.Start, font='arial 20')

        self.frame_op = Frame(self)
        self.frame_op.grid(row=0, column=0, columnspan=3, sticky=W+E)

        self.valor = IntVar()

        self.lb_op = Label(self.frame_op, text='qual tabuada?:')
        self.lb_op.grid(row=0)


        self.rbt1 = Radiobutton(self.frame_op, text='1', variable=self.valor, value=1, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt1.grid(row=0, column=1)

        self.rbt2 = Radiobutton(self.frame_op, text='2', variable=self.valor, value=2, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt2.grid(row=0, column=2)

        self.rbt3 = Radiobutton(self.frame_op, text='3', variable=self.valor, value=3, indicatoron=0, padx=10, pady=10,bg='green')
        self.rbt3.grid(row=0, column=3)

        self.rbt4 = Radiobutton(self.frame_op, text='4', variable=self.valor, value=4, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt4.grid(row=0, column=4)

        self.rbt5 = Radiobutton(self.frame_op, text='5', variable=self.valor, value=5, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt5.grid(row=0, column=5)

        self.rbt6 = Radiobutton(self.frame_op, text='6', variable=self.valor, value=6, indicatoron=0, padx=10, pady=10,
                        bg='green')
        self.rbt6.grid(row=0, column=6)

        self.rbt7 = Radiobutton(self.frame_op, text='7', variable=self.valor, value=7, indicatoron=0, padx=10, pady=10,
                        bg='green')

        self.rbt7.grid(row=0, column=7)
        self.rbt8 = Radiobutton(self.frame_op, text='8', variable=self.valor, value=8, indicatoron=0, padx=10, pady=10,
                        bg='green')

        self.rbt8.grid(row=0, column=8)
        self.rbt9 = Radiobutton(self.frame_op, text='9', variable=self.valor, value=9, indicatoron=0, padx=10, pady=10, bg='green')

        self.rbt9.grid(row=0, column=9)
        self.rbt10 = Radiobutton(self.frame_op, text='10', variable=self.valor, value=10, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt10.grid(row=0, column=10)

        self.rbt9.select()

        
        self.bt_start.grid(row=5, columnspan=3, sticky=W+E)


    def Start(self):  


        frameStart = FrameStart(self)
        frameStart.grid()
        frameStart.iniciar(self.valor.get())
    



if __name__ == '__main__':
    root = Tabuada()
    root.mainloop()