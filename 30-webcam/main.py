from tkinter import *
import ttkbootstrap as ttk
from PIL import Image, ImageTk
import cv2

class fr_webcam(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.label = ttk.Label(self)
        self.label.frame_num = 0
        self.label.grid(row=0, column=0)
        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            print("Cannot open camera")
            exit()

        self.show_frames()
        self.bind("p", self.key_pressed)
        
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
        file_name = f"{self.label.frame_num}.png"
        imagetk = self.label.imgtk
        imgpil = ImageTk.getimage( imagetk )
        imgpil.save(file_name, "PNG")
        imgpil.close()

window = ttk.Window()
frame = fr_webcam(window)
frame.pack()
window.mainloop()