import random
x1=[]
x2=[]
cx=[]

contar=0

def l():
    print('=-=-=-'*15, end='')
    print('=')

for i  in range(0, 11):
    for ii in range(0, 11):
        x1.insert(contar, i)
        x2.insert(contar, ii)
        contar = contar + 1
   




for i in range(0, contar):
    cx.insert(i, i)


random.shuffle(cx)


while 1:
    l()
    op = int(input('multiplication table/tabuada de multiplicação\n1 Normal\n2 random/Aleatorio\n0 exit/Sair\nop:'))
    if op == 1:
        for i in range(0, contar):
            print(x1[i], 'x', x2[i])
        
    if op == 2:
        for i in cx:
            print(x1[i], 'x', x2[i])
    if op == 0:
        print('fim/the end')
        break