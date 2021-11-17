import tkinter as tk
from tkinter import ttk
from tkinter.constants import LEFT, RIGHT
from frame1 import Fr1
from frame2 import Fr2


class Principal(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)



        self.frame_left = tk.Frame(self)
        self.frame_right = tk.Frame(self)
        

        # self.frames = {}
        # for F in (StartPage, PageOne, PageTwo):
        #     page_name = F.__name__
        #     frame = F(parent=container, controller=self)
        #     self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            # frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame("StartPage")
        
        self.fr1 = Fr1(parent=self.frame_left, controller=self)
        self.fr1.grid()
        
        self.fr2 = Fr2(parent=self.frame_right, controller=self)
        self.fr2.grid()

        self.frame_left.pack(side=LEFT)
        self.frame_right.pack(side=RIGHT)

        
    def mostrar_dados(self, dados):
        print('dados main:', dados)
        self.fr2.inserir(dados)
    # def show_frame(self, page_name):
    #     '''Show a frame for the given page name'''
    #     frame = self.frames[page_name]
    #     frame.tkraise()

root = Principal()
root.mainloop()