from tkinter import *
import tkinter



class FrAcesso(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller


        self.bt_logout = Button(self, text='log out', command=self.logout)
        self.bt_logout.pack()
        
        self.lb = Label(self, text='conta acessada')
        self.lb.pack()

    def logout(self):
        self.controller.show_frame('FrLogin')

        


if __name__ == '__main__':
    from main import Principal
    root = Principal()
    root.mainloop()