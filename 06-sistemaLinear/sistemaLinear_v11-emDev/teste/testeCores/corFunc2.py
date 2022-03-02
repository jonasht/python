


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
         'cyan',
         'gray',
         'light green',
         'white']

def mostrar(n):
    for nn in n:
        print(nn)
def formatar(line, conta) -> list:
    line += 1
    line = str(line)

    print(conta)
    
    formatado = list()
    contador = 0
    
    for i, c in enumerate(conta):
        if c.isalpha() and c != '=':
            
            p1 = i
            p2 = p1 + 1
            
            p1 = str(p1)
            p2 = str(p2)
            # print('p1:', type(p1), p1)
            
            nome = c+line+p1
            print(nome)
            if contador == len(cores): 
                contador = 0
            d = {
            'nome': nome,
            'p1': line+'.'+p1,
            'p2': line +'.'+p2,
            'fg': cores[contador]
            }
            formatado.append(d)
            contador += 1
    # mostrar
    # print()
    # mostrar(formatado)
    
    return formatado
if __name__ == '__main__':
    formatar(line=0, conta='33xcx8x=safsafsfasfasfsf')
