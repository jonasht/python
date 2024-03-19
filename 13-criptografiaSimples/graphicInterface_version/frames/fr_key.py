from tkinter import *
from tkinter import ttk
import pyperclip as pc

class Fr_key(ttk.Frame):
    def __init__(self, parent, con):
        super().__init__(parent)
        self.con = con
        self.fr_et = ttk.Frame(self)
        self.lb_key = ttk.Label(self.fr_et, text='Key:')
        self.etd = ttk.Entry(self.fr_et)
        self.bt_paste = ttk.Button(self, text='Colar', command=self.colar)

        self.bt_del = ttk.Button(self, text='Apagar', command=self.deletar)
        self.bt_copy = ttk.Button(self, text='Copiar', command=self.copiar)
        
        self.cbt_value = BooleanVar()
        self.cbt = ttk.Checkbutton(self, text='Colorir', variable=self.cbt_value, command=self.cbt_evento)


        # self.lb_key.grid(row=0, column=0, padx=3, pady=3, sticky=E)
        # self.lb_key.grid(row=0, column=0, pady=3, sticky=E)
        # self.etd.grid(row=0, column=1, sticky=EW, pady=3)
        self.lb_key.grid(row=0, column=0)
        self.etd.grid(row=0, column=1)

        self.fr_et.grid(row=0, column=1, sticky=EW, ipadx=3)

        self.cbt.grid(row=0, column=3, padx=3, pady=3)
        self.bt_paste.grid(row=0, column=2, padx=2, pady=3)
        
        self.bt_copy.grid(row=1, column=0, ipadx=90, columnspan=2, sticky=NSEW, padx=3, pady=3)
        self.bt_del.grid(row=1, column=2, columnspan=2, sticky=NSEW, padx=3, pady=3)
        
    def cbt_evento(self):
        self.con.put_color(None)
        
    def deletar(self):
        # self.con.del_etd()
        self.etd.delete(0, END)
        
    def copiar(self):
        pc.copy(self.etd.get())

    def colar(self):
        txt = pc.paste()
        self.deletar()
        self.etd.insert(0, txt)




if __name__ == '__main__':
    # from main import main
    from ..main import main
    main()
    # fazendo test
    # app = Tk()


    # # Create a style
    # style = ttk.Style(app)

    # # Import the tcl file
    # app.tk.call('source', './forest_ttk_theme/forest-dark.tcl')

    # # Set the theme with the theme_use method
    # style.theme_use("forest-dark")

    # fr = Fr_key(app, app)
    # fr.grid(sticky=NSEW)
    # fr.config(border=20)
    # fr.etd.config(width=30)
    # from sys import exit
    # app.bind('q', exit)

    # app.mainloop()
