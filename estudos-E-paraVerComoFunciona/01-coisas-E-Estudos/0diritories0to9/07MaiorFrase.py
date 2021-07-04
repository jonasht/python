nomes  = ['jonas', 'fernando', 'henrique', 'sonia', 'alex']
numeros = [12, 3, 44,23, 9]
nomesN = []
for nome in nomes:
    print(nome + f", qtd: {len(nome)}")
    nomesN.append(len(nome))

    
print(f'max nomesNumeros: {max(nomesN)}')
print(f'max: {max(numeros)}')
