from tkinter import LEFT, NSEW, RIGHT, Tk, ttk
from PIL import Image, ImageTk
from random import randint, sample
from readDir import read_dir


class Fr(ttk.Frame):
    def __init__(self, parent, con, nome):
        super().__init__(parent)
        self.con = con
        self.nome = nome

# =-=7
        self.load = Image.open(self.nome)
        self.resize_img = self.load.resize((200, 200))
        
        self.render = ImageTk.PhotoImage(self.resize_img)
        
        self.img = ttk.Label(self, image=self.render)
        # self.img.image = self.render
        # img.place(x=0, y=0)
        # self.img.grid(row=0, column=0, sticky=EW, columnspan=1)
        self.img.pack()


        self.lb = ttk.Label(self, text=f'{nome}')
        self.lb.config(font='Arial 20')
        self.lb.pack()

 


class App(Tk):
    def __init__(self):
        super().__init__()
        self.contador = 0
        
        self.dirs = read_dir()
        self.frs_namelist = sample(self.dirs, 5)

        print(self.frs_namelist)

        self.fr_main = ttk.Frame(self)
        self.frs = {}
        for i, name in enumerate(self.frs_namelist):
            self.frs[name] = Fr(self.fr_main, self, name)
            self.frs[name].grid(row=0, column=0, sticky=NSEW)

        self.fr_main.pack()

        self.bt1 = ttk.Button(self, text='<<<', command=self.to_left)
        self.bt2 = ttk.Button(self, text='>>>', command=self.to_right)

        self.bt1.pack(side=LEFT)
        self.bt2.pack(side=RIGHT)
        
        self.mostrar(self.frs_namelist[0])
        
        
    def mostrar(self, fr_name):
        self.frs[fr_name].tkraise()


    def to_right(self):
        if self.contador < (len(self.frs_namelist)-1):
            self.contador += 1
        else:
            self.contador = 0
            
        name = self.frs_namelist[self.contador]
        self.mostrar(name)

    
    def to_left(self):

        if self.contador > 0:
            self.contador -= 1
        else:
            self.contador = 0

        name = self.frs_namelist[self.contador]
        self.mostrar(name)



if __name__ == '__main__':
    app = App()
    app.geometry('500x500')
    app.title('teste')
    app.mainloop()




