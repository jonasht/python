import ttkbootstrap as ttk


class Window(ttk.Window):
    def __init__(self) -> None:
        super().__init__()

        ttk.Label(self, text="primeria tela").pack()
        ttk.Button(self, text='click').pack()
        ttk.Label(self, text="primeria tela").pack()
        ttk.Button(self, text='click').pack()
        ttk.Label(self, text="primeria tela").pack()
        ttk.Button(self, text='click').pack()

        ttk.Button(self, text='configuracoes',
                   command=self.open_2window).pack(pady=20)

        cb_list = self.style.theme_names()

        self.cb = ttk.Combobox(
            self, values=cb_list, bootstyle='success')
        self.cb.set(cb_list[0])

        self.cb.pack()

        self.cb.bind('<<ComboboxSelected>>', self.change_theme)

    def change_theme(self, event):
        theme = self.cb.get()
        print(theme)
        self.style.theme_use(theme)

    def open_2window(self):

        self.toplevel = ttk.Toplevel(self)
        self.toplevel.bind('q', lambda x: self.quit(), self.toplevel.quit())
        self.toplevel.geometry('500x400')


win = Window()
win.geometry('500x500')

win.bind('q', lambda x: win.quit())

win.mainloop()
