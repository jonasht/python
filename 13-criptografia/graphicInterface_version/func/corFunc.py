
cores = ['blue',
         'green',
         'yellow',
         'red',
         'cyan',
         'gray',
         'light green',
         'white']


def formatar(line, conta) -> list:
    line += 1
    line = str(line)
    
    formatado = list()
    contador = 0
    
    for i, c in enumerate(conta):
            
        p1 = i
        p2 = p1 + 1
        
        p1 = str(p1)
        p2 = str(p2)
        
        nome = c+line+p1

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
    
    return formatado


if __name__ == '__main__':

    from main import main
    main()
    
    # fazendo teste
    # formatar(line=0, conta='33xcx8x=safsafsfasfasfsf')
