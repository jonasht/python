from random import shuffle

class Conta:
    def __init__(self):
        self.contas = list()

    # set numero 1
    def set_numero1(self, ns):
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
        
class ContaCards(Conta):
    def __init__(self):
        super().__init__()
        self.removido = []

    # pega vez
    def get_vez(self):
        return self.contas[0]
    
    # passar a vez, correto = true, tira o numero lista
    def passar_vez(self, correto=False):
        itemDaLista = self.contas.pop(0)
        
        if correto:
            self.removido.append(itemDaLista)
        else:
            self.contas.append(itemDaLista)

# fazendo o teste
if __name__ == '__main__':
    conta = ContaCards()
    conta.set_numero1([8])
    conta.mostrar()    

    print('vez:', conta.get_vez())
    conta.passar_vez(True)
    print('removida:', conta.removido)

    conta.mostrar()
    print('vez:', conta.get_vez())
    conta.passar_vez(True)
    print('removida:', conta.removido)

    for _ in range(8):
        print()
        print('vez:', conta.get_vez())
        conta.passar_vez(True)
        
        print('removida:', conta.removido)
        print('restante:', conta.contas)
    