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
    if '=' in vars:
        vars.remove('=')
    for i, v in enumerate(vars):
        p1 = conta.find(vars[i])
        
        vars.pop(p1)
        

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
    print(get_vars('xxx'))