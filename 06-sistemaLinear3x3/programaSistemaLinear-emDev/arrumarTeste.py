def arrumar(conta, vars):
    print('=-=-= Arrumar =-=-=')
    print('conta:', conta, 'v:', vars)
    a = list()
    b = list()

    for var in vars:
        
        conta = conta.split(var)
        # print(conta)
        # conta.remove("''")
        if var != '=':
            a.append(conta.pop(0))
        else:
            conta = ''.join(conta)

            b = conta
            
        conta = ''.join(conta)
            
        # print('a', a, 'conta:', conta)
        
    # print('='*30)
    
    # print('a:', a, 'b:', b)
    a = list(map(int, a))
    b = int(b)
    return a, b

    
vars = ['x', 'y', 'z', '=']
def mostrar(conta, vars=vars):
    print()
    A, B = arrumar(conta, vars)
    print(A, B)

conta = '1x-1y+1z=8'
conta = '1x-12y+12z=8'
conta = '1x-12y+12z=89'
conta = '-1x-12y-12z=89'
conta = '+1x+12y+12z=89'
mostrar(conta)