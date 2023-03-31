import ttkbootstrap as ttk
from tkinter import Tk
from tkinter import filedialog



root = Tk()

def open():
    
    root.filename = filedialog.askopenfilename(initialdir='./', 
                                           title='select a file',
                                           filetypes=(('txt files', '.txt'), ("all files", '.*'))
                                           
                                           )
    lb = ttk.Label(root, text=root.filename)
    lb.pack()
    
bt = ttk.Button(root, command=open, text='open file')
bt.pack()

root.geometry('500x500')
root.mainloop()