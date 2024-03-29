from cl_3x3 import *
# --------------------------------------------------
conta = [
    {'x': 1, 'y': 2, 'z': 1, '=': 8},
    {'x': 2, 'y': -1, 'z': 1, '=': 3},
    {'x': 3, 'y': 1, 'z': -1, '=': 2}
]
# --------------------------------------------------
def enfeitar():
    print('-' * 30)

a = cl_3x3(conta)

print()

enfeitar()
print('conta:')
a.mostrar_conta()

enfeitar()
print('matriz delta:')
a.mostrar_matriz(a.matriz_delta)


delta = a.somarMatriz(a.matriz_delta)

print(f'delta = {delta}')
enfeitar()


a.mostrar_matriz(a.matriz_deltaX)
deltaX = a.somarMatriz(a.matriz_deltaX)
print(f'deltaX = {deltaX}')

enfeitar()
a.mostrar_matriz(a.matriz_deltaY)

deltaY = a.somarMatriz(a.matriz_deltaY)
print(f'deltaX = {deltaY}')

enfeitar()
a.mostrar_matriz(a.matriz_deltaZ)

deltaZ = a.somarMatriz(a.matriz_deltaZ)
print(f'deltaZ = {deltaZ}')

enfeitar()
print(f'delta={delta}, deltaX={deltaX}, deltaY={deltaY}, deltaZ={deltaZ}')

print(f'x = {deltaX}/{delta} = {int(deltaX/delta)}')
print(f'y = {deltaY}/{delta} = {int(deltaY/delta)}')
print(f'z = {deltaZ}/{delta} = {int(deltaZ/delta)}')
enfeitar()
print(f'x = {int(deltaX/delta)}, y = {int(deltaY/delta)}, z = {int(deltaZ/delta)}')
