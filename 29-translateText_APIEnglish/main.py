import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import eng_to_ipa as ipa



class Frame(ttk.Frame):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.bt_translate = ttk.Button(self, text='Translate', padding=20)
        self.bt_translate.configure(command=self.cmd_translate)
        self.lb1 = ttk.Label(self, text='english text:')
        self.lb2 = ttk.Label(self, text='alphabet phonetic international:')
        width_tt = 130
        height_tt = 50

        self.tt1 = ttk.Text(self, width=width_tt, height=height_tt)
        self.tt2 = ttk.Text(self, width=width_tt, height=height_tt)
        
        self.lb1.grid(row=1, column=0, sticky=EW)
        self.lb2.grid(row=1, column=1, sticky=EW)
        self.tt1.grid(row=2, column=0)
        self.tt2.grid(row=2, column=1)
        self.bt_translate.grid(row=3, column=0, columnspan=2, sticky=EW, pady=10, padx=5)

        self.tt2.configure(state=DISABLED)
        self.tt1.insert(1.0, 'hello world')
        
    def cmd_translate(self):
        self.tt2.configure(state=NORMAL)
        text = self.tt1.get(1.0, END)
        print(text)
        text = ipa.convert(text)
        self.tt2.insert(1.0, text)

def main():

    window = ttk.Window()
    window.style.theme_use('darkly')
    window.bind('q', lambda x: window.quit())

    frame = Frame(window)
    frame.pack()
    window.mainloop()

if __name__ == "__main__":
    main()