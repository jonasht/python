from random import shuffle

class Conta:
    def __init__(self):
        
        self.conta_1 = 5
        

        self.conta_2 = list(range(10))
        self.contas = list()
        
        # self.fazerContas()
        
    def set_numero1(self, n):
        self.conta_1 = n
        self.fazerContas()
        
    def fazerContas(self, numero1):
        
        for conta in self.conta_2:
            self.contas.append([numero1, conta])  
                  
    def mostrar(self):
        print(f'conta1: {self.conta_1}')
        print(f'conta2: {self.conta_2}')
        print(f'contas: {self.contas}')
    

            
        shuffle(self.contas)
if __name__ == '__main__':
    
    conta = Conta()
    print('primeiro')
    conta.mostrar()
    conta.mostrar()
    
        