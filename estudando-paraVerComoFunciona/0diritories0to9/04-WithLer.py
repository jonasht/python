with open('./04.txt') as arquivo:
    for linha in arquivo:
        print(linha)
        
        
        
        
with open('./04.txt') as arquivo:
    for i, linha in enumerate(arquivo, start=1):
        print(i, linha)
        