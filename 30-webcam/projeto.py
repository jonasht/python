import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import Image, ImageTk
import cv2
import random as rd

class Fr_webcam(ttk.Frame):
    def __init__(self, parent, controller=None) -> None:
        super().__init__(parent)
        self.controller = controller

        self.label = ttk.Label(self)
        self.label.frame_num = 0
        self.label.grid(row=0, column=0)
        self.cap = cv2.VideoCapture(0)


        self.show_frames()
        # self.bind("p", self.key_pressed)
        
        self.bt_photo = ttk.Button(self, text='tirar foto', command=self.take_pic)
        self.bt_photo.grid()
        
        

    def show_frames(self):
        cv2image= cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image = img)
        self.label.imgtk = imgtk
        self.label.frame_num += 1.
        self.label.configure(image=imgtk)
        self.label.after(20, self.show_frames)

    def key_pressed(self, event):
        self.take_pic()

    def take_pic(self):
        # file_name = f"{self.label.frame_num}.png"
        # imagetk = self.label.imgtk
        # imgpil = ImageTk.getimage( imagetk )
        # imgpil.save(file_name, "PNG")
        # imgpil.close()
        imageTk = self.label.imgtk
        pil_img = ImageTk.getimage(imageTk)
        self.controller.fr_photo.set_image(pil_img)
        
        
class Fr_photo(ttk.Frame):
    def __init__(self, parent, controller=None) -> None:
        super().__init__(parent)
        self.controller = controller
        
        self.image = Image.open('./images/1.png')
        self.image = self.image.resize((160, 120), Image.LANCZOS)
        
        self.tkimg = ImageTk.PhotoImage(self.image)

        self.lb_img = ttk.Label(self, image=self.tkimg)
        self.lb_img.pack()
        self.bt_save = ttk.Button(self, text='salvar foto', command=self.save_photo)
        self.bt_save.config(padding=50)
        self.bt_save.pack()
    def set_image(self, pil_image):
        self.image = pil_image
        # self.image = self.image.resize((160, 120), Image.LANCZOS)
        self.tkimg = ImageTk.PhotoImage(self.image)
        self.lb_img.configure(image=self.tkimg)
        
    def save_photo(self, id=rd.randint(1, 20)):
        file_name = f"{id}.png"
        # imagetk = self.label.imgtk
        imageTk = self.tkimg
        imgpil = ImageTk.getimage(imageTk)
        # imgpil = ImageTk.getimage( imagetk )
        imgpil.save(file_name, 'PNG')
        # imgpil.save(file_name, "PNG")
        imgpil.close()
        # imgpil.close()
        
class Fr_photoMain(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        
        self.container = ttk.Frame(self)
        
        self.fr_photo = Fr_photo(self.container, self)
        self.fr_webcam = Fr_webcam(self.container, self)
        self.fr_photo.grid(row=0, column=0, sticky=NSEW)
        self.fr_webcam.grid(row=0, column=0, sticky=NSEW)
        self.fr_webcam.tkraise()
        
        self.container.pack()
        # fazendo teste
        self.bt_showFr_webcam = ttk.Button(self, text='mostrar webcam', bootstyle=SUCCESS, command=self.show_frWebcam)
        self.bt_showFr_photo = ttk.Button(self, text='mostrar foto', bootstyle=WARNING, command=self.show_frPhoto)
        
        self.bt_showFr_webcam.pack(side=LEFT, anchor=S, fill=X, expand=True)
        self.bt_showFr_photo.pack(side=RIGHT, anchor=S, fill=X, expand=True)

    def show_frPhoto(self):
        self.fr_photo.tkraise()

    def show_frWebcam(self):
        self.fr_webcam.tkraise()

if __name__ == '__main__':
        
    window = ttk.Window()
    window.style.theme_use('darkly')
    frame = Fr_photoMain(window)
    frame.pack(fill=BOTH, expand=True)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    
    
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(f'{width}x{height}')
    window.bind('q', lambda x: window.quit())
    
    window.mainloop()