
#it was made on windows/feito no window
c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'Y']

def l():
    print('=-=-'*15,'=')
p1=p2=p3=0
l()
i=0

for contar in range(0, 1726):
    
    print(f'{c[p3]}{c[p2]}{c[p1]} ', end='' )
    i = 1 + i
    p1=p1+1
    if p1 == len(c):
        p2 = p2 + 1
        p1 = 0
        if p2 == len(c):
            p3 = p3 + 1
            p2 = 0
        print('\n')
    
