from tkinter import Label, ttk
import tkinter as tk

from PIL import Image, ImageTk
 

class Fr_home(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.lb = ttk.Label(self, text='teste')
        self.lb.pack()

        self.lb_img = Label(self)

        # self.lb_img['image'] = ImageTk.PhotoImage(Image.open('./img/bike_mania.png'))
        self.lb_img.config(image=ImageTk.PhotoImage(Image.open('./img/bike_mania.png')))

        self.lb_img.pack()

        python_image = tk.PhotoImage(file='./img/bike_mania.png')
        ttk.Label(self, image=python_image).pack()
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('1200x800')
    frame = Fr_home(root)
    frame.pack()
    root.mainloop()
