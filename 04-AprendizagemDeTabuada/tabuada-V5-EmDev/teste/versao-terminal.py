import conta 
from cores import *

# versao terminal

c = conta.ContaCards()

c.set_numero1(7)
c.mostrar()

while True:
    if c.isRunning():
        
        vez = c.get_vez()
        alternativas = c.get_alternativas()
        
        print(f'\t{blue}{vez[0]} X {vez[1]}')
        print(f'{yellow}\t 0 - {alternativas[0]}\n\t 1 - {alternativas[1]}\n\t 2 - {alternativas[2]}{fim}')
        opcao = input('opcao:')
        
        
        if opcao == 's' or not(opcao.isnumeric()):
            break
        
        correto = c.check_alternativa(int(opcao))

        if correto:
            print(f'\t{green}correto{fim}')
        else:
            print(f'{red}incorreto{fim}')
    else:
        print('acabou, parabens')
        break