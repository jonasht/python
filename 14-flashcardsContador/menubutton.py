import ttkbootstrap as ttk

root = ttk.Window()
root.geometry("300x200")

w = ttk.Label(root, text='GeeksForGeeks', font="50")
w.pack()

menubutton = ttk.Menubutton(root)

menubutton.menu = ttk.Menu(menubutton)
menubutton["menu"] = menubutton.menu

var1 = ttk.IntVar()
var2 = ttk.IntVar()
var3 = ttk.IntVar()
var = ttk.StringVar()


def show():
    print(var.get())


menubutton.menu.add_radiobutton(
    label='opcao3', command=show, variable=var, value='opcao 3')
menubutton.menu.add_cascade(label='opcao1')
menubutton.menu.add_command(label='opcao2', command=show)

menubutton.pack()
root.mainloop()
