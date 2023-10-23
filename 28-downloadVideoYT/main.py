import ttkbootstrap as ttk
from ttkbootstrap import Window
from ttkbootstrap.constants import *
from tkinter import filedialog
from downloadVideo import download_yt
import pyperclip as ppc
import utils as u
from PIL import Image, ImageTk
 

class Root(Window):
    def __init__(self):
        super().__init__()
        
        # put theme
        self.style.theme_use(u.get_configTheme())

        # frame botoes
        # self.fr_bts = ttk.Frame(self)

        self.lb_title = ttk.Label(self, text='Paste the Links for Downloading:', font=('15'))
        self.txt = ttk.Text(self, height=25) 
        self.bt_delete = ttk.Button(self, text='Delete')

        self.lb_lang = ttk.Label(self, text='Language:')
        self.cb_lang = ttk.Combobox(self, state=DISABLED)
        
        self.bt_paste = ttk.Button(self, text='Paste')
        self.bt_download = ttk.Button(self, text='Download')

        # command button =-=-=-=-=-=-=
        self.bt_paste.configure(command=self.cmd_paste)
        self.bt_download.configure(command=self.cmd_download)
        self.bt_delete.configure(command=self.cmd_delete)
        
        
        self.lb_aviso = ttk.Label(self, text='')
        self.lb_msg = ttk.Label(self, text='esc to exit', font=('Arial', 23, 'bold'))

        self.lb_file = ttk.Label(self, text='file:')
        self.et_file = ttk.Entry(self)
        self.bt_file = ttk.Button(self, text='Open file', command=self.cmd_open)
        
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
        
        self.bt_delete.grid(row=4, column=0, columnspan=3, sticky=EW)
        self.lb_aviso.grid(row=5, column=0, columnspan=3)

        # colocando botoes
        self.bt_paste.grid(row=1, column=3, sticky=NSEW)
        self.bt_download.grid(row=2, column=3, rowspan=2, sticky=NSEW)
        self.lb_msg.grid(row=4, column=3)


        self.bt_config.grid(row=6, column=3, sticky=E)

        self.lb_file.grid(row=6, column=0, sticky=E )
        self.et_file.grid(row=6, column=1, sticky=EW)
        self.bt_file.grid(row=6, column=2, sticky=EW)

        
    def change_theme(self, event):
        theme = self.cb.get()
        print(theme)
        self.style.theme_use(theme)
        u.set_configTheme(self.style.theme_use())
        
    def open_topbar(self):
        self.toplevel = ttk.Toplevel(self)
        self.toplevel.geometry('300x200')
        self.toplevel.title('config')

        self.fr_theme = ttk.Label(self.toplevel)

        self.lb_theme = ttk.tk.Label(self.fr_theme, text='Theme:')


        cb_list = self.style.theme_names()
        self.cb = ttk.Combobox( self.fr_theme, values=cb_list)
        self.cb.set(cb_list[cb_list.index(self.style.theme_use())])

        self.bt_toplevelQuit = ttk.Button(self.toplevel, text='Quit')

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
                
 
    def cmd_download(self):
        self.lb_aviso.configure(text='download, wait', bootstyle=WARNING)
        
        txt = self.txt.get(1.0, END)
        txt = txt.split('\n')
        print(txt)

        # remove all space ''
        while '' in txt: txt.remove('')
        
        # error_lines = list()
        if txt:
      
            for i, t in enumerate(txt):
            
                    msg = download_yt(t)
                    # error_lines.append(msg)

        #     if msg:
        #         self.lb_aviso.configure(text='download feito com sucesso', bootstyle=SUCCESS)
        #     else:
        #         self.lb_aviso.configure(text='ocorreu um erro', bootstyle=DANGER)
                
        else:
            self.lb_aviso.configure(text='por favor coloque um link de video do youtube', bootstyle=WARNING)

        self.lb_aviso.configure(text='download feito com sucesso', bootstyle=SUCCESS)
        # self.put_tags(error_lines)
def main():
    root = Root()
    root.title('download video youtube')
    root.place_window_center()
    # root.open_topbar()
    root.bind('<Escape>', lambda x: root.quit())
    root.mainloop()

if __name__ == '__main__':
    main()
    