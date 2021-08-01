from tkinter import *
from conta import Conta
from random import shuffle


class FrameStart(Frame):
        def __init__(self, container):
                super().__init__(container)
                
                self.conta = Conta()
                # variaveis
                self.posicao = 0
                self.questao = list()
                
                
                self.lb_conta = Label(self, text='=-=-=-=', width=5, fg='red', font='arial 80 bold')

                self.bt0 = Button(self, text='', command=lambda: self.opcaoQuestao(1), font='arial 20 bold', width=5, borderwidth=2)
                self.bt1 = Button(self, text='', command=lambda: self.opcaoQuestao(2), font='arial 20 bold', width=5, borderwidth=2)
                self.bt2 = Button(self, text='', command=lambda: self.opcaoQuestao(3), font='arial 20 bold', width=5, borderwidth=2)

                self.lb_validacao = Label(self, text='', width=5)
                
                
                self.lb_conta.grid(row=1, columnspan=3, sticky=W+E)

                
                self.bt0.grid(row=2, sticky=W+E)
                self.bt1.grid(row=3, sticky=W+E)
                self.bt2.grid(row=4, sticky=W+E)
                self.lb_validacao.grid(row=3, column=1, sticky=W+E)
                
                self.n1 = 0
                self.n2 = 0
                self.resultado = 0
        def next(self):
                
                self.n1 = self.conta.contas[self.posicao][0]
                self.n2 = self.conta.contas[self.posicao][1] 
                self.resultado = self.n1*self.n2     
    
                self.lb_conta.config(text=f'{self.n1}X{self.n2}')
                self.questao = [
                        (self.resultado + 5),
                        (self.resultado + 1),
                        self.resultado
                ] 
                
                # >>>>>>>>>>> embaralhar questao <<<<<<<<<<<
                shuffle(self.questao)
                
                self.bt0.config(text=self.questao[0])
                self.bt1.config(text=self.questao[1])
                self.bt2.config(text=self.questao[2])
                   
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
                else:
                        self.lb_validacao.config(text='incorreto',
                                                 fg='red')
                        print(self.resultado,resultadoDado)
                
                
                self.posicao += 1
                if self.posicao == len(self.conta.contas):
                        self.bt0.config(text='', state=DISABLED)
                        self.bt1.config(text='', state=DISABLED)
                        self.bt2.config(text='', state=DISABLED)
                        self.lb_conta.config(text='=-=-=')
                        self.lb_validacao.config(text='fim') 
                        # self.destroy()
                        
                else:
                
                        self.next()

                
        
        def iniciar(self, numero1):
                # self.conta.fazerContas(numero1)
                self.conta.set_numero1(numero1)
                self.next()
                
                

if __name__ == '__main__':
        root = Tk()
        frame = FrameStart(root)
        frame.pack()
        frame.iniciar(8)
        root.mainloop()
