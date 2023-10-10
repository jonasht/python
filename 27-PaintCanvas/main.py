from ttkbootstrap import Window
import ttkbootstrap as ttk 
from ttkbootstrap.constants import *


class App(Window):
    def __init__(self):
        super().__init__()

        self.scV = ttk.Scrollbar(self, orient=VERTICAL)
        self.scH = ttk.Scrollbar(self, orient=HORIZONTAL)
        
        self.canvas = ttk.Canvas(self, scrollregion=(0, 0, 1000, 1000),
                                 yscrollcommand=self.scV.set, xscrollcommand=self.scH.set)

        self.scH[COMMAND] = self.canvas.xview
        self.scV[COMMAND] = self.canvas.yview

        ttk.Sizegrip(self).grid(row=1, column=1, sticky=SE)

        self.canvas.grid(row=0, column=0, sticky=NSEW)
        self.scH.grid(row=1, column=0, sticky=EW)
        self.scV.grid(row=0, column=1, sticky=NS)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.lastx, self.lasty = 0, 0

        self.canvas.bind('<Button-1>', self.xy)
        self.canvas.bind('<B1-Motion>', self.addLine)
        self.canvas.bind('<B1-ButtonRelease>', self.doneStroke)

        # vermelho
        self.id = self.canvas.create_rectangle((10, 10, 30, 30), fill='red', tags=('palette', 'palettered'))
        self.canvas.tag_bind(self.id, '<Button-1>', lambda x: self.set_color('red'))

        # azul
        self.id = self.canvas.create_rectangle((10, 35, 30, 55), fill='blue', tags=('palette', 'paletteblue'))
        self.canvas.tag_bind(self.id, '<Button-1>', lambda x: self.set_color('blue'))

        # preto 
        self.id = self.canvas.create_rectangle((10, 60, 30, 80), fill='black', tags=('palette', 'paletteblack'))
        self.canvas.tag_bind(self.id, '<Button-1>', lambda x: self.set_color('black'))

        # verde
        self.id = self.canvas.create_rectangle((10, 85, 30, 105), fill='green', tags=('palette', 'palettegreen'))
        self.canvas.tag_bind(self.id, '<Button-1>', lambda x: self.set_color('green'))
        
        # amarelo
        self.id = self.canvas.create_rectangle((10, 110, 30, 130), fill='yellow', tags=('palette', 'paletteyellow'))
        self.canvas.tag_bind(self.id, '<Button-1>', lambda x: self.set_color('yellow'))
        
        # set color default
        self.set_color('black')
        
        self.canvas.itemconfig('palette', width=5)

    def xy(self, event):
        self.lastx, self.lasty = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
    

    def set_color(self, newColor):
        self.color = newColor
        self.canvas.dtag(ALL, 'paletteSelected')
        self.canvas.itemconfig('palette', outline='white')
        self.canvas.addtag('paletteSelected', 'withtag', 'palette%s' % self.color)
        self.canvas.itemconfig('paletteSelected', outline='#999999')


    # adiconar linha
    def addLine(self, event):
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        self.canvas.create_line((self.lastx, self.lasty, x, y), fill=self.color, width=10, tags='currentline')
        self.lastx, self.lasty = x, y


    # func para quebrar o desenho
    def doneStroke(self, event):
        self.canvas.itemconfigure('currentline', width=10)



def main():
    
    app = App()
    app.title('Paint canvas')
    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()
    app.geometry(f'{width}x{height}')
    app.bind('<Escape>', lambda x: app.quit())
    
    app.mainloop()
if __name__ == '__main__':
    main()