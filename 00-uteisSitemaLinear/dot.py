import numpy as np
import uteis as u

print()
u.enfeitar()
print('3x3=1 dot =-=-=')
l11, l12, l13, p1 = map(float, input('linha1: ').split(' '))
l21, l22, l23, p2 = map(float, input('linha2: ').split(' '))
l31, l32, l33, p3 = map(float, input('linha3: ').split(' '))

# l11, l12, l13, p1 = 1, 2, 3, 6
# l21, l22, l23, p2 = 1, 2, 3, 8
# l31, l32, l33, p3 = 1, 2, 3, 4


a = np.array([
    [l11, l12, l13],
    [l21, l22, l23],
    [l31, l32, l33]
])

b = np.array([
    [p1],
    [p2],
    [p3]
])

print(a)
print(b)

solve = np.dot(a, b)


print('resoltado:')
print(solve)