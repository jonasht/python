
import tkinter as tk               
from tkinter import font as tkfont  
from tkinter import ttk
from tkinter.constants import DISABLED, END, NORMAL

import uteis as u



class Principal(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.lb = ttk.Label(text='texto:')
        self.lb.pack()
        
        self.txt = tk.Text(self)
        self.txt.pack()

        self.bt = ttk.Button(self, text='ok', command=self.evento)
        self.bt.pack()
        
        self.txt.insert(END, u.get_msg('jonas'))

    def evento(self):
        print('evento')
        msg = self.txt.get('1.0', END)
        print(msg)
        self.txt.config(state=DISABLED)
        
        print('estado do txt:', self.txt['state'])
        if self.txt['state']  == DISABLED:
            self.txt.config(state=NORMAL)
            print('if: estado do txt:', self.txt['state'])
            
        elif self.txt['state'] == NORMAL:
            print('elif: estado do txt:', self.txt['state'])
            
            self.txt.config(state=DISABLED)
        

        
if __name__ == "__main__":
    root = Principal()
    root.geometry('400x500')
    root.mainloop()
    # NOME = 'jonas'
    # u.update_msg(NOME, 'alog algo adf\nadsfdaf\nsdafasdf')
    # print(u.get_msg(NOME))
    
    