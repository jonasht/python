from tkinter import *
from tkinter import ttk
from conta import ContaCards
from random import shuffle, randint


class FrameStart(Frame):
        def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                self.controller = controller
        
        
                # label da conta ================================================
                self.lb_conta = ttk.Label(self, text='=-=-=-=', width=5, foreground='red', font='arial 80 bold')

                # botoes de opcoes de questoes =====================================
                self.bt0 = Button(self, text='', command=lambda: self.opcaoQuestao(1), font='arial 20 bold', width=5, borderwidth=2)
                self.bt1 = Button(self, text='', command=lambda: self.opcaoQuestao(2), font='arial 20 bold', width=5, borderwidth=2)
                self.bt2 = Button(self, text='', command=lambda: self.opcaoQuestao(3), font='arial 20 bold', width=5, borderwidth=2)

                self.lb_doBt0 = ttk.Label(self, text='1', font='arial 20 bold', foreground='gray')
                self.lb_doBt1 = ttk.Label(self, text='2', font='arial 20 bold', foreground='gray')
                self.lb_doBt2 = ttk.Label(self, text='3', font='arial 20 bold', foreground='gray')

                self.lb_validacao = ttk.Label(self, text='', width=5,
                                          font='bold')
                
                
                self.lb_conta.grid(row=1, columnspan=3, sticky=W+E)

                
                self.lb_validacao.grid(row=2, column=2, sticky=W+E)
                self.bt0.grid(row=3, column=0,sticky=W+E)
                self.bt1.grid(row=3, column=1,sticky=W+E)
                self.bt2.grid(row=3, column=2,sticky=W+E)
                
                self.lb_doBt0.grid(row=4, column=0)
                self.lb_doBt1.grid(row=4, column=1)
                self.lb_doBt2.grid(row=4, column=2)
                
                
                self.conta = ContaCards()
                # variaveis
                self.questao = list()
                
                self.n1 = 0
                self.n2 = 0
                self.resultado = 0
                
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
                        self.controller.show_frame('FrameMenu')
                        self.conta.limpar()
                        
                else:
                        self.next()

        
        def iniciar(self, numero1):
                
                if type(numero1) == list:
                        self.conta.set_numero1(numero1)
                else:
                        self.conta.set_numero1([numero1])
                        
                self.next()
                
                

if __name__ == '__main__':
        import main
        # root = Tk()
        # frame = FrameStart(root, None)
        # frame.pack()
        # # frame.iniciar([8])
        # frame.iniciar(6)
        # root.mainloop()
