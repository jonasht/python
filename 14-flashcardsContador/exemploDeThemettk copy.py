import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar
from tkinter import Tk


root = ttk.Window()
# root = Tk()


root.bind('q', lambda x: exit())

themes = root.style.theme_names()

stringvar = StringVar()

root.style.theme_use('darkly')


def change_theme():
    theme = stringvar.get()
    root.style.theme_use(theme)


rb = []
frame = ttk.Frame(root)

for i, theme in enumerate(themes):
    rb.append(ttk.Radiobutton(frame, text=theme, variable=stringvar,
              value=theme, command=change_theme))
    rb[i].grid(row=0, column=i, padx=6)


frame.grid(row=2, columnspan=8)
user_choice = ttk.IntVar()


def print_var():
    print(user_choice.get())


j = 1
speed = ['10', '20', '30', '40']

root.menubutton_1 = ttk.Menubutton(root, text='speed')
root.menubutton_1.menu = ttk.Menu(root.menubutton_1)
root.menubutton_1.grid()
root.file_menu = ttk.Menu(root.menubutton_1, tearoff=0)
for i in speed:
    s = root.file_menu.add_radiobutton(
        label=i, variable=user_choice, value=i)
    j += 1
root.menubutton_1.config(menu=root.file_menu)
root.mainloop()
root.mainloop()
