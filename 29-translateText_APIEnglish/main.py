import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import utils as u
import eng_to_ipa as ipa



class Frame(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.bt_translate = ttk.Button(self, text='Translate', padding=20)
        self.bt_translate.configure(command=self.cmd_translate)
        self.lb1 = ttk.Label(self, text='english text:')
        self.lb2 = ttk.Label(self, text='alphabet phonetic international:')
        self.lb1.config(bootstyle=INFO)
        self.lb2.config(bootstyle=INFO)
        width_tt = 130
        height_tt = 50

        self.tt1 = ttk.Text(self, width=width_tt, height=height_tt)
        self.tt2 = ttk.Text(self, width=width_tt, height=height_tt)
        
        self.fr_file = ttk.Frame(self)
        self.lb_file = ttk.Label(self.fr_file, text='file:')
        self.et_file = ttk.Entry(self.fr_file)
        self.bt_file = ttk.Button(self.fr_file, text='Open file', command=self.cmd_open)
        
        self.lb1.grid(row=1, column=0, sticky=EW, padx=7)
        self.lb2.grid(row=1, column=1, sticky=EW)
        self.tt1.grid(row=2, column=0)
        self.tt2.grid(row=2, column=1)
        self.bt_translate.grid(row=3, column=0, columnspan=2, pady=10, padx=5, sticky=EW)

        self.lb_file.grid(row=0, column=0, padx=5,)
        self.et_file.grid(row=0, column=1, padx=5,)
        self.bt_file.grid(row=0, column=3, padx=5,)

        self.et_file.config(width=90)
        self.bt_file.config(width=30)
        self.fr_file.grid(row=4, column=0, sticky=EW, padx=5,)
        
        
        self.fr_save = ttk.Frame(self)
        self.lb_save = ttk.Label(self.fr_save, text='save:')
        self.et_save = ttk.Entry(self.fr_save)
        self.bt_save = ttk.Button(self.fr_save, text='save file', command=self.save_file)
        

        self.lb_save.grid(row=0, column=0, padx=5,)
        self.et_save.grid(row=0, column=1, padx=5,)
        self.bt_save.grid(row=0, column=3, padx=5,)

        self.et_save.config(width=90)
        self.bt_save.config(width=30)
        self.fr_save.grid(row=4, column=1, sticky=EW, padx=5,)
        
        self.tt2.configure(state=DISABLED)
        # self.tt1.insert(1.0, 'hello world')
        
        # disabled save button
        self.bt_save.config(state=DISABLED)
    def save_file(self):
        self.f = filedialog.asksaveasfile(
            initialfile = 'Untitled.txt',
            defaultextension=".txt", 
            filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        
        print(self.f)
    def cmd_open(self):
    
        self.filename = filedialog.askopenfilename(initialdir='./', 
                                            title='select a file',
                                            filetypes=(('txt files', '.txt'), ("all files", '.*'))
                                            
                                            )

        
        filename = self.filename
        self.et_file.insert(0, filename)
        text = u.read(filename)
        self.tt1.insert(1.0, text)
        
    def cmd_translate(self):
        self.tt2.configure(state=NORMAL)
        text = self.tt1.get(1.0, END)
        print(text)
        text = ipa.convert(text)
        self.tt2.insert(1.0, text)
        
def main():

    window = ttk.Window()
    window.style.theme_use('darkly')
    # window.bind('q', lambda x: window.quit())
    window.bind('<Escape>', lambda x: window.quit())

    frame = Frame(window)
    frame.pack()
    window.mainloop()

if __name__ == "__main__":
    main()