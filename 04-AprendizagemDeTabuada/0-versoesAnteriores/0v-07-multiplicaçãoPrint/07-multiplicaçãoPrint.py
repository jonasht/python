x1=[]
x2=[]
contar=0
for i  in range(0, 11):
    print('-'*12)
    for ii in range(0, 11):
        x1.insert(contar, i)
        x2.insert(contar, ii)
        contar = contar + 1
        print(i, 'X' ,ii, '=', i*ii)

print(x1)
print(x2)