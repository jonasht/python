from tkinter import *


class FrameMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        
        self.opcaoMenu = Frame(self)
        
        self.bt_start = Button(self, text='Start', font='arial 20', command=lambda: controller.show_frame('FrameStart'))
        self.valor = IntVar()

        self.lb_op = Label(self.opcaoMenu, text='qual tabuada?:')
        self.lb_op.pack()



        # ======= radio Button ===========================================
        # radio button das opcao para escolher
        self.rbt1 = Radiobutton(self.opcaoMenu, text='1', variable=self.valor, value=1, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt2 = Radiobutton(self.opcaoMenu, text='2', variable=self.valor, value=2, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt3 = Radiobutton(self.opcaoMenu, text='3', variable=self.valor, value=3, indicatoron=0, padx=10, pady=10,bg='green')
        self.rbt4 = Radiobutton(self.opcaoMenu, text='4', variable=self.valor, value=4, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt5 = Radiobutton(self.opcaoMenu, text='5', variable=self.valor, value=5, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt6 = Radiobutton(self.opcaoMenu, text='6', variable=self.valor, value=6, indicatoron=0, padx=10, pady=10,bg='green')
        self.rbt7 = Radiobutton(self.opcaoMenu, text='7', variable=self.valor, value=7, indicatoron=0, padx=10, pady=10,bg='green')
        self.rbt8 = Radiobutton(self.opcaoMenu, text='8', variable=self.valor, value=8, indicatoron=0, padx=10, pady=10,bg='green')
        self.rbt9 = Radiobutton(self.opcaoMenu, text='9', variable=self.valor, value=9, indicatoron=0, padx=10, pady=10, bg='green')

        self.rbt1.pack (side=LEFT)
        self.rbt2.pack (side=LEFT)
        self.rbt3.pack (side=LEFT)
        self.rbt4.pack (side=LEFT)
        self.rbt5.pack (side=LEFT)
        self.rbt6.pack (side=LEFT)
        self.rbt7.pack (side=LEFT)
        self.rbt8.pack (side=LEFT)
        self.rbt9.pack (side=LEFT)

        self.rbt9.select()
    
        self.opcaoMenu.pack(anchor=CENTER, padx=10, pady=20)
        self.bt_start.pack(anchor=CENTER)

if __name__ == '__main__':
    import main

    # root = Tk()
    # frame = FrameMenu(root)
    # def tecla1(event):
    #     print('1 apertado')
    #     frame.rbt1.select()
    # def tecla2(event):
    #     print('2 apertado')
    #     frame.rbt2.select()

    # root.bind('1', tecla1)
    # root.bind('2', tecla2)
    # frame.pack()
    
    # root.mainloop()
