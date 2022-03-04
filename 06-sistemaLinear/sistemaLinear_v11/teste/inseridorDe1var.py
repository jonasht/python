

def insert_1var(conta):
    conta_copy = list(conta)
    i = 0

    for c in conta:
        # print('1:', c)
        if (c.isalpha() and (conta_copy[i-1].isalpha() or
            conta_copy[i-1] in '+-' or
            conta_copy[0].isalpha()
            )):
            # print('2:', c)

            conta_copy.insert(i, '1')
            i+=1
        i+=1

    conta_copy = ''.join(conta_copy)
    return conta_copy


conta = '2xyz2r=80'
conta2 = '2x+y+1z=8'
conta3 = 'x-y+1z=8'
conta4 = '+x-y+1z=8'
conta5 = '-x-y+1z=+8'
conta6 = '+x'
conta7 = '2x+y+1z=8'

def mostrar(conta):
    print()
    print(insert_1var(conta))
    print(conta)

mostrar(conta)
mostrar(conta2)
mostrar(conta3)
mostrar(conta4)
mostrar(conta5)
mostrar(conta6)
mostrar(conta7)
import uteis as u
print()
print(u.insert_1var(conta7))