import ttkbootstrap as ttk
from ttkbootstrap import Window
from ttkbootstrap.constants import *
from tkinter import filedialog
from downloadVideo import download_yt
import pyperclip as ppc
import utils as u

class Root(Window):
    def __init__(self):
        super().__init__()
        # put theme
        self.style.theme_use(u.get_configTheme())


        # frame botoes
        self.fr_bts = ttk.Frame(self)

        self.txt = ttk.Text(self, height=50) 
        self.lb_title = ttk.Label(self, text='put the links for downloading:', font=('Arial', 20, 'bold'))

        self.bt_paste = ttk.Button(self.fr_bts, text='Paste',  width=24, padding=65)
        self.bt_download = ttk.Button(self.fr_bts, text='Download', bootstyle=SUCCESS, width=20, padding=80)
        self.bt_delete = ttk.Button(self.fr_bts, text='Delete', bootstyle=DANGER, width=24, padding=65)

        self.bt_paste.configure(command=self.cmd_paste)
        self.bt_download.configure(command=self.cmd_download)
        self.bt_delete.configure(command=self.cmd_delete)
        
        
        self.lb_aviso = ttk.Label(self, text='', font=('Arial', 15))
        self.lb_msg = ttk.Label(self, text='esc to exit', font=('Arial', 23, 'bold'))

        self.fr_file = ttk.Frame(self)
        self.lb_file = ttk.Label(self.fr_file, text='file:')
        self.et_file = ttk.Entry(self.fr_file)
        self.bt_file = ttk.Button(self.fr_file, text='Open file', command=self.cmd_open)
        
        self.bt_file.config(width=20)
        self.et_file.config(width=50)

        self.bt_config = ttk.Button(self, text='config', command=self.open_topbar)
        
        self.lb_title.grid(row=0, column=0)
        self.txt.grid(row=1, column=0, padx=20, pady=20, rowspan=2)
        
        self.lb_msg.grid(row=2, column=1, padx=10)
        self.lb_aviso.grid(row=3, column=0, columnspan=1)

        # colocando botoes
        self.bt_paste.grid(row=0, column=0, pady=10)
        self.bt_download.grid(row=1, column=0, pady=10)
        self.bt_delete.grid(row=2, column=0, pady=10)

        self.fr_bts.grid(row=1, column=1, rowspan=1)


        self.lb_file.grid(row=0, column=0, padx=6, pady=4)
        self.et_file.grid(row=0, column=1, padx=6, pady=4)
        self.bt_file.grid(row=0, column=2, padx=6, pady=4)
        self.fr_file.grid(row=4, column=0, padx=6)
        
        self.bt_config.grid(row=4, column=1, sticky=EW, columnspan=1, padx=6)
        # esc para sair
        self.bind('<Escape>', lambda x: self.quit())
        
    def change_theme(self, event):
        theme = self.cb.get()
        print(theme)
        self.style.theme_use(theme)
        u.set_configTheme(self.style.theme_use())
        
    def open_topbar(self):
        self.toplevel = ttk.Toplevel(self)
        self.toplevel.geometry('500x400')

        self.lb_theme = ttk.tk.Label(self.toplevel, text="tema:")

        cb_list = self.style.theme_names()
        self.cb = ttk.Combobox(
            self.toplevel, values=cb_list, bootstyle='success')
        self.cb.set(cb_list[cb_list.index(self.style.theme_use())])



        self.lb_theme.pack()
        self.cb.pack()

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
        
        # remove all space ''
        while '' in txt: txt.remove('')
        
        error_lines = list()
        if txt:
      
            for i, t in enumerate(txt):
            
                    msg = download_yt(t)
                    error_lines.append(msg)

            if msg:
                self.lb_aviso.configure(text='download feito com sucesso', bootstyle=SUCCESS)
            else:
                self.lb_aviso.configure(text='ocorreu um erro', bootstyle=DANGER)
                
        else:
            self.lb_aviso.configure(text='por favor coloque um link de video do youtube', bootstyle=WARNING)

        self.lb_aviso.configure(text='download feito com sucesso', bootstyle=SUCCESS)
        self.put_tags(error_lines)
def main():
    root = Root()
    root.title('download video youtube')

    root.bind('q', lambda x: root.quit())
    root.mainloop()

if __name__ == '__main__':
    main()
    