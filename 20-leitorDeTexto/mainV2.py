from tkinter import END, EW, BooleanVar, ttk, Tk, Text
import func
from customtkinter import CTkLabel, CTk, CTkTextbox, CTkFrame, CTkButton, CTkFont



class Fr(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.lb = CTkLabel(self, text='escreva um texto p ser lido | q para sair')
        self.bt_read = CTkButton(self, text='ler',width=600, command=self.bt_press)
        self.bt_clean = CTkButton(self, text='Limpar', command=self.toClean)

        self.txt = CTkTextbox(self, width=1000, height=700)
        
        self.lb.grid(row=0, column=0, columnspan=2)
        self.txt.grid(row=1, column=0, columnspan=2, pady=6, padx=50)

        self.bt_clean.grid(row=2, column=0, sticky=EW)
        self.bt_read.grid(row=2, column=1, padx=3, sticky=EW)
        font = CTkFont(family='Arial', size=20, weight='bold')
        self.txt.configure(font=font)


    def bt_press(self):
        txt = self.txt.get('1.0', END)
        
        
        func.read(txt)
    def toClean(self):
        pass

if __name__ == '__main__':
    root = CTk()
    root.title('leitorDeTexto')
    fr = Fr(root)
    root.bind('<Escape>', lambda x: root.destroy())
    fr.pack()
    root.geometry('1100x800')
    root.mainloop()
