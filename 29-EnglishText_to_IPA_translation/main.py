import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import utils as u
import eng_to_ipa as ipa



class Frame(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        
        # frames lines
        self.line1 = ttk.Frame(self)
        self.line2 = ttk.Frame(self)
        self.line3 = ttk.Frame(self)
        self.line4 = ttk.Frame(self)
        

        self.lb1 = ttk.Label(self.line1, text='English Text:', font=('Arial', 16, 'bold'))
        self.lb2 = ttk.Label(self.line1, text=':Alphabet Phonetic International', font=('Arial', 16, 'bold'))
        self.tt1 = ttk.Text(self.line2)
        self.tt2 = ttk.Text(self.line2)
        
        self.bt_translate = ttk.Button(self.line3, text='Translate', bootstyle=SUCCESS, padding=20)
        self.bt_translate.configure(command=self.cmd_translate)
        self.lb1.config(bootstyle=INFO)
        self.lb2.config(bootstyle=INFO)        

        
        self.lb_file = ttk.Label(self.line4, text='file:')
        self.et_file = ttk.Entry(self.line4)
        self.bt_file = ttk.Button(self.line4, text='Open file', bootstyle=INFO, command=self.cmd_open)
        
        self.lb_save = ttk.Label(self.line4, text='save:')
        self.et_save = ttk.Entry(self.line4)
        self.bt_save = ttk.Button(self.line4, text='save file', command=self.save_file)

        
        self.lb1.pack(side=LEFT, fill=X)
        self.lb2.pack(side=RIGHT,fill=X)
        self.tt1.pack(side=LEFT, anchor=W, expand=True, fill=BOTH)
        self.tt2.pack(side=LEFT, anchor=E, expand=True, fill=BOTH)
        self.bt_translate.pack(fill=X, expand=True, pady=5)
        
        self.lb_file.pack(side=LEFT)
        self.et_file.pack(side=LEFT, expand=True, fill=X)
        self.bt_file.pack(side=LEFT, expand=True, fill=X, padx=5)
        
        self.bt_save.pack(side=RIGHT, expand=True, fill=X)
        self.et_save.pack(side=RIGHT, expand=True, fill=X, padx=5)
        self.lb_save.pack(side=RIGHT)
        
        # linhas pack
        self.line1.pack(fill=X)
        self.line2.pack(anchor=CENTER,fill=BOTH, expand=True)
        self.line3.pack(anchor=S,fill=X)
        self.line4.pack(anchor=S,fill=X)


        
        self.tt2.configure(state=DISABLED)
        # self.tt1.insert(1.0, 'hello world')
        
        # disabled save button
        self.bt_save.config(state=DISABLED)
    def save_file(self):
        self.f = filedialog.asksaveasfile(
            initialfile = 'Untitled.txt',
            defaultextension=".txt", 
            filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        
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
    # window.style.theme_use('cyborg')
    window.style.theme_use('darkly')
    window.title('IPA Translation')
    # window.bind('q', lambda x: window.quit())
    window.bind('<Escape>', lambda x: window.quit())
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(f'{width}x{height}')
    frame = Frame(window)
    frame.pack(fill=BOTH, expand=True)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(0, weight=1)
    window.mainloop()

if __name__ == "__main__":
    main()