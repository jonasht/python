from tkinter import CENTER, TOP, Tk, ttk
from fr_play import Fr_play


class App(Tk):
    def __init__(self):
        super().__init__()
   
        # chamando frames 
        self.fr_play = Fr_play(self, self)

        self.fr = ttk.Frame(self)

        self.lb_qtd = ttk.Label(self.fr, text='Quantidade de Cartas:')
        self.et_qtd = ttk.Entry(self.fr)

        self.bt_start = ttk.Button(self.fr, text='Iniciar', command=self.toStart)

        self.lb_qtd.grid(row=0,column=0)
        self.et_qtd.grid(row=0,column=1)

        self.bt_start.grid(row=1,column=1)
        
        self.fr.pack(anchor=CENTER)
    def toStart(self):
        self.fr_play.tkraise()

        # fr = Fr_play(app)
        # fr.pack(anchor=CENTER)

        

def main():
    app = App()
    app.geometry('1800x1000')
    app.bind('q', lambda x: app.destroy())
    app.bind('<Escape>', lambda x: app.destroy())
    app.mainloop()    
        
if __name__ == '__main__':
    main()

