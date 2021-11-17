import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

root = tk.Tk()
# definindo a fonte

grandeFonte = Font(
    family='Helvetica',
    size=42,
    weight='bold',
    slant='roman',
    underline=0,
    overstrike=0
)
bt1 = ttk.Button(root, text='grande botao', font=grandeFonte)
bt1.pack(pady=20)

lb1 = ttk.Label(root, text='um texxto', font=grandeFonte)
lb1.pack()
root.mainloop()