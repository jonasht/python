from tkinter import ttk
import tkinter as tk

from PIL import Image, ImageTk
 

class Fr_home(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.lb = ttk.Label(self, text='Bem Vindo')
        self.lb.grid(row=0, column=0)

        
        self.img = ImageTk.PhotoImage(Image.open("./img/bike_mania.png"), size='10x10')

        #Displaying it
        self.lb_img = ttk.Label(self, image=self.img).grid(row=1, column=0)        
        


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1200x800')
    frame = Fr_home(root)
    frame.pack()
    root.mainloop()
