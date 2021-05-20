from tkinter import *

cadastro = Tk()
def cadastrar():
    bd = dict(
        id =entd_id.get(),
        nome=entdNome.get(),
        sexo=entdSexo.get(),
        idade=entdIdade.get()
    )
    
    print(bd)
# cadastro.config(background='gray')

# id
lb_id = Label(cadastro, text='id:')
entd_id = Entry(cadastro)
lb_id.grid(row=0, column=1)
entd_id.grid(row=0, column=2)

lbnome = Label(cadastro, text='nome:')
lbnome.grid(row=1, column=1)
cadastro.title('cadastro')

# nome
entdNome = Entry(cadastro)
entdNome.grid(row=1, column=2)

# sexo
lbsexo = Label(cadastro, text='sexo:')
entdSexo = Entry(cadastro)
lbsexo.grid(row=2, column=1)
entdSexo.grid(row=2, column=2)

# idade
lbidade = Label(cadastro, text='idade:')
entdIdade = Entry(cadastro)
lbidade.grid(row=3, column=1)
entdIdade.grid(row=3, column=2)

# botao cadatrar
btcadastrar = Button(cadastro, text='cadastrar', command=cadastrar)
btcadastrar.grid(row=4, column=2, columnspan=3)

# botao sair
btsair = Button(cadastro, text='sair', command=cadastro.quit)
btsair.grid(row=4, column=1)


cadastro.mainloop()