from os import system

n_de_cartas_pRecomeçar = []

n_de_cartas_pComeçar = []

# contar numero de cartas para recomeçar/antigas cartas
def Contar_n_de_cartas_pRecomeçar(n):
    if len(n) > 1:
        n = n[:]
        n_de_cartas_pRecomeçar.extend(n)
    else:
        n_de_cartas_pRecomeçar.append(n)

# contar numero de cartas p começar/novas Cartas
def Contar_n_de_cartas_pComeçar(n):
    if len(n) > 1:
        n = n[:]
        n_de_cartas_pComeçar.extend(n)
    else:
        n_de_cartas_pComeçar.append(n)



def ConverterPInt(converter):
    convertidos = []
    for c in converter:
        convertidos.append(int(c))
    
    return convertidos

    


def MostrarNCartas():
    
    system('clear')
    print('=-'*30 + '=')
    
    print(f'numero de cartas p recomeçar: {sum(ConverterPInt(n_de_cartas_pRecomeçar))}')
    print(f'numero de cartas p   começar: {sum(ConverterPInt(n_de_cartas_pComeçar))}')
    print(f'                cartas total: {sum(ConverterPInt(n_de_cartas_pRecomeçar))+sum(ConverterPInt(n_de_cartas_pComeçar))}')

       
while 1:
    print()
    
    while 1:
        MostrarNCartas()
        ns = input(f'n Para ReComeçar: ')


        if ns == '': 
            n = '1'
        else:
            n = ns
            
        if n == '0': break
        
                
        Contar_n_de_cartas_pRecomeçar(n)
    
    while 1:
        MostrarNCartas()

        ns = input(f'n Para Começar: ')
        
        if ns == '': 
            n = '1'
        else:
            n = ns
        
        if n == '0': break
        
        Contar_n_de_cartas_pComeçar(n)
    
            
    MostrarNCartas()
    continuar = input('s para sair: ')
    if continuar == 's': break
    
MostrarNCartas()