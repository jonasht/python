from tkinter import Tk, BooleanVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class FrameMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        
        self.fr_option = ttk.Frame(self)
        
        self.bt_start = ttk.Button(self, text='Start', width=20, command=lambda: controller.show_frame('FrameStart'))
      

        self.lb_op = ttk.Label(self.fr_option, text='Quais tabuadas?:')
        self.lb_op.grid(row=0, column=1, columnspan=9)



        # ======= radio Button ===========================================
        # radio button das opcao para escolher
        self.var_1 = BooleanVar()
        self.var_2 = BooleanVar()
        self.var_3 = BooleanVar()
        self.var_4 = BooleanVar()
        self.var_5 = BooleanVar()
        self.var_6 = BooleanVar()
        self.var_7 = BooleanVar()
        self.var_8 = BooleanVar()
        self.var_9 = BooleanVar()
        

        self.chbt1 = ttk.Checkbutton(self.fr_option, text='1', variable=self.var_1, bootstyle=TOOLBUTTON)
        self.chbt2 = ttk.Checkbutton(self.fr_option, text='2', variable=self.var_2, bootstyle=TOOLBUTTON)
        self.chbt3 = ttk.Checkbutton(self.fr_option, text='3', variable=self.var_3, bootstyle=TOOLBUTTON)
        self.chbt4 = ttk.Checkbutton(self.fr_option, text='4', variable=self.var_4, bootstyle=TOOLBUTTON)
        self.chbt5 = ttk.Checkbutton(self.fr_option, text='5', variable=self.var_5, bootstyle=TOOLBUTTON)
        self.chbt6 = ttk.Checkbutton(self.fr_option, text='6', variable=self.var_6, bootstyle=TOOLBUTTON)
        self.chbt7 = ttk.Checkbutton(self.fr_option, text='7', variable=self.var_7, bootstyle=TOOLBUTTON)
        self.chbt8 = ttk.Checkbutton(self.fr_option, text='8', variable=self.var_8, bootstyle=TOOLBUTTON)
        self.chbt9 = ttk.Checkbutton(self.fr_option, text='9', variable=self.var_9, bootstyle=TOOLBUTTON)

        self.chbt1.grid(row=1, column=1) 
        self.chbt2.grid(row=1, column=2) 
        self.chbt3.grid(row=1, column=3) 
        self.chbt4.grid(row=1, column=4) 
        self.chbt5.grid(row=1, column=5) 
        self.chbt6.grid(row=1, column=6) 
        self.chbt7.grid(row=1, column=7) 
        self.chbt8.grid(row=1, column=8) 
        self.chbt9.grid(row=1, column=9) 

        # self.chbt9.select()
    
        self.fr_option.pack(anchor=CENTER, padx=10, pady=20)

        self.bt_start.pack(anchor=CENTER)
        
    def get_numbers(self):

        numbers = [
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
        
        numbers = list(filter(lambda x: x, numbers))
        
        return numbers if numbers else [9]

if __name__ == '__main__':
    from main import main
    main()

