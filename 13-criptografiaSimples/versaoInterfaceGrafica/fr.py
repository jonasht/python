from tkinter import *
from tkinter import ttk
from fr_bts1 import Fr_bts1
from fr_bts2 import Fr_bts2
from fr_key import Fr_key
import uteis as u


class Fr(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.txt1 = Text(self)
        self.txt2 = Text(self)
        
        # chamando frames
        self.fr_bts1 = Fr_bts1(self, self)
        self.fr_bts2 = Fr_bts2(self, self)
        self.fr_key = Fr_key(self, self)

        # colocando widgets =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.txt1.grid(row=1, column=0)
        self.fr_bts1.grid(row=2, column=0, sticky=NSEW, columnspan=3)
        self.fr_bts1.bt_cri.config(width=62)
        
        # key
        self.fr_key.grid(row=0, column=1)
        self.fr_key.etd.config(width=50)
        self.txt2.grid(row=1, column=1)
        self.fr_bts2.grid(row=2, column=1, sticky=NSEW, columnspan=3)
        self.fr_bts2.bt_cri.config(width=62)
        # self.fr_key.etd.insert(0, 'alfogo')

    def criptar(self):
        txt = self.txt1.get(1.0, END)
        print(txt)
        key, token = u.criptar(txt)
        print(key)
        print(token)

        self.del_txt2()
        self.txt2.insert(END, token)
        # self.del_etd()
        
        # self.key_etd.insert(0, key)
        # self.fr_key.etd.delete(0, END)
        self.fr_key.etd.insert(0, key)
        


    def del_etd(self):
        pass
        self.key_etd.delete(0, END)
        
    def del_txt1(self):
        self.txt1.delete(1.0, END)
    
    def del_txt2(self):
        self.txt2.delete(1.0, END)

        
    def descriptar(self):
        txt = self.txt2.get(1.0, END)
        # key = self.key_etd.get()
        key = self.fr_key.etd.get()
        print()
        print('key:', key)
        print('key tipo:', type(key))
        print('txt:', txt)
        print('txt tipo:', type(txt))

 
        print(txt, '\n', type(txt))

        txt = u.descriptar(key, txt)

        self.del_txt1()
        self.txt1.insert(END, txt)
        

if __name__ == '__main__':
    app = Tk()


    # Create a style
    style = ttk.Style(app)

    # Import the tcl file
    app.tk.call('source', './forest_ttk_theme/forest-dark.tcl')

    # Set the theme with the theme_use method
    style.theme_use("forest-dark")

    Fr(app).pack()
    from sys import exit
    # app.bind('q', exit)

    app.mainloop()
