from tkinter import BOTH, CENTER, END, EW, TOP, ttk, StringVar
import func
from customtkinter import CTkLabel, CTk, CTkTextbox, CTkFrame, CTkButton, CTkFont
from  uteis import get_dict_idioms


class Fr(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.dict_langs = get_dict_idioms()

        self.fr_bts = CTkFrame(self)
        self.cb_var = StringVar()
        self.cb = ttk.Combobox(self, textvariable=self.cb_var,
                               width=25,
                               values=list(self.dict_langs.keys()))

        self.lb = CTkLabel(self, text='escreva um texto p ser lido | q para sair')
        self.bt_read = CTkButton(self.fr_bts, text='ler', width=660, height=50, command=self.bt_press)
        self.bt_clean = CTkButton(self.fr_bts, text='Limpar', width=300, height=50, command=self.toClean)

        self.txt = CTkTextbox(self, width=1000, height=700)
        
        # grid =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        self.cb.grid(row=0, column=1,)
        self.lb.grid(row=1, column=0, columnspan=2)
        self.txt.grid(row=2, column=0, columnspan=2, pady=6, padx=100)

        self.fr_bts.grid(row=3, padx=100, columnspan=2, sticky=EW)
        self.bt_clean.grid(row=3, column=0, sticky=EW, padx=10, pady=20)
        self.bt_read.grid(row=3, column=1, sticky=EW, padx=10, pady=20)
        
        font = CTkFont(family='Arial', size=20, weight='bold')
        self.txt.configure(font=font)

        # default combobox
        self.cb.set('portugues Brasil')


    def bt_press(self):
        lang = self.dict_langs[self.cb_var.get()]
        
        txt = self.txt.get('1.0', END)
        func.read(txt, lang)

    def toClean(self):
        self.txt.delete('1.0', END)

if __name__ == '__main__':
    root = CTk()
    root.title('leitorDeTexto')

    fr = Fr(root)
    
    root.bind('<Escape>', lambda x: root.destroy())

    fr.pack(anchor=CENTER, side=TOP)
    # root.geometry('1200x850')
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f'{width}x{height}')
    
    root.mainloop()
