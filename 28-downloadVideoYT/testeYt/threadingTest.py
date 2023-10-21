import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from time import sleep
from threading import Thread

class Fr_ (ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.sleep_time = 0
        
        
        self.lb_load = ttk.Label(self, text='')
        self.progressbar = ttk.Progressbar(self, length=400, maximum=100, mode=DETERMINATE)

        
        self.lb_load.grid(row=0, column=1)
        self.progressbar.grid(row=0, column=0)
        self.progressbar.config(bootstyle=WARNING)
    def loading(self):
        for i in range(1, 101):
            self.progressbar.config(value=i)
            sleep(self.sleep_time)
            self.lb_load.config(text=f'{i}% loading', bootstyle=WARNING)
            self.progressbar.update()
            
        per = self.progressbar['value']
        if per >= 100:
            self.progressbar.config(bootstyle=SUCCESS,)
            self.lb_load.config(text=f'100% completed', bootstyle=SUCCESS)

        # self.progressbar.config(value=100, bootstyle=SUCCESS)
        # self.progressbar.update()

    def start(self):
        th = Thread(target=self.loading)
        th.start()

if __name__ == '__main__':
    def start():
        fr1.start()
        fr2.start()
        fr3.start()

    window = ttk.Window()
    window.place_window_center()
    fr1 = Fr_(window)
    fr2 = Fr_(window)
    fr3 = Fr_(window)
    fr4 = Fr_(window)
    fr1.sleep_time = 0.1
    fr2.sleep_time = .09
    fr3.sleep_time = .2
    
    bt_start = ttk.Button(window, text='start', bootstyle=SUCCESS, command=start)
    fr1.pack()
    fr2.pack()
    fr3.pack()
    
    
    
    
    
    bt_start.pack()
    
    
    
    window.style.theme_use('cyborg')
    window.geometry('500x500')
    window.bind('q', lambda x: window.quit())
    window.bind('<Escape>', lambda x: window.quit())

    
    window.mainloop()