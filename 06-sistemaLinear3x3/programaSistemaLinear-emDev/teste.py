conta = '2x-32y3z=20'
vars_conta = ['x', 'y', 'z', '=']

def remove_dirty(conta):
    vars_toRemove = ['[', ']', ',', '\'']
    for var in vars_toRemove:
        conta = conta.replace(var, '')
    return conta

def separar(conta):
    print(conta)
    for var in vars_conta:
        conta = conta.split(var)
        conta = str(conta)
        # conta = conta.replace(']', '')
        # conta = conta.replace('[', '')
        conta = remove_dirty(conta)
        # conta = conta.replace('\'', '')
        # conta = conta.replace(',', '')
        
        print(conta)
    print(conta)
    conta = conta.split('  ')
    print(conta)
    b = list()
    b.append(int(conta.pop()))
    a = conta.pop()

    print('b:', b, 'a:', a)
    a = a.split(' ')
    print('b:', b, 'a:', a)

    return a, b
    
    

    
    
separar(conta)