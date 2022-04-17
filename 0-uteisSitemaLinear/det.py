import numpy as np

print()
print('3x3 =-=-=-= det')

l11, l12, l13 = map(float, input('linha1: ').split(' '))
l21, l22, l23 = map(float, input('linha2: ').split(' '))
l31, l32, l33 = map(float, input('linha3: ').split(' '))

# l11, l12, l13 = 1, 2, 3
# l21, l22, l23 = 1, 2, 3
# l31, l32, l33 = 1, 2, 3


a = np.array([
    [l11, l12, l13],
    [l21, l22, l23],
    [l31, l32, l33]
])


print(a)

solve = np.linalg.det(a)



print('resoltado:')
print(solve)