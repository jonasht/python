from tkinter import CENTER, EW, LEFT, RIGHT, TOP, Tk, ttk
from PIL import ImageTk, Image
from tkinter.constants import BOTH
from nomePlacasList import nomePlaca as placaList
from readDir import read_dir


class Fr(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        
        # self.pack(fill=BOTH, expand=1)
        
        self.load = Image.open("./placasDeTransito/R-1.jpg")
        self.resize_img = self.load.resize((200, 200))
        
        self.render = ImageTk.PhotoImage(self.resize_img)
        
        self.img = ttk.Label(self, image=self.render)
        # self.img.image = self.render
        # img.place(x=0, y=0)
        self.img.grid(row=0, column=0, sticky=EW, columnspan=1)

    def mostrar(self, c):
        self.load = Image.open(c)
        self.resize_img = self.load.resize((200, 200))
        
        self.render = ImageTk.PhotoImage(self.resize_img)
        
        self.img.config(image=self.render)
        # self.img.image = self.render
        
        # img.place(x=0, y=0)
        # self.img.grid(row=0, column=0, sticky=EW, columnspan=1)



class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        ttk.Label(self, text='teste').pack()
        self.contador = 0
        self.dir_imgList = read_dir()
        
        
        self.fr_img = Fr(self, self)
        self.fr_img.pack()

        # botoes 
        self.bt_show = ttk.Button(self, text='Mostrar')

        
        
        
        # default
        self.lb_contador = ttk.Label(self, text='')
        self.lb_contador.pack(side=TOP)

        self.lb_contador.config(text=f'c: {self.contador+1}/{len(self.dir_imgList)}')

    

if __name__ == '__main__':
    app = App()
    app.geometry('500x500')
    app.mainloop()
    # print(placaList)
