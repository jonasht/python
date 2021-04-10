
p3 = ['1', '2', '3', '4']
p2 = []
p1 = []




def mostrar():
    print('parte 3:', p3, len(p3))
    print('parte 2:', p2, len(p2))
    print('parte 1:', p1, len(p1))
    
def mudar(nomeParte, nome, para):
    nomeParte.remove(nome)
    para.append(nome)
    mostrar()
    
mostrar()
mudar(p3, '1', p2)
mudar(p3, '2', p1)
