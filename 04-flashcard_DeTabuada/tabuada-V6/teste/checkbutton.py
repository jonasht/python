from tkinter import Tk, IntVar, StringVar, BooleanVar, DoubleVar
# from tkinter.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *





class Fr (ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lb = ttk.Label(self, text='isso so eh um teste')
        self.lb.pack()
        
        self.fr = ttk.Frame(self)
        
        self.var_1 = BooleanVar()
        self.var_2 = BooleanVar()
        self.var_3 = BooleanVar()
        self.var_4 = BooleanVar()
        self.var_5 = BooleanVar()
        self.var_6 = BooleanVar()
        self.var_7 = BooleanVar()
        self.var_8 = BooleanVar()
        self.var_9 = BooleanVar()
        
        self.chbt1 = ttk.Checkbutton(self.fr, text='1', variable=self.var_1, bootstyle=TOOLBUTTON)
        self.chbt2 = ttk.Checkbutton(self.fr, text='2', variable=self.var_2, bootstyle=TOOLBUTTON)
        self.chbt3 = ttk.Checkbutton(self.fr, text='3', variable=self.var_3, bootstyle=TOOLBUTTON)
        self.chbt4 = ttk.Checkbutton(self.fr, text='4', variable=self.var_4, bootstyle=TOOLBUTTON)
        self.chbt5 = ttk.Checkbutton(self.fr, text='5', variable=self.var_5, bootstyle=TOOLBUTTON)
        self.chbt6 = ttk.Checkbutton(self.fr, text='6', variable=self.var_6, bootstyle=TOOLBUTTON)
        self.chbt7 = ttk.Checkbutton(self.fr, text='7', variable=self.var_7, bootstyle=TOOLBUTTON)
        self.chbt8 = ttk.Checkbutton(self.fr, text='8', variable=self.var_8, bootstyle=TOOLBUTTON)
        self.chbt9 = ttk.Checkbutton(self.fr, text='9', variable=self.var_9, bootstyle=TOOLBUTTON)

        self.chbt1.grid(row=0, column=1) 
        self.chbt2.grid(row=0, column=2) 
        self.chbt3.grid(row=0, column=3) 
        self.chbt4.grid(row=0, column=4) 
        self.chbt5.grid(row=0, column=5) 
        self.chbt6.grid(row=0, column=6) 
        self.chbt7.grid(row=0, column=7) 
        self.chbt8.grid(row=0, column=8) 
        self.chbt9.grid(row=0, column=9) 

        self.fr.pack(anchor=CENTER)


        self.bt = ttk.Button(self, text='Start', command=self.bt_press)
        self.bt.pack()

        self.var_9.set(True)
        self.var_8.set(True)
        

    def bt_press(self):
        print('='*30)

        numeros = [
                    1 if self.var_1.get() else False,
                    2 if self.var_2.get() else False,
                    3 if self.var_3.get() else False,
                    4 if self.var_4.get() else False,
                    5 if self.var_5.get() else False,
                    6 if self.var_6.get() else False,
                    7 if self.var_7.get() else False,
                    8 if self.var_8.get() else False,
                    9 if self.var_9.get() else False,
                ]
        
        numeros = list(filter(lambda x: x, numeros))
        
        print(f'numeros: {numeros}')
        
        

def main():
    root = Tk()
    fr = Fr(root)
    fr.pack()
    root.bind('q', lambda x: root.destroy())
    root.bind('<Escape>', lambda x: root.destroy())
    
    width=500
    height=400



    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = screen_width//2 - width//2
    y = screen_height//2 - height//2

    
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.mainloop()



if __name__ == '__main__':
    main()
