from tkinter import *

cadastro = Tk()
def cadastrar():
    bd = dict(
        nome=entdnome.get(),
        sexo=entdsexo.get(),
        idade=entdidade.get()
        
    )
    print(bd)

lbnome = Label(cadastro, text='nome:')
lbnome.grid(row=1, column=1)
cadastro.title('cadastro')
# cadastro.config(background='gray')

entdnome = Entry(cadastro)
entdnome.grid(row=1, column=2)

lbsexo = Label(cadastro, text='sexo:')
entdsexo = Entry(cadastro)
lbsexo.grid(row=2, column=1)
entdsexo.grid(row=2, column=2)

lbidade = Label(cadastro, text='idade:')
entdidade = Entry(cadastro)
lbidade.grid(row=3, column=1)
entdidade.grid(row=3, column=2)

btcadastrar = Button(cadastro, text='cadastrar', command=cadastrar)
btcadastrar.grid(row=4, column=2, columnspan=3)

btsair = Button(cadastro, text='sair', command=cadastro.quit)
btsair.grid(row=4, column=1)


cadastro.mainloop()