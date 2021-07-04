colunas = 10
linhas = 10

ligar = False

for linha in range(linhas):
    for coluna in range(colunas):
        print(linha, coluna)
        if linha == 3 and coluna == 3:
            
            ligar = True
            break
    if ligar == True:
        break
    
print()

for linha, coluna in ((l, c) for l in range(linhas) for c in range(colunas)):
    print(linha, coluna)
    
    if linha == 3 and coluna == 3:
        break
    