import ttkbootstrap as ttk
from pytube import YouTube
from ttkbootstrap.constants import *
import utilTest as util
from threading import Thread
from os import system


from PIL import Image, ImageTk

# =- delete all .mp4 and .jpg
# system('rm video_image/*.jpg')


class Fr_videos(ttk.Frame):
    def __init__(self, parent, link) -> None:
        super().__init__(parent)
        self.yt = YouTube(link)
        self.link = link

        self.yt_title = self.yt.title
        # util.download_image(thumbnail_url=self.yt.thumbnail_url, name=self.yt_title)

        self.image = Image.open(f'./video_image/{self.yt_title}.jpg')
        self.image = self.image.resize((180, 100), Image.LANCZOS)

        self.imageTk = ImageTk.PhotoImage(self.image) 

        self.lb_image = ttk.Label(self, image=self.imageTk)

        self.title2 = ttk.Label(self, text=self.yt_title)
        self.progressBar = ttk.Progressbar(self, length=300, maximum=100, mode=DETERMINATE, value=0)
        
        # size_video = self.yt.streams.get_by_itag(17).filesize
        
        self.var_cb = ttk.StringVar()
        self.cb = ttk.Combobox(self,textvariable=self.var_cb,state=READONLY, bootstyle=SUCCESS,)
        filesize_high = 31408912
        filesize_high = util.format_bytes(filesize_high)
        
        filesize_low = 16608912
        filesize_low = util.format_bytes(filesize_low)
        self.cb_values = list()
        self.cb_values.append(f'{filesize_high} high')
        self.cb_values.append(f'{filesize_low} low')
        
        self.cb.config(values=self.cb_values)
        self.cb.set(self.cb_values[0])
        
        self.lb_size = ttk.Label(self, text=f'size:{filesize_high}')



        self.lb_image.grid(row=0, column=0, rowspan=4)
        self.title2.grid(row=0, column=1)
        # self.lb_size.grid(row=1, column=1)
        self.cb.grid(row=1, column=1)
        self.progressBar.grid(row=3, column=1, columnspan=2)


    def progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percent = int(bytes_downloaded / total_size * 100)

        self.progressBar.config(value=percent)
        self.progressBar.update()
        
        if percent == 100:
            self.progressBar.config(bootstyle=SUCCESS,)


    
    def startDownload(self):
        yt = YouTube(self.link, on_progress_callback=self.progress)

        video = yt.streams.get_highest_resolution()
        video.download()
        
    def start(self):
        th = Thread(target=self.startDownload)
        th.start()
    
    

        
    
    
        

        
if __name__ == '__main__':


    def start():
        
        fr1.start()
        # fr2.start()
        # fr3.startDownload()  

    window = ttk.Window()
    link1 = 'https://www.youtube.com/watch?v=_p2NvO6KrBs'
    link2 = 'https://www.youtube.com/watch?v=ZQ80_j3CXJQ'
    # link3 = 'https://www.youtube.com/watch?v=ytIZGsm1NXo'

    fr1 = Fr_videos(window, link1)
    # fr2 = Fr_videos(window, link2)
    # fr3 = Fr_videos(window, link3)
    fr1.pack(ipadx=200)
    # fr2.pack(ipadx=200)
    # fr3.pack(ipadx=200)
    
    bt_download = ttk.Button(window, text='Download', bootstyle=SUCCESS, command=start)
    bt_download.pack()
    
    window.bind('q', lambda x: window.quit())
    window.place_window_center()
    window.style.theme_use('cyborg')
    # window.geometry('500x300')
    window.mainloop()