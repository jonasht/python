class Conta:
    def __init__(self, numero, titular, saldo, limite ):
        
        print('funcionando')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limete = limite
        
        
    def extrato(self):
        print('=-'*20+'=')
        print(f'nome: {self.__titular}')
        print(f'saldo: {self.__saldo}')
        print('=-'*20+'=')
    def depositar(self, valor):
        self.__saldo += valor
    
    def secar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, origem, destino, valor):
        origem.sacar(valor)
        destino.depositar(valor)



        
#conta = Conta(123, 'jonas', 520.0, 1000.0)
