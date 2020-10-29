
print('\nlist(range(10))')
print(list(range(10)))

print('\nlist(range(1, 11))')
print(list(range(1, 11)))

print('\nlist(range(0, 30, 5))')
print(list(range(0, 30, 5)))

print('\nlist(range(0, 10, 3))')
print(list(range(0, 10, 3)))

print('\nlist(range(0, -10, -1))')
print(list(range(0, -10, -1)))

print('\nlist(range(0))')
print(list(range(0)))

print('\nlist(range(1, 0))')
print(list(range(1, 0)))

print('\n')

print('\n-------------------')

r = range(0, 20, 2)
print(r)

print(range(0, 20, 2))

#11 in r 
# False
if 11 in r:
    print(1)
else:
    print(0)

# 10 in r
# True
if 10 in r:
    print(1)
else:
    print(0)



print(r.index(10))


print(r[5])


print(r[:5])
print(range(0, 10, 2))
range(0, 10, 2)
print(r[-1])
