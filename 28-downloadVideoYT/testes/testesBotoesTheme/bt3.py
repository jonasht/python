import ttkbootstrap as ttk
from tkinter import ttk as tt
from ttkbootstrap.constants import *



window = ttk.Window()
window.geometry('500x500')
window.style.theme_use('darkly')
window.bind('q', lambda x: window.quit())

style = ttk.Style()
style.configure('success.TButton', font=('Helvetica bold', 22))


bt = ttk.Button(text='teste', style='success.TButton')

style.configure('danger.TButton', font=('arial bold', 22))

bt1 = ttk.Button(text='teste', style='danger.TButton')

style.configure('my.TButton', font=('arial bold', 22))
bt2 = ttk.Button(text='teste', style='my.TButton')

bt.pack()
bt1.pack()
bt2.pack()

window.mainloop()
