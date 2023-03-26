import ttkbootstrap as ttk
from tkinter import ttk as tt
from ttkbootstrap.constants import *



window = ttk.Window()
window.geometry('500x500')
window.style.theme_use('darkly')
window.bind('q', lambda x: window.quit())

style1 = ttk.Style()
style1.configure('my.TButton', font=('Helvetica', 22), foreground='gray')


bt = ttk.Button(text='teste', style='my.TButton')




bt.pack()
window.mainloop()
