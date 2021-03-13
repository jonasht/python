
# calculo linear 
# regra de cramer

conta = [
    {'x': 1, 'y': 2, 'z': 1, '=': 8},
    {'x': 2, 'y':-1, 'z': 1, '=': 3},
    {'x': 3, 'y': 1, 'z':-1, '=': 2}
]
def enfeitar():
    print('-' * 30)
for c in conta:
    print(c)

enfeitar()
for dic in conta:
    for chave, item in dic.items():
        if chave == '=':
            print(f' = {item}', end='')      
        else:
            print(f' {item}{chave}', end='')
    print()
enfeitar()

print('delta:')

lista_delta = [[], [], []]


for i, dic in enumerate(conta):
    for chave, item in dic.items():
        if chave != '=':
            print(f' {item}', end='')
            lista_delta[i].append(item)



    print()

for i in range(3):
    for ii in range(2):
        lista_delta[i].append(lista_delta[i][ii])

enfeitar()
def mostrar_delta():
    for lista in lista_delta:
        for n in lista:
            if len(str(n)) == 1:
                print(f'  {n}', end='')
            else:
                print(f' {n}', end='')
        print()

mostrar_delta()

enfeitar()
print(lista_delta)
d_resultado = 1

for seguinte in range(3):
    for i in range(3):
        if i >= 0:
            print(lista_delta[i][i+seguinte], f'[{i}][{i}]')
        #d_resultado *= lista_delta[i][i+seguinte] 
        #print(d_resultado)
    print()
enfeitar()
mostrar_delta()
enfeitar()
for seguinte in range(3):
    for i in range(3):
        if i >= 0:
            print(lista_delta[i][i+seguinte], f'[{i}][{i}]')
        #d_resultado *= lista_delta[i][i+seguinte] 
        #print(d_resultado)
    print()

enfeitar()

mostrar_delta()
enfeitar()
print(lista_delta[2][0])
print(lista_delta[1][1])
print(lista_delta[0][2])