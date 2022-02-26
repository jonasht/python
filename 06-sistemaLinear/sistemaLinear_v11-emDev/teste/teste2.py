import numpy as np
conta = '2x-32y3z=20'
vars_conta = ['x', 'y', 'z', '=']

def remove_dirty(conta):
    vars_toRemove = ['[', ']', ',', '\'']
    for var in vars_toRemove:
        conta = conta.replace(var, '')
    return conta


    
def insert_1var(conta):
    conta_copy = list(conta)
    i = 0

    for c in conta:
        # print('1:', c)
        if (c.isalpha() and (conta_copy[i-1].isalpha() or
            conta_copy[i-1] in '+-' or
            conta_copy[0].isalpha()
            )):
            # print('2:', c)

            conta_copy.insert(i, '1')
            i+=1
        i+=1

    conta_copy = ''.join(conta_copy)
    return conta_copy

def get_vars(conta) -> list:
    vars = list()
    for c in conta:
        # print(c)
        if c.isalpha() or c == '=':
            vars.append(c)
            # print(c, vars)
    # print(vars)
    return vars

def separar_linhas(conta):
    conta = conta.split('\n')
    while '' in conta:
        conta.remove('')
    return conta
        
def arrumar(conta, vars):
    a = list()
    b = 0

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
    
def calcular(conta):
    # removendo espaços
    while ' ' in conta:
        conta = conta.replace(' ', '')
        
    print(conta)
    conta = separar_linhas(conta)
    print('1:', conta)
    
    conta_c = list()

    for c in conta:
        conta_c.append(insert_1var(c))
    conta = conta_c
    print('2:', conta)
    vars = get_vars(conta[0])
    print('vars:', vars)
    # conta_c = conta.copy()
    # print('c', conta_c)
    A = list()
    B = list()

    for l in conta:
        print(l)
        a, b = arrumar(l, vars)
        A.append(a)
        B.append(b)
    
    A = np.array(A)
    B = np.array(B)

    print('A:', A, 'B:', B)
    conta = np.linalg.solve(A, B)
    print(conta)
    vars = vars[:-1]
    solve = dict()
    for v, c in zip(vars, conta):
        solve[v] = c

    print(solve)

if __name__ == '__main__':
    # conta3x3 = '''2x+6y-2z=24\n4x+5y-4z=24\n6x+5y-4z=28\n'''
    conta3x3v1 = '''
    2x+y+z=8\n
    x+y+4z=15\n
    3x+2y+0z=9\n
    '''
    
    conta3x3_v2 = '1x+2y-3z=1\n3x-1y+2z=0\n2x+1y+1z=2\n\n'
    
    conta3x3v3 = '''
    x+0y+0z=3
    0x+y+0z=2
    0x+0y+z=1
    '''
    
    # colocar essa conta como exemplo do programa

    conta3x3v4 = '''
    x-3y+5z=1
    x+2y+z=12
    2x-y+3z=10
    '''
    # print(calcular(conta3x3))
    calcular(conta3x3v3)
    calcular(conta3x3v4)
    # print(insert_1var('2x+y+1z=8'))