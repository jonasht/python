from tkinter import END, EW, BooleanVar, ttk, Tk, Text
import func



class Fr(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.event_ch = BooleanVar()

        self.bt_read = ttk.Button(self, text='ler')
        self.bt_read.config(command=self.bt_press)

        self.txt = Text(self)
        
        self.txt.grid(row=0, column=0, pady=3)
        self.bt_read.grid(row=1, column=0, padx=3, ipady=2, sticky=EW)
        self.txt.config(font='arial 15 bold')

    def bt_press(self):
        txt = self.txt.get('1.0', END)
        print(txt)
        print(txt.split('\n'))
        
        
        func.read(txt)
        
if __name__ == '__main__':
    root = Tk()
    root.title('leitorDeTexto')
    fr = Fr(root)
    fr.pack()
    root.geometry('890x640')
    root.mainloop()
