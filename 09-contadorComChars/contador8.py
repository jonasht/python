
# o programa nao usa conversores numericos de python, ele feito para contar sem conversoes

duodeciamal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'Y']
binario = ['0', '1']
def l(oque = '=-', qtd = 40):
    oqueFinal = oque[0]
    print('\n', oque*qtd + oqueFinal)
l()

l()

def contador(c):
    pularLinha = 0 # pula linha para poder ficar bonito
    part = 0

    while True:
        
        qtd=int(input('type 0 to exit\ndigite 0 p/ sair\ncount until:\ncontar ate:\ndecimal n:'))

        if qtd == 0:
            break    
        qtd+=1
        parts = list() 

        for i in range(0, len(str(qtd))):
            parts.insert(i, 0)    

        for i in range (0, qtd):

            if i == 0: print(c[0], end='')
            for p in reversed(parts): # mostrar
    
                print(c[p], end='')
                
            pularLinha += 1
            if pularLinha == 10:
                print('\n')
                pularLinha = 0
            
            parts[part] = parts[part] + 1
            
            for ii in range(0, len(parts)-1):
                print(' ', end='') 
                if parts[ii] == 12:
                    parts[ii] = 0
                    parts[ii+1] = parts[ii+1] + 1
        l()            

while True:
    l()
    print('escolha uma opcao (s) para sair')
    print('1 - duodeciamal', duodeciamal)
    print('2 - binario', binario)

    opcao = input('opcao:')

    if opcao == '1':
        contador(duodeciamal)
    if opcao == '2':
        #contador(binario)
        print('desculpe opcao ainda não disponivel')
    else:
        print('opcao invalida')

    if opcao == 's' or opcao == '0': break

l()
print('\n\tfinished program/ fim de programa')
l()
  
