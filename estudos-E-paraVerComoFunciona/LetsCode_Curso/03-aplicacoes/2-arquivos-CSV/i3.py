# coding: utf-8
opt = input('o que deseja fazer\n1-cadastrar\n0-sair\nopcao:')
dados = []

while opt != '0':
    nome = input('qual eh teu nome:')
    sobrenome = input('qual eh teu sobrenome:')
    
    dados.append([nome, sobrenome])
    
    opt = input('o que deseja fazer:\n1-cadastrar\n0-sair\nopcao:')
    
print(dados)

with open('user.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)
    
   
with open('user.csv', 'r') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',')
   for row in csv_reader:
       print(row)
       
