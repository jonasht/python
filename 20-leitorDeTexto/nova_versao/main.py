import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

import func
from  uteis import get_dict_idioms
import uteis as u


class Window(ttk.Window):
    def __init__(self):
        super().__init__()
        self.fr = ttk.Frame(self)
        self.style.theme_use(u.read_theme())

        
        self.dict_langs = get_dict_idioms()

        self.cb_var = ttk.StringVar()
        self.cb = ttk.Combobox(self.fr, textvariable=self.cb_var,
                               width=25,
                               values=list(self.dict_langs.keys()))

        self.lb_title = ttk.Label(self.fr, text='Escreva para o leitor:')
        self.txt = ttk.Text(self.fr, width=100)
        self.bt_read = ttk.Button(self.fr, text='Ler', command=self.bt_press)
        self.bt_clean = ttk.Button(self.fr, text='Limpar', command=self.toClean)

        # separetor
        self.sp = ttk.Separator(self.fr, orient=HORIZONTAL)
        
        self.image = Image.open('./contexto.png')
        self.image = self.image.resize((25, 25), Image.LANCZOS)
        self.imagetk = ImageTk.PhotoImage(self.image)
        self.bt_config = ttk.Button(self.fr, image=self.imagetk, command=self.open_topbar)

        # grids =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.lb_title.grid(row=0, column=0, sticky=W, pady=10)
        self.cb.grid(row=0, column=1, sticky=E)
        self.txt.grid(row=1, column=0, columnspan=2)
        self.bt_clean.grid(row=2, column=0, sticky=EW, pady=4, padx=1)
        self.bt_read.grid(row=2, column=1, sticky=EW, padx=1)
        
        
        self.sp.grid(row=3, column=0, sticky=EW, columnspan=2, padx=10, pady=10)
        self.bt_config.grid(row=4, column=1, sticky=E)
        # default combobox
        self.cb.set('portugues Brasil')

        # boot style
        self.bt_read.config(bootstyle=SUCCESS, padding=10)
        self.bt_clean.config(bootstyle=DANGER,padding=10)
        self.bt_config.config(bootstyle=LINK+INFO, padding=0)

        self.fr.pack(anchor=CENTER, side=TOP, padx=10, pady=10)

        
    def bt_press(self):
        lang = self.dict_langs[self.cb_var.get()]
        
        txt = self.txt.get('1.0', END)
        func.read(txt, lang)

    def toClean(self):
        self.txt.delete('1.0', END)

    def change_theme(self, event):
        theme = self.cb_theme.get()
        theme = theme.lower()

        print(theme)
        self.style.theme_use(theme)
        u.read_theme(theme)
        

    def open_topbar(self):
        self.toplevel = ttk.Toplevel(self)
        self.toplevel.geometry('500x400')
        self.toplevel.title('configurações')

        self.lb_theme = ttk.tk.Label(self.toplevel, text="tema:")
        
        cb_list = list(map(lambda x: x.title(), u.theme_names))

        self.cb_theme = ttk.Combobox(
            self.toplevel, values=cb_list)
        self.cb_theme.set(cb_list[0])

        self.lb_theme.pack()
        self.cb_theme.pack()
        self.cb_theme.bind('<<ComboboxSelected>>', self.change_theme)
        
if __name__ == '__main__':
    
    window = Window()
    window.title('leitorDeTexto')
    # window.style.theme_use('darkly')
    window.open_topbar()
    window.bind('<Escape>', lambda x: window.quit())
    
    window.place_window_center()
    window.mainloop()
