

# 1 - Crie a função cria_conta, que recebe como argumento numero, titular, saldo e limite.
def cria_conta(numero, titular, saldo, limite):
    
# 2 - Dentro dela, crie o dicionário conta com os argumentos da função e retorne-o no final da função.
    conta = {'numero':numero, 'titular':titular, 'saldo':saldo, 'limite':limite}
    return conta

# 3 - Crie a função deposita, que recebe como argumento a conta e o valor e adiciona o valor ao saldo da conta.
def deposita(conta, valor):
    conta['saldo'] += valor
    
# 4 - Crie a função saca, que recebe como argumento a conta e o valor e subtrai o valor do saldo da conta.
def saca(conta, valor):
    conta['saldo'] -= valor

# 5 - Crie a função extrato, que recebe como argumento a conta e imprime o seu saldo.
def extrato(conta):
    print('saldo: ', end='')
    print(conta['saldo'], '\n')
    
conta = cria_conta(123, 'jonas', 100, 1000)
deposita(conta, 100)
saca(conta, 10)
extrato(conta)
