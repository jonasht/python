def get_vars(conta) -> list:
    vars = list()
    for c in conta:
        # print(c)
        if c.isalpha() or c == '=':
            vars.append(c)
            # print(c, vars)
    # print(vars)
    return vars

cores = ['blue',
         'green',
         'yellow',
         'red',
         'white']


def formatar(num, conta) -> dict:
    formatado = list()
    

    print(conta)
    vars = get_vars(conta)
    vars.remove('=')
    for i, v in enumerate(vars):
        p1 = conta.find(v)
        p2 = p1 +1
        # print('i', 'v', 'p1 p2')
        # print(i, v, p1, p2)
        d = {
            'nome':v+str(num+1),
            'p1': str(num+1)+'.'+str(p1),
            'p2':str(num+1)+'.'+str(p2),
            'fg':cores[i]
        }
        formatado.append(d)
        
    # mostrar

    return formatado
if __name__ == '__main__':
    conta2x2 = 'x2y=5\n3x-5y=4'
    conta = conta2x2.split('\n')
    print(conta)
    formatado = list()
    for i, c in enumerate(conta):
        formatado.append(formatar(i, c))
    print()
    print(formatado[0][0])