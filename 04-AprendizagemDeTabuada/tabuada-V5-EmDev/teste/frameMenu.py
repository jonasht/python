from tkinter import *


class FrameMenu(Frame):
    def __init__(self, parent, controller):
        Frame().__init__(parent)
        self.controller = controller
        
        
        
        lb = Label(self, text='frame menu')
        lb.pack()
        
        bt_start = Button(self, text='start', command=lambda: controller.showFrame('OlaMundo'))
        bt_start.pack()