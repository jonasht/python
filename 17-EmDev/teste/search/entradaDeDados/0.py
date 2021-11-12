from tkinter import Button, Frame, ttk
import tkinter as tk
from tkinter.constants import DISABLED, LEFT, NORMAL, RIGHT


class Fr(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent)
        self.frame_esquerda = ttk.Frame(self)
        self.frame_direita = ttk.Frame(self)

        self.bt1 = ttk.Button(self.frame_esquerda, text='1', command=lambda: self.bt_event(1))
        self.bt2 = ttk.Button(self.frame_esquerda, text='2', command=lambda: self.bt_event(2))
        self.bt3 = ttk.Button(self.frame_esquerda, text='3', command=lambda: self.bt_event(3))

        self.bt1.pack()
        self.bt2.pack()
        self.bt3.pack()
        
        self.etd = ttk.Entry(self.frame_direita)
        self.bt_editar = Button(self.frame_direita, text='editar', command=self.bt_editarEvent)

        self.etd.pack()
        self.bt_editar.pack()

        self.frame_esquerda.pack(side=LEFT)
        self.frame_direita.pack(side=RIGHT)
        
        # self.etd.config(state=NORMAL)
    def bt_event(self, event):
        event = str(event)
        print(event)
        
    def mostrar_etd(self):
        pass
    def deletar_etd(self):
        pass
    def bt_editarEvent(self):
        print(self.etd['state'], 'tipo:', type(self.etd['state']))
        if str(self.etd['state']) == NORMAL:
            print('if disabled', self.etd['state'])
            self.etd.config(state=DISABLED)
        
        else:
            print('if normal', self.etd['state'])
            
            self.etd.config(state=NORMAL)
            
    
root = tk.Tk()
root.geometry('500x500')

fr = Fr(root)
fr.pack()
root.mainloop()
