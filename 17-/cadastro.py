from tkinter import *

cadastro = Tk()
def cadastrar():
    bd = dict(
        id =entd_id.get(),
        nome=entdNome.get(),
        sexo=entdSexo.get(),
        idade=entdIdade.get()
    )
    lb_aviso.config(text='cadastro feito com sucesso', fg='green')
    
    print(bd)
cadastro.geometry('200x150+400+300')

# id
lb_id = Label(cadastro, text='id:')
entd_id = Entry(cadastro)
lb_id.grid(row=0, column=1, pady=2)
entd_id.grid(row=0, column=2, pady=2)

lbnome = Label(cadastro, text='nome:')
lbnome.grid(row=1, column=1, pady=2)
cadastro.title('cadastro')

# nome
entdNome = Entry(cadastro)
entdNome.grid(row=1, column=2, pady=2)

# sexo
lbsexo = Label(cadastro, text='sexo:')
entdSexo = Entry(cadastro)
lbsexo.grid(row=2, column=1, pady=2)
entdSexo.grid(row=2, column=2, pady=2)

# idade
lbidade = Label(cadastro, text='idade:')
entdIdade = Entry(cadastro)
lbidade.grid(row=3, column=1, pady=2)
entdIdade.grid(row=3, column=2, pady=2)

# label de aviso
lb_aviso = Label(cadastro, text='   ')
lb_aviso.grid(row=4, column=1, columnspan=3, padx=2, pady=2, sticky='news')

# botao cadatrar
btcadastrar = Button(cadastro, text='cadastrar', command=cadastrar)
btcadastrar.grid(row=5, column=2, columnspan=3, padx=2, pady=2, sticky='news')

# botao sair
btsair = Button(cadastro, text='sair', command=cadastro.quit)
btsair.grid(row=5, column=1, pady=2, padx=2, sticky='news')


cadastro.mainloop()