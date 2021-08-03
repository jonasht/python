from typing import Container


conta = {}
def criar_conta(numero, titular, saldo, limite):
    
    conta = {'numero': numero, 'titular':titular, 'saldo':saldo, 'limite':limite}

def depositar(conta, valor):
    conta['saldo'] += valor
    
def secar(conta, valor):
    conta['saldo'] -= valor
    
def extrato(conta):
    print(f'saldo: ', end='')
    print(conta['saldo'], '\n')