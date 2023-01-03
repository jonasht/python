import gtts 
from customtkinter import *
from tkinter import ttk


dict_idioms = gtts.lang.tts_langs()
lista = dict_idioms.values()
print(lista)
# print(dict_idioms)
lista = list(lista)
lista = lista[:20]
root = CTk()
root.geometry('500x500')

cb_var = StringVar()

cb = ttk.Combobox(root, textvariable=cb_var, values=lista)

cb.grid()
def t_event(event):
    print(cb_var.get())

cb.set('teste 1')
cb.grid()

root.bind('t', t_event)
root.bind('<Escape>', lambda x: root.destroy())

root.mainloop()