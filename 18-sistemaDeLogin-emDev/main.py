from tkinter import *                
from tkinter import font as tkfont  
from frAcesso import FrAcesso
from frLogin import FrLogin
from frCadastro import FrCadastro


class Principal(Tk):
    
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FrLogin, FrAcesso, FrCadastro):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('FrLogin') 
        

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()




if __name__ == "__main__":
    root = Principal()
    root.geometry('400x300')
    root.mainloop()
    