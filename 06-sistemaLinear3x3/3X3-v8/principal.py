from cl_3x3 import *

# --------------------------------------------------
conta = [
    {'x': 1, 'y': 2, 'z': 1, '=': 8},
    {'x': 2, 'y': -1, 'z': 1, '=': 3},
    {'x': 3, 'y': 1, 'z': -1, '=': 2}
]
# --------------------------------------------------
def enfeitar(oque='-', qtd=50):
    print(oque * qtd)

a = cl_3x3(conta)

print()

enfeitar()
print('conta:')
a.mostrar_conta()

enfeitar()
print('matriz delta:')
a.mostrar_matriz()


print(f'delta = {a.delta}')
enfeitar()


a.mostrar_matriz('x')
print(f'deltaX = {a.deltaX}')

enfeitar()
a.mostrar_matriz('y')
print(f'deltaX = {a.deltaY}')

enfeitar()
a.mostrar_matriz('z')

print(f'deltaZ = {a.deltaZ}')

enfeitar()
print(f'delta={a.delta}, deltaX={a.deltaX}, deltaY={a.deltaY}, deltaZ={a.deltaZ}')

print(f'x = {a.deltaX}/{a.delta} = {a.x}\n')
print(f'y = {a.deltaY}/{a.delta} = {a.y}\n')
print(f'z = {a.deltaZ}/{a.delta} = {a.z}\n')

enfeitar()
print(f'x = {a.x}, y = {a.y}, z = {a.z}')
