from lib2to3.pgen2 import token
from tkinter import *
from tkinter import ttk
import uteis as u



class Fr(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.txt1 = Text(self)
        self.txt2 = Text(self)
        self.key_etd = ttk.Entry(self)
        self.bt_delTxt1 = ttk.Button(self, text='deletar criptografar', command=self.del_txt1)
        self.bt_delTxt2 = ttk.Button(self, text='deletar descriptografar', command=self.del_txt2)
        self.bt_delEtd = ttk.Button(self, text='delatar key', command=self.del_etd)

        self.bt_criptar = ttk.Button(self, text='Criptografar', command=self.criptar)
        self.bt_descriptar = ttk.Button(self, text='Descriptografar', command=self.descriptar)

        # colocando widgets
        self.txt1.grid(row=0, column=0)
        self.txt2.grid(row=0, column=1)
        self.key_etd.grid(row=1, column=0)
        self.bt_delEtd.grid(row=1, column=1)
        self.bt_criptar.grid(row=2, column=0)
        self.bt_descriptar.grid(row=2, column=1)
        self.bt_delTxt1.grid(row=3, column=0)
        self.bt_delTxt2.grid(row=3, column=1)

    def criptar(self):
        txt = self.txt1.get(1.0, END)
        print(txt)
        key, token = u.criptar(txt)
        print(key)
        print(token)

        self.del_txt2()
        self.txt2.insert(END, token)
        self.del_etd()
        self.key_etd.insert(0, key)

    def del_etd(self):
        self.key_etd.delete(0, END)
    def del_txt1(self):
        self.txt1.delete(0.1, END)
    
    def del_txt2(self):
        self.txt2.delete(0.1, END)

        
    def descriptar(self):
        txt = self.txt2.get(1.0, END)
        key = self.key_etd.get()
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
    Fr(app).pack()
    from sys import exit
    app.bind('q', exit)

    app.mainloop()