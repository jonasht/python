from random import shuffle, randint
from tkinter import Checkbutton


class ContaCards:
    def __init__(self):
        self.contas = list()
        self.removido = list()

    # set numero 1 
    def set_numero1(self, ns):
        
        # se nao eh lista, passa para lista
        if not(type(ns) == list):
            ns = list([ns])
        
        for n in ns:
            self.fazerContas(n)
    
    # fazer conta
    def fazerContas(self, numero1):
        
        numero2 = list(range(10))
        for conta in numero2:
            self.contas.append([numero1, conta])  
        shuffle(self.contas)
    
    
    def mostrar(self):
        print(self.contas)
        
    

    # pega vez
    def get_vez(self):
        return self.contas[0]
    
    # passar a vez, correto = true, tira o numero lista
    def passar_vez(self, correto):
        itemDaLista = self.contas.pop(0)
        
        if correto:
            self.removido.append(itemDaLista)
        else:
            self.contas.append(itemDaLista)
    
    # as resposta verdadeira a falsa para mostrar
    def get_alternativas(self):
        self.resultado = self.get_vez()[0] * self.get_vez()[1]
        alternativa1 = self.resultado + randint(1,6)
        alternativa2 = self.resultado + randint(1,6)
        while alternativa1 == alternativa2:
            alternativa1 = self.resultado + randint(1,6)
            
        
        self.alternativas = [
                self.resultado,
                alternativa1,
                alternativa2
        ] 
        
        # embaralhando 
        shuffle(self.alternativas)
        return self.alternativas

    def check_alternativa(self, alternativaNum):
        if self.resultado == alternativaNum:
            self.passar_vez(True)
            return True  
        elif alternativaNum <3 and alternativaNum >=0 and self.alternativas[alternativaNum] == self.resultado:
            self.passar_vez(True)
            return True
        else:
            self.passar_vez(False)
            return False
    
    # se programa nao acabou = true, terminou = false
    def isRunning(self):
        if len(self.contas) != 0:
            return True
        else:
            return False
    def limpar(self):
        # del(self.contas)
        # del(self.removid o)
        self.contas = list()
        self.removido = list()
        
# fazendo o teste
if __name__ == '__main__':
    conta = ContaCards()
    conta.set_numero1([8])
    print('tabuada gerada:')
    conta.mostrar()    

    print('vez:', conta.get_vez())
    alternativas = conta.get_alternativas()
    print('alternativas:', alternativas)
    
    # escolhendo alternativa
    print('escolhendo alternativa 1 de 0-1-2 ')
    print('correto' if conta.check_alternativa(1) else 'incorreto')
    
    