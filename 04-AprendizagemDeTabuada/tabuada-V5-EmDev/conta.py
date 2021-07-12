from random import shuffle

class Conta:
    def __init__(self):

        self.contas = list()
        # self.fazerContas()
        
    def set_numero1(self, n):
        self.fazerContas(n)
        
    def fazerContas(self, numero1):
        
        numero2 = list(range(10))
        for conta in numero2:
            self.contas.append([numero1, conta])  
        shuffle(self.contas)
                  
    def mostrar(self):
        print(self.contas)
        
    

if __name__ == '__main__':
    conta = Conta()
    conta.set_numero1(9)
    
    conta.mostrar()

        