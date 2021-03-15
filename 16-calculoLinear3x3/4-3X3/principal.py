from cl_3x3 import *
# --------------------------------------------------
conta = [
    {'x': 1, 'y': 2, 'z': 1, '=': 8},
    {'x': 2, 'y':-1, 'z': 1, '=': 3},
    {'x': 3, 'y': 1, 'z':-1, '=': 2}
]
# --------------------------------------------------
print()

a = cl_3x3(conta)



print('conta:')

a.mostrar_conta()

#print('lista delta:')
#
#lista_delta = montar_matriz(conta)
#mostrar_matriz(lista_delta)
#
#
#delta = somarMatriz(lista_delta)
#print(f'delta = {delta}')
#
#
#lista_deltaX = montar_matriz(conta, 'x')
#mostrar_matriz(lista_deltaX)
#deltaX = somarMatriz(lista_deltaX)
#print(f'deltaX = {deltaX}')
#
#matriz_deltaY = montar_matriz(conta, 'y')
#mostrar_matriz(matriz_deltaY)
#
#deltaY = somarMatriz(matriz_deltaY)
#print(f'deltaX = {deltaY}')
#
#enfeitar()
#matriz_deltaZ = montar_matriz(conta, 'z')
#mostrar_matriz(matriz_deltaZ)
#
#deltaZ = somarMatriz(matriz_deltaZ)
#print(f'deltaZ = {deltaZ}')
#
#enfeitar()
#print(f'delta={delta}, deltaX={deltaX}, deltaY={deltaY}, deltaZ={deltaZ}')
#
#print(f'x = {deltaX}/{delta} = {int(deltaX/delta)}')
#print(f'y = {deltaY}/{delta} = {int(deltaY/delta)}')
#print(f'z = {deltaZ}/{delta} = {int(deltaZ/delta)}')
#enfeitar()
#print(f'x = {int(deltaX/delta)}, y = {int(deltaY/delta)}, z = {int(deltaZ/delta)}')
