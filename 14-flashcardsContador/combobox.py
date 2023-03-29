import ttkbootstrap as ttk


root = ttk.Window()
var = ttk.StringVar()


def show(e):
    print(cb.get())
    root.style.theme_use(cb.get())


cb_list = root.style.theme_names()

cb = ttk.Combobox(root, values=cb_list, bootstyle='success')
root.geometry('500x500')
cb.set(cb_list[0])
cb.pack()
cb.bind('<<ComboboxSelected>>', show)
root.mainloop()
