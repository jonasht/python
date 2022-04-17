lista = list(range(20))

print(' lista:', lista)

def separar_lista(lista):
    c = 0
    listaSeparada = []
    ls = []
    
    for l in lista:
        ls.append(l)
        print('l:', l, 'c:', c)
        if c == 5:
            listaSeparada.append(list(ls))
            ls.clear()
            c = 0
        c+=1
        
        
    if len(ls) != 0:
        listaSeparada.append(ls)
        
    return listaSeparada

print(separar_lista(lista))
