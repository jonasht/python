from cgitb import text
from tkinter import LEFT, NSEW, RIGHT, Tk, ttk
from random import randint



class Fr(ttk.Frame):
    def __init__(self, parent, con, nome):
        super().__init__(parent)
        self.con = con
        self.nome = nome


        self.lb = ttk.Label(self, text=f'lb {nome}')
        self.lb.config(font='Arial 50')
        self.lb.pack()

        n_random = randint(1, 20) 
        self.lb_random = ttk.Label(self, text=n_random, font='Times 25')
        self.lb_random.pack()
        if n_random > 10:
            self.lb_random.config(foreground='red')
        else:
            self.lb_random.config(foreground='green')



class App(Tk):
    def __init__(self):
        super().__init__()
        self.contador = 0
        
        self.frs_namelist = list()
        for i in range(1, 21):
            self.frs_namelist.append(f'fr{i}')
        print(self.frs_namelist)

        self.fr_main = ttk.Frame(self)
        self.frs = {}
        for name in self.frs_namelist:
            self.frs[name] = Fr(self.fr_main, self, name)
            self.frs[name].grid(row=0, column=0, sticky=NSEW)

        self.fr_main.pack()

        self.bt1 = ttk.Button(self, text='<<<', command=self.to_left)
        self.bt2 = ttk.Button(self, text='>>>', command=self.to_right)

        self.bt1.pack(side=LEFT)
        self.bt2.pack(side=RIGHT)
        
        self.mostrar('fr1')
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
                
        self.contador -= 1
        name = self.frs_namelist[self.contador]
        self.mostrar(name)



if __name__ == '__main__':
    app = App()
    app.geometry('500x500')
    app.title('teste')
    app.mainloop()




