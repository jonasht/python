class Conta:
    def __init__(self, numero, titular, saldo, limite ):
        
        print('funcionando')
        self.__numero = numero
        self.__titulo = titular
        self.__saldo = saldo
        self.__limete = limite
        
        
    def extrato(self, conta):
        print(f'saldo: {self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor
    
    def secar(self, valor):
        self.__saldo -= valor
        
#conta = Conta(123, 'jonas', 520.0, 1000.0)
