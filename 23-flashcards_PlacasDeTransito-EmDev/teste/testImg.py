from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("./placas de transito/R-1.jpg")
        resize_img = load.resize((200, 200))
        
        render = ImageTk.PhotoImage(resize_img)
        
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

if __name__ == '__main__':        
    root = Tk()
    app = Window(root)

    root.geometry("1000x1000")
    root.mainloop()