cs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'Y']

def l():
    print('\n', '=-'*30 + '=')

def contar(ate=5):
    for c in cs[:ate]:
        print(c, end='')
    
    

for i in range(20):
    contar(i)