import numpy as np
import uteis as u

ll = list()
c = 0

while True:
    break
    
    l = list(map(float, input(f'linha{c+1}: ').split(' ')))
    ll.append(l)
    print('l:', l)
    print('ll:', ll)
    c+=1
    if c == (len(ll[0]) - 1):
        break
    

ll = [
    [1, 2, 3, 6],
    [5, 10, 2, 17],
    [2, 4, 5, 11]
]

b = list()

for lista in ll:
    lin = [lista.pop()]
    b.append(lin)
    
    

a = np.array(ll)
b = np.array(b)

print('a =-=-=-=')
print(a)
print('b =-=-=-=')
print(b)

u.enfeitar()
print('resultado: ')
solve = np.linalg.solve(a, b)
print(solve)