import numpy as np
conta = '2x-32y3z=20'
vars_conta = ['x', 'y', 'z', '=']

def remove_dirty(conta):
    vars_toRemove = ['[', ']', ',', '\'']
    for var in vars_toRemove:
        conta = conta.replace(var, '')
    return conta

def separar(conta, vars=vars_conta):
    print('conta:', conta, 'v:', vars)
    # for var in vars:
    #     conta = conta.split(var)
    #     # conta = str(conta)
    #     # conta = remove_dirty(conta)

    # conta = conta.split('  ')
    # b = list()
    # b.append(int(conta.pop()))
    # a = conta.pop()

    # a = a.split(' ')
    # a = list(map(int, a))
    # return a, b
    
def insert_1var(conta):
    conta_copy = list(conta)
    i = 0
    for c in conta:
        if c.isalpha() and conta_copy[i-1].isalpha():
            conta_copy.insert(i, '1')
            i+=1
        i+=1

    conta_copy = ''.join(conta_copy)
    return conta_copy

def get_vars(conta) -> list:
    vars = list()
    for c in conta:
        if c.isalpha():
            vars.append(c)
    return vars

def separar_linhas(conta):
    conta = conta.split('\n')
    while '' in conta:
        conta.remove('')
    return conta
        
    
def calcular(conta):
    conta = separar_linhas(conta)
    vars = get_vars(conta[0])
    
    print(conta)
    A = list()
    B = list()
    for l in conta:
        
        # a_inho, b_inho = separar(l)
        separar(l)
        # print(a_inho, b_inho, 'tipo:', type(a_inho[0]), type(b_inho[0]))
        # A.append(a_inho)
        # B.append(b_inho)

    # print(a_inho)
    # print(b_inho)
    # A = np.array(A)
    # B = np.array(B)
    # print(A, B)

    # solucao = np.linalg.solve(A, B)
    # retornar = dict()
    # for v, s in zip(vars, solucao):
    #     retornar[v] = s[0]
    # return retornar

if __name__ == '__main__':
    # conta3x3 = '''2x+6y-2z=24\n4x+5y-4z=24\n6x+5y-4z=28\n'''
    conta3x3 = '''
    2x+y1z=8\n
    1x+1y+4z=15\n
    3x+2y+0z=9\n
    '''
    
    conta3x3_v2 = '1x+2y-3z=1\n3x-1y+2z=0\n2x+1y+1z=2\n\n'

    print(calcular(conta3x3))
