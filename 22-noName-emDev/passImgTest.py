from tkinter import CENTER, EW, LEFT, RIGHT, Tk, ttk
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
        load = Image.open(c)
        resize_img = load.resize((200, 200))
        render = ImageTk.PhotoImage(resize_img)
        self.img.config(image=render)




class App(Tk):
    def __init__(self) -> None:
        super().__init__()
        ttk.Label(self, text='teste').pack()
        self.contador = 0
        self.dir_imgList = read_dir()
        
        
        self.fr_img = Fr(self, self)
        self.fr_img.pack()

        # botoes 
        self.bt1 = ttk.Button(self, text='<<<')
        self.bt2 = ttk.Button(self, text='>>>', command=self.toRight)
        
        self.bt1.pack(side=LEFT)
        self.bt2.pack(side=RIGHT)        
    
    def toRight(self):
        nome_dir = self.dir_imgList[self.contador]
        self.fr_img.mostrar(nome_dir)
        print('nome_dir:', nome_dir)
        self.contador += 1

    
if __name__ == '__main__':
    app = App()
    app.geometry('500x500')
    app.mainloop()
    print(placaList)
