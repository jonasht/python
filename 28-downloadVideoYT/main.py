import ttkbootstrap as ttk
from ttkbootstrap import Window
from ttkbootstrap.constants import *
from tkinter import filedialog
from downloadVideo import download_yt
import pyperclip as ppc
import utils as u
from PIL import Image, ImageTk
import time 
from lang import Languages 
from pytube import YouTube
import threading

class Root(Window):
    def __init__(self):
        super().__init__()
        self.l = Languages()
        # put theme
        self.style.theme_use(u.get_configTheme())

        # frame center 
        self.fr_center = ttk.Frame(self)
        # frame delete and frame progressBar
        self.fr_delete = ttk.Frame(self.fr_center)
        self.fr_progressBar = ttk.Frame(self.fr_center)
        
        self.lb_title = ttk.Label(self.fr_center, text=self.l.lb_title, font=('15'))
        self.txt = ttk.Text(self.fr_center, height=25) 
        self.progressBar = ttk.Progressbar(self.fr_progressBar, length=300, maximum=100, mode=DETERMINATE, value=0)
        self.lb_percent = ttk.Label(self.fr_progressBar, text=f'  0%')
        
        self.bt_delete = ttk.Button(self.fr_delete, text=self.l.bt_delete)

        self.lb_lang = ttk.Label(self, text=self.l.lb_lang)
        self.var_cbLang = ttk.StringVar()
        self.cb_lang = ttk.Combobox(self, state=READONLY, textvariable=self.var_cbLang, bootstyle=SUCCESS)
        self.cb_lang.config(values=self.l.languages)
        self.cb_lang.set(self.l.language)
        self.cb_lang.bind('<<ComboboxSelected>>', self.change_lang)
        
        
        self.bt_paste = ttk.Button(self.fr_center, text=self.l.bt_paste)
        self.bt_download = ttk.Button(self.fr_center, text=self.l.bt_download)

        # command button =-=-=-=-=-=-=
        self.bt_paste.configure(command=self.cmd_paste)
        self.bt_download.configure(command=self.cmd_download)
        self.bt_delete.configure(command=self.cmd_delete)
        
        
        self.lb_aviso = ttk.Label(self.fr_center, text='')
        self.lb_msg = ttk.Label(self.fr_center, text=self.l.lb_msg, font=('Arial', 23, 'bold'))

        self.lb_file = ttk.Label(self, text=self.l.lb_file)
        self.et_file = ttk.Entry(self)
        self.bt_file = ttk.Button(self, text=self.l.bt_file, command=self.cmd_open)
        
        # self.bt_file.config(width=20)
        self.et_file.config(width=61)
        
        # button config
        self.image = Image.open('./contexto.png')
        self.image = self.image.resize((25, 25), Image.LANCZOS)

        self.imagetk = ImageTk.PhotoImage(self.image)
        self.bt_config = ttk.Button(self, image=self.imagetk, command=self.open_topbar, bootstyle=LINK)

        # bootstyle buttons
        self.bt_download.config(bootstyle=SUCCESS)
        self.bt_delete.config(bootstyle=DANGER,)
        

        self.lb_title.grid(row=0, column=0, columnspan=2, sticky=W)
        self.txt.grid(row=1, column=0, rowspan=3, columnspan=3)
        
        self.lb_lang.grid(row=0, column=2)
        self.cb_lang.grid(row=0, column=3)
        
        self.progressBar.grid(row=0, column=0, columnspan=3, sticky=EW)
        self.lb_percent.grid(row=0, column=1)
        self.fr_progressBar.grid(row=4, column=0, columnspan=3, sticky=NSEW)
        
        self.bt_delete.grid(row=0, column=0, sticky=EW)
        self.fr_delete.grid(row=4, column=0, columnspan=3, sticky=NSEW)
        
        # sticky frames delete progressbar
        self.fr_progressBar.columnconfigure(0, weight=1)
        self.fr_progressBar.rowconfigure(0, weight=1)
        self.fr_delete.columnconfigure(0, weight=1)
        self.fr_delete.rowconfigure(0, weight=1)
        self.fr_delete.tkraise()

        
        self.lb_aviso.grid(row=6, column=0, columnspan=3)

        # colocando botoes
        self.bt_paste.grid(row=1, column=3, sticky=NSEW)
        self.bt_download.grid(row=2, column=3, rowspan=2, sticky=NSEW)
        self.lb_msg.grid(row=4, column=3)

        self.fr_center.grid(row=1, column=0, columnspan=4)
        self.bt_config.grid(row=7, column=3, sticky=E)

        self.lb_file.grid(row=7, column=0, sticky=E )
        self.et_file.grid(row=7, column=1, sticky=EW)
        self.bt_file.grid(row=7, column=2, sticky=EW)

    # change languages portuguese and english
    def change_lang(self, event):
        lang = self.var_cbLang.get()
        # if lang == 'english':
            # self.l.set_lang('en')
        # elif lang == 'portuguese':
            # self.l.set_lang('pt')
        # change language
        self.l.set_lang(lang)

        self.lb_title.config(text=self.l.lb_title)
        self.bt_delete.config(text=self.l.bt_delete)
        self.lb_lang.config(text=self.l.lb_lang)
        self.bt_paste.config(text=self.l.bt_paste)
        self.bt_download.config(text=self.l.bt_download)
        self.lb_msg.config(text=self.l.lb_msg)
        self.lb_file.config(text=self.l.lb_file)
        self.bt_file.config(text=self.l.bt_file)
        
        # self.toplevel.title(self.l.toplevel_title)
        # self.lb_theme = ttk.tk.Label(self.fr_theme, text=self.l.lb_theme)
        # self.bt_toplevelQuit = ttk.Button(self.toplevel, text=self.l.bt_toplevelQuit)

    def change_theme(self, event):
        theme = self.cb.get()
        print(theme)
        self.style.theme_use(theme)
        u.set_configTheme(self.style.theme_use())
        
    def open_topbar(self):
        self.toplevel = ttk.Toplevel(self)
        self.toplevel.geometry('300x200')
        self.toplevel.title(self.l.toplevel_title)

        self.fr_theme = ttk.Label(self.toplevel)

        self.lb_theme = ttk.tk.Label(self.fr_theme, text=self.l.lb_theme)


        cb_list = self.style.theme_names()
        self.cb = ttk.Combobox( self.fr_theme, values=cb_list, state=READONLY, bootstyle=SUCCESS)
        self.cb.set(cb_list[cb_list.index(self.style.theme_use())])

        self.bt_toplevelQuit = ttk.Button(self.toplevel, text=self.l.bt_toplevelQuit)

        self.bt_toplevelQuit.config(command=lambda:self.toplevel.destroy())
        self.bt_toplevelQuit.config(bootstyle=DANGER)
        self.lb_theme.grid(row=0, column=0)
        self.cb.grid(row=0, column=1)
        self.fr_theme.pack(side=TOP)
        self.bt_toplevelQuit.pack(side=BOTTOM, fill=BOTH)
        
        self.toplevel.bind('<Escape>', lambda x: self.toplevel.destroy())
        
        self.cb.bind('<<ComboboxSelected>>', self.change_theme)
        
    def cmd_open(self):
    
        self.filename = filedialog.askopenfilename(initialdir='./', 
                                            title='select a file',
                                            filetypes=(('txt files', '.txt'), ("all files", '.*'))
                                            
                                            )  
        
        filename = self.filename
        self.et_file.insert(0, filename)
        text = u.read(filename)
        self.txt.insert(1.0, text)
        
    def cmd_paste(self):
        txt = self.txt.get(1.0, END)
        paste = ppc.paste()

        if txt[-2:] == '\n\n' or txt=='\n':
            self.txt.insert(END, paste+'\n')
        else:
            self.txt.insert(END, '\n'+paste+'\n')
            
    

    def cmd_delete(self):
        self.txt.delete(1.0, END)

    def put_tags(self, error_lines):
        pass

        lines = self.txt.get(1.0, END)
        lines = lines.split('\n')
        while '' in lines: lines.remove('')
        print(lines)
        lines_names = list()
        # criando tag names
        for i, line in enumerate(lines):
            self.txt.tag_add(f'l{i+1}', f'{i+1}.0', f'{i+1}.{len(line)}') 
            print(f'l{i+1}', f'{i+1}.0', f'{i+1}.{len(line)}') 
            lines_names.append(f'l{i+1}')
            
        print('lines name', lines_names)
        # self.txt.tag_add('l1', 1.0, 1.6)        
        for name, error in zip(lines_names, error_lines):
            if error:
                
                self.txt.tag_config(name, foreground='green')
            else:
                self.txt.tag_config(name, foreground='red')
                
    def disabled(self):
        self.bt_config.config(state=DISABLED)
        self.bt_delete.config(state=DISABLED)
        self.bt_download.config(state=DISABLED)
        self.bt_file.config(state=DISABLED)
        self.bt_paste.config(state=DISABLED)
        self.txt.config(state=DISABLED)
        self.et_file.config(state=DISABLED)
        
    def normal(self):
        self.bt_config.config(state=NORMAL)
        self.bt_delete.config(state=NORMAL)
        self.bt_download.config(state=NORMAL)
        self.bt_file.config(state=NORMAL)
        self.bt_paste.config(state=NORMAL)
        self.txt.config(state=NORMAL)
        self.et_file.config(state=NORMAL)

    def cmd_download(self):
        self.fr_progressBar.tkraise()
        thread = threading.Thread(target=self.disabled)
        thread.start()
        th2 = threading.Thread(target=self.download)
        th2.start()

    def download(self):

        self.lb_aviso.configure(text='download, wait', bootstyle=WARNING)
        
        self.links = self.txt.get(1.0, END)
        self.links = self.links.split('\n')
        # print(txt)

        # remove all space ''
        while '' in self.links: self.links.remove('')
        
        self.lb_percent.config(text=f'{str(0):>3}%{len(self.links)}')
        

        for link in self.links:
            yt = YouTube(link, on_progress_callback=self.loading)
            video = yt.streams.get_highest_resolution()
            video.download()

        self.normal()
        self.lb_aviso.config(bootstyle=SUCCESS, text='download completed')
        self.fr_delete.tkraise()
        
    def loading(self, stream, chunk, bytes_remaining):
        
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percent = int(bytes_downloaded / total_size * 100)

        self.lb_percent.config(text=f'{str(percent):>3}%')
        self.progressBar.config(value=percent)
        self.progressBar.update()
        qtd_download = len(self.links)
        
        if percent == 100:
            self.progressBar.config(bootstyle=SUCCESS)
            self.progressBar.update()
            self.lb_percent.config(text=f'{str(100):>3}%{qtd_download}', bootstyle=SUCCESS)

            time.sleep(.5)
            self.progressBar.config(bootstyle=WARNING, value=0)
            self.progressBar.update()
            self.lb_percent.config(text=f'{str(0):>3}%{qtd_download}', bootstyle=WARNING)
            
        
def main():
    root = Root()
    root.title('download video youtube')
    root.place_window_center()
    # root.open_topbar()
    root.bind('<Escape>', lambda x: root.quit())
    root.mainloop()
    
    

if __name__ == '__main__':
    # apagar todos os videos
    import os
    os.system('rm *.mp4')
    main()
    