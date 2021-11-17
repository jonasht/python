from tkinter import *
from tkinter import font
from tkinter.font import Font

root = Tk()
# definindo a fonte
grandeFonte = Font(
    family='Helvetica',
    size=42,
    weight='bold',
    slant='roman',
    underline=0,
    overstrike=0
)
bt1 = Button(root, text='grande botao', font=grandeFonte)
bt1.pack(pady=20)

lb1 = Label(root, text='um texxto', font=grandeFonte)
lb1.pack()
root.mainloop()