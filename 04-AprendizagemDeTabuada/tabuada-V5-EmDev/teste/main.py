from tkinter import *
from conta import ContaCards
from random import randint, shuffle

class Principal(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (FrameStart, FrameMenu):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame('FrameMenu')

        self.numeros = []
        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        
        if page_name == 'FrameStart':
            frame.iniciar(self.frames['FrameMenu'].valor.get())
            


class FrameMenu(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        
        
        label = Label(self, text='menu frame')
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text='Start',
                            command=lambda: controller.show_frame('FrameStart'))
        button1.pack()
        
        self.opcaoMenu = Frame(self)
        self.valor = IntVar()
        # ======= radio Button ===========================================
        # radio button das opcao para escolher
        self.rbt1 = Radiobutton(self.opcaoMenu, text='1', variable=self.valor, value=1, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt2 = Radiobutton(self.opcaoMenu, text='2', variable=self.valor, value=2, indicatoron=0, padx=10, pady=10, bg='green')
        self.rbt3 = Radiobutton(self.opcaoMenu, text='3', variable=self.valor, value=3, indicatoron=0, padx=10, pady=10,bg='green')

        self.rbt1.pack (side=LEFT)
        self.rbt2.pack (side=LEFT)
        self.rbt3.pack (side=LEFT)


        self.rbt3.select()
        
        
        self.opcaoMenu.pack(anchor=CENTER, padx=10, pady=20)


class FrameStart(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.conta = ContaCards()
        
        # label da conta =======================================
        self.lb_conta = Label(self, text='=-=-=-=', width=5, fg='red', font='arial 80 bold')

        # botoes de opcoes de questoes =====================================
        self.bt0 = Button(self, text='', command=lambda: self.opcaoQuestao(1), font='arial 20 bold', width=5, borderwidth=2)
        self.bt1 = Button(self, text='', command=lambda: self.opcaoQuestao(2), font='arial 20 bold', width=5, borderwidth=2)
        self.bt2 = Button(self, text='', command=lambda: self.opcaoQuestao(3), font='arial 20 bold', width=5, borderwidth=2)

        self.lb_doBt0 = Label(self, text='1', font='arial 20 bold', fg='gray')
        self.lb_doBt1 = Label(self, text='2', font='arial 20 bold', fg='gray')
        self.lb_doBt2 = Label(self, text='3', font='arial 20 bold', fg='gray')

        self.lb_validacao = Label(self, text='', width=5,
                                    font='bold')
        
        
        self.lb_conta.grid(row=1, columnspan=3, sticky=W+E)

        
        self.bt0.grid(row=2, column=1,sticky=W+E)
        self.bt1.grid(row=3, column=1,sticky=W+E)
        self.bt2.grid(row=4, column=1,sticky=W+E)
        
        self.lb_doBt0.grid(row=2, column=0)
        self.lb_doBt1.grid(row=3, column=0)
        self.lb_doBt2.grid(row=4, column=0)
        self.lb_validacao.grid(row=3, column=2, sticky=W+E)
        
        
  
        # variaveis
        self.questao = list()
        
        self.n1 = 0
        self.n2 = 0
        self.resultado = 0
        
        # iniciando
        # self.iniciar(controller.valor)
    def tecla1(self, event):
            self.opcaoQuestao(1)
            print('1')
    def tecla2(self, event):
            self.opcaoQuestao(2)
    def tecla3(self, event):
            self.opcaoQuestao(3)
    
    def next(self):
            
        self.n1, self.n2 = self.conta.get_vez()
        
        self.resultado = self.n1*self.n2     
        self.lb_conta.config(text=f'{self.n1}X{self.n2}')
        
        # fazendo questoes falsas e verdadeira
        self.questao = [
                (self.resultado + randint(1, 5)),
                (self.resultado + randint(1, 4)),
                self.resultado
        ] 
        
        # >>>>>>>>>>> embaralhar questao <<<<<<<<<<<
        shuffle(self.questao)
        
        self.bt0.config(text=self.questao[0])
        self.bt1.config(text=self.questao[1])
        self.bt2.config(text=self.questao[2])
        
        # mostrando contas
        self.conta.mostrar()
        print('removidas:', self.conta.removido)
                
    def opcaoQuestao(self, opcao=0):      
            
        if opcao == 1:
            self.resposta(self.questao[0])
        if opcao == 2:
            self.resposta(self.questao[1])
        if opcao == 3:
            self.resposta(self.questao[2])

    def resposta(self, resultadoDado):
        
            
        if self.resultado == resultadoDado:
            self.lb_validacao.config(text='correto',
                                        fg='green')
            print(self.resultado, resultadoDado)
            
            self.conta.passar_vez(correto=True)
        else:
            self.lb_validacao.config(text='incorreto',
                                        fg='red')
            print(self.resultado,resultadoDado)
            
            self.conta.passar_vez(correto=False)
        
        
        
        if len(self.conta.contas) == 0:
            self.bt0.config(text='', state=DISABLED)
            self.bt1.config(text='', state=DISABLED)
            self.bt2.config(text='', state=DISABLED)
            self.lb_conta.config(text='=-=-=')
            self.lb_validacao.config(text='fim') 
                
                
        else:
        
            self.next()
        
    
    def iniciar(self, numero1):
        self.conta.set_numero1(numero1)
        self.next()
            
            

if __name__ == "__main__":
    app = Principal()
    app.mainloop()
