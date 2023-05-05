import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import os


class Fr_foto(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        
        ttk.Label(self, text='esta funcionando normalmente').pack()
        


        # self.lb_img.bind('<Double-Button>', self.botao_clicado)
        # self.lb_img.bind('<Button-1>', self.botao_clicado)
        
        self.labels = list()
        self.pil_images = list()
        self.pil_imagesTk = list()
        self.colocar_photos()
    def colocar_photos(self):
        
        for i, file in enumerate(os.listdir('./images')):
            self.pil_images.append(Image.open(f'./images/{file}'))
            
        for i, pil_image in enumerate(self.pil_images):
            self.pil_images[i] = pil_image.resize((160, 120), Image.LANCZOS)

        for i, pil_image in enumerate(self.pil_images):
            self.labels.append(ttk.Label(self, image=ImageTk.PhotoImage(pil_image)))
        
        # pack labels
        for label in self.labels:
            label.pack()
            # self.image = Image.open('./images/1.png')
            # self.image = self.image.resize((160, 120), Image.LANCZOS)
            # self.tkimg = ImageTk.PhotoImage(self.image)
# 
            # self.lb_img = ttk.Label(self, image=self.tkimg)
            # self.lb_img.pack()
    def botao_clicado(self, event):
        print(event)
        print('foto foi clicada duas vezes')

if __name__ == '__main__':
    window = ttk.Window()
    window.style.theme_use('darkly')
    frame = Fr_foto(window)
    frame.pack()
    
    # width = window.winfo_screenwidth()
    # height = window.winfo_screenheight()
    # window.geometry(f'{width}x{height}')
    window.geometry('800x800')
    window.bind('q', lambda x: window.quit())
    window.mainloop()

