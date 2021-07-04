from tkinter import *
from tkinter.messagebox import showinfo


def reply(nome):
    if nome:
        showinfo(title='reply', message=f'ola, {nome}')
    else:
        showinfo(title='reply', message=f'ola, "semNome"')
    


top = Tk()
# top.iconbitmap("img.ico")
top.title('echo')


Label(top, text='coloque teu nome:').pack(side=TOP)
entrada = Entry(top)
entrada.pack(side=TOP)
botao = Button(top, text='enviar', command=(lambda: reply(entrada.get())))
botao.pack()
top.mainloop()