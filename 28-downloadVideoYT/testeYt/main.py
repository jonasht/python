import ttkbootstrap as ttk
from pytube import YouTube
from ttkbootstrap.constants import *
import utilTest as util

from PIL import Image, ImageTk

class Fr_videos(ttk.Frame):
    def __init__(self, parent, link) -> None:
        super().__init__(parent)
        self.yt = YouTube(link)
        
        self.yt_title = self.yt.title
        util.download_image(thumbnail_url=self.yt.thumbnail_url, name=self.yt_title)

        self.image = Image.open(f'./video_image/{self.yt_title}.jpg')
        self.image = self.image.resize((180, 100), Image.LANCZOS)

        self.imageTk = ImageTk.PhotoImage(self.image) 

        self.lb_image = ttk.Label(self, image=self.imageTk)

        self.title1 = ttk.Label(self, text='title:')
        self.title2 = ttk.Label(self, text=self.yt_title)
        self.progressBar = ttk.Progressbar(self, length=400)
        



        self.title1.grid(row=0, column=0)
        self.title2.grid(row=0, column=1)
        self.lb_image.grid(row=1, column=0, columnspan=2, sticky=W)
        self.progressBar.grid(row=2, column=0, columnspan=2)

    def startDownload(self):
        video = self.yt.streams.get_highest_resolution()
        video.download()
        
        print('start download')
        

        
if __name__ == '__main__':
    window = ttk.Window()
    link = 'https://www.youtube.com/watch?v=_p2NvO6KrBs'
    fr = Fr_videos(window, link)
    fr.pack()
    bt_download = ttk.Button(window, text='Download', bootstyle=SUCCESS, command=lambda: fr.startDownload())
    bt_download.pack()
    
    window.bind('q', lambda x: window.quit())
    window.place_window_center()
    window.style.theme_use('cyborg')
    window.geometry('500x300')
    window.mainloop()