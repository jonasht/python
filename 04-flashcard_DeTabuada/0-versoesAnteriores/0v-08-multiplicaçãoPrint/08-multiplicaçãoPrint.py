import random
import os

#feito no window/ it was made on windows
resposta=0
x2 = []

def l():
    print('=-=-'*15,'=')

os.system('clear')


for i in range(2, 10):
    
    x2.insert(i, i)
print(x2)
random.shuffle(x2)
while 1:

    op = int(input('\rwhich multiplication table would you like?, "e" to exit\nqual tabuada voce gostaria?, "s" para sair\nop:'))
    
    if str(op) == 's' or str(op) == 'e':
        break

    for i in x2:
        l()
        resposta = input(f'{op} X {i} = ')

        os.system('clear')    
        if resposta == op * i:
            print(f'{op} X {i} = {resposta}\ncorreto\ncorrect')
        else:
            print(f'{op} X {i} = {resposta}\nincorreto\nincorrect')


print('fim//the end')