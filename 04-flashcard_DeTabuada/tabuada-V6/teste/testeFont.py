
from tkinter import Tk, ttk
from tkinter.constants import *

# Cria a janela principal
root = Tk()
style = ttk.Style()
style.configure("TButton", font='arial 30 bold')

bt1 = ttk.Button(text="Test", style="TButton")
bt2 = ttk.Button(text="Test", style="TButton")
bt1.pack()
bt2.pack()

from utils import *
root.geometry(get_configGeometry(root, 500, 500))

root.mainloop()
