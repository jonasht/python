
nomes = ['robson', 'fernando', 'lucio', 'sonia', 'fernanda', 'luiza']

idades = [29, 29, 31, 21, 12, 21] 
print()
for nome, idade in zip(nomes, idades):
    print(f'{nome.title()} tem {idade} anos')

print()