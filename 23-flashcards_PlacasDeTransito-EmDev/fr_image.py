from tkinter import EW, Tk, ttk
from PIL import ImageTk, Image





class Fr_image(ttk.Frame):
    def __init__(self, parent, con, resize:tuple=(200, 200)):
        super().__init__(parent)
        self.resize = resize
        self.con = con
        
        self.img = ttk.Label(self, image='')
        self.img.grid(row=0, column=0, sticky=EW, columnspan=1)

    def display(self, imageName):
        
        path = f'./placasDeTransito/{imageName}.jpg'
        
        self.load = Image.open(path)
        self.resize_img = self.load.resize(self.resize)
        
        self.render = ImageTk.PhotoImage(self.resize_img)
        
        self.img.config(image=self.render)






if __name__ == '__main__':
    app = Tk()
    
    def teste():
        fr.display('R-2')
        
    fr = Fr_image(app, None)
    fr.pack()
    fr.display('R-1')
    app.bind('q', lambda x: app.destroy())
    app.bind('<Escape>', lambda x: app.destroy())
    
    ttk.Button(app, text='teste', command=teste).pack()

    app.geometry('500x500')
    app.mainloop()
    
