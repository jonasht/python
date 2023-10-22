import ttkbootstrap as ttk
from pytube import YouTube
from ttkbootstrap.constants import *
import utilTest as util
from threading import Thread
from os import system


from PIL import Image, ImageTk

# =- delete all .mp4 and .jpg
system('rm *.mp4')
system('rm video_image/*.jpg')


class Fr_videos(ttk.Frame):
    def __init__(self, parent, link) -> None:
        super().__init__(parent)
        self.yt = YouTube(link, on_progress_callback=self.progress)
        
        self.yt_title = self.yt.title
        util.download_image(thumbnail_url=self.yt.thumbnail_url, name=self.yt_title)

        self.image = Image.open(f'./video_image/{self.yt_title}.jpg')
        self.image = self.image.resize((180, 100), Image.LANCZOS)

        self.imageTk = ImageTk.PhotoImage(self.image) 

        self.lb_image = ttk.Label(self, image=self.imageTk)

        self.title1 = ttk.Label(self, text='title:')
        self.title2 = ttk.Label(self, text=self.yt_title)
        self.progressBar = ttk.Progressbar(self, length=300, maximum=100, mode=DETERMINATE, value=0)
        



        self.lb_image.grid(row=0, column=0, rowspan=2)
        self.title1.grid(row=0, column=1)
        self.title2.grid(row=0, column=2)
        self.progressBar.grid(row=1, column=1, columnspan=2)


    # def progress(self, n1, n2, n3):
    def progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percent = int(bytes_downloaded / total_size * 100)

        self.progressBar.config(value=percent)
        self.progressBar.update()
        
        if percent == 100:
            self.progressBar.config(bootstyle=SUCCESS,)


    
    def startDownload(self):
        print('start download')
        video = self.yt.streams.get_highest_resolution()
        video.download()
    
    
        

        
if __name__ == '__main__':


    def start():
        
        th1 = Thread(target=fr1.startDownload())
        th2 = Thread(target=fr2.startDownload())
        th3 = Thread(target=fr3.startDownload())  
        th1.start()
        th2.start()
        th3.start()
        
    window = ttk.Window()
    link1 = 'https://www.youtube.com/watch?v=_p2NvO6KrBs'
    link2 = 'https://www.youtube.com/watch?v=ZQ80_j3CXJQ'
    link3 = 'https://www.youtube.com/watch?v=ytIZGsm1NXo'

    fr1 = Fr_videos(window, link1)
    fr2 = Fr_videos(window, link2)
    fr3 = Fr_videos(window, link3)
    fr1.pack(ipadx=200)
    fr2.pack(ipadx=200)
    fr3.pack(ipadx=200)
    
    bt_download = ttk.Button(window, text='Download', bootstyle=SUCCESS, command=start)
    bt_download.pack()
    
    window.bind('q', lambda x: window.quit())
    window.place_window_center()
    window.style.theme_use('cyborg')
    # window.geometry('500x300')
    window.mainloop()