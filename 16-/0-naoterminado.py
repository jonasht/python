
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
enfeitar()
print(lista_delta)
d_resultado = 1

for i in range(3):
    print(lista_delta[i][i])
    d_resultado *= lista_delta[i][i] 
    print(d_resultado)