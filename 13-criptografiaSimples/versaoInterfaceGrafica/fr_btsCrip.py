from tkinter import *
from tkinter import ttk

class Fr_btsCrip(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con

        
        self.bt_cri = ttk.Button(self, text='Criptografar', command=self.criptografar)
        self.bt_copy = ttk.Button(self, text='Copiar', command=self.copiar)
        self.bt_paste = ttk.Button(self, text='Colar', command=self.colar)

        self.bt_del = ttk.Button(self, text='apagar', command=self.deletar)       
        
        self.bt_cri.grid(row=0, column=0, columnspan=2, sticky=EW, pady=3, padx=3, ipadx=60)
        self.bt_copy.grid(row=1, column=0, sticky=EW, pady=3, padx=3)
        self.bt_paste.grid(row=1, column=1, sticky=EW, pady=3, padx=3)
        self.bt_del.grid(row=2, column=0, pady=3, padx=3, columnspan=2, sticky=EW)

    def criptografar(self):
        self.con.criptar()
        
    def copiar(self):
        pass
    def colar(self):
        pass
    def deletar(self):
        self.con.del_txt1()

if __name__ == '__main__':
    app = Tk()


    # Create a style
    style = ttk.Style(app)

    # Import the tcl file
    app.tk.call('source', './forest_ttk_theme/forest-dark.tcl')

    # Set the theme with the theme_use method
    style.theme_use("forest-dark")

    fr = Fr_btsCrip(app, app)
    fr.grid(sticky=NSEW)
    fr.config(border=20)
    fr.bt_cri.config(width=30)
    from sys import exit
    app.bind('q', exit)

    app.mainloop()
