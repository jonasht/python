from tkinter import *


class OlaMundo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        lb = Label(self, text='ola mundo')
        lb.pack()
        bt_voltar = Button(self, text='voltar', command=lambda: controller.showFrame('FrameMenu'))
        bt_voltar.pack()