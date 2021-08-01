import conta 
from cores import *
from os import system

# versao terminal

c = conta.ContaCards()

while True:
    system('clear')
    print()
    print('==============================================')
    print('qual tabuada/what is tabuada would you like')
    op = input('t:')
    if op.isnumeric():
        c.set_numero1(int(op))
        break
    else:
        print('por favor, digite somente numeros')
        print('please, type only numbers')

# c.mostrar()
system('clear')

while True:
    if c.isRunning():
        
        print('==============================================')
        print('s para sair / q to quit')
        
        
        vez = c.get_vez()
        alternativas = c.get_alternativas()
        
        print(f'\t{blue}{vez[0]} X {vez[1]}')
        print(f'{yellow}\t 0 - {alternativas[0]}\n\t 1 - {alternativas[1]}\n\t 2 - {alternativas[2]}{fim}')
        opcao = input('opcao:')
        
        
        if opcao.lower() == 's' or opcao.lower() == 'q':
            break
        elif opcao.isnumeric():
            correto = c.check_alternativa(int(opcao))
            if correto:
                print(f'\t{green}correto{fim}')
            else:
                print(f'{red}incorreto{fim}')
            system('clear')
        else:
            system('clear')
            print('por favor, digite apenas numeros')
            print('please, type only numbers')
            print('\n\n')
    else:
        system('clear')
        print('acabou, parabens')
        break