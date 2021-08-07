from colorama.ansi import Back, Fore, Style



class Conta:
    def __init__(self, numero, titular, saldo, limite ):
        
        
        self.__numero = numero
        self.__titular = titular.title()
        self.__saldo = float(saldo)
        self.__limite = float(limite)
        
        
    def extrato(self):
        print('=-'*20+'=')
        print(Fore.BLUE+ f' nome: {Fore.RESET}{self.__titular:^5}')
        saldo = f'{self.__saldo:.2f}'
        print(Fore.BLUE+ f'saldo: {Fore.GREEN}R${saldo:^5}{Fore.RESET}')
        print('=-'*20+'=')
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, destino, valor):
        self.sacar(valor)
        destino.depositar(valor)
        print('=-'*20+'=')
        
        print(f'tranferencia:\n', 
              f'\t  de: {self.__titular:^5}\n',
              f'\tpara: {destino.__titular:^5}\n'
              f'feita com {Fore.GREEN}sucesso{Fore.RESET}')
        print('=-'*20+'=')
    
    def get_saldo(self):
        return self.__saldo
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, NovoLimite):
        self.__limite = float(NovoLimite)
    

if __name__ == '__main__':
    conta1 = Conta(123, 'jonas', 520.0, 1000.0)
    conta1.extrato()
    
    conta2 = Conta(123, 'henrique', 520.0, 1000.0)
    conta2.extrato()

    conta1.transferir(destino=conta2, valor=10)

    conta1.limite