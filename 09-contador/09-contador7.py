c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'Y']

def l():
    print('\n', '=-=-'*15 +'=')
l()
pl = 0 # pula linha

part = 0

remove0 = True
l()
while 1:
    
    qtd=int(input('type 0 to exit\ndigite 0 p/ sair\ncount until:\ncontar ate:\ndecimal n:'))

    if qtd == 0:
        break    
    qtd+=1
    parts = []    
    for i in range(0, len(str(qtd))):
        parts.insert(i, 0)    

    for i in range (0, qtd):
        remove0 = True
        if i == 0: print(c[0], end='')
        for p in reversed(parts): # mostrar
            
            if c[p] == '0' and remove0 == True :
                print(' ', end='')
            else:
                remove0 = False        
                print(c[p], end='')
            
        pl += 1
        if pl == 10:
            print('\n')
            pl = 0
        
        parts[part] = parts[part] + 1
        
        for ii in range(0, len(parts)-1):
            print(' ', end='') 
            if parts[ii] == 12:
                parts[ii] = 0
                parts[ii+1] = parts[ii+1] + 1
    l()            


l()
print('\n\tfinished program/ fim de programa')
l()
  
