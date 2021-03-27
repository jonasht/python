from  tkinter import*

janela = Tk()
janela.title('contagem')

janela['bg']='Black'
segundos = None


#dimisões da janela
largura = 250
altura = 350

#resolução do sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

#posição da janela
posX = largura_screen/2 - largura/2
posY = altura_screen/2 - altura/2

#definir a geometry
janela.geometry('%dx%d+%d+%d' % (largura, altura, posX, posY))

def Contagem():
    global ate
    global segundos
    
    if segundos == None:
        ate = int(entrada.get())
        segundos = -1 
    if segundos == ate:
        lb_contagem['text'] = 'Fim'
    else:
        segundos = segundos + 1
        lb_contagem['text'] = segundos
        lb_contagem.after(1000, Contagem)


label = Label(janela, text="quantos segundos:", fg='green', bg='black')
label.grid(row=0, column=0)

entrada = Entry(janela, textvariable=0, borderwidth=5, bg='gray')
entrada.grid(row=0, column=1)

lb_contagem = Label(janela, fg='green', font='Times 100 bold', bg='black', text='0')
lb_contagem.grid(row=2, column=0, columnspan=2, sticky=W+E)

bt = Button(janela, fg='dark green', bg='light sea green', padx=25, pady=25,
             text='Começar',
             command=Contagem,
              font='Arial 20 bold')
bt.grid(row=3, column=0, columnspan=2, sticky=W+E)

bt_sair = Button(janela, text='sair', fg='dark green', bg='light sea green', command=janela.quit, font='Arial 20 bold')
bt_sair.grid(row=4, columnspan=2, sticky=W+E)

janela.mainloop()