# coding: utf-8
with open('brasil_covid.csv', 'r') as csv_file:
    linhas = csv_file.read()
    linhas = linhas.split()
    for linha in linhas:
        linha = linha.split()
        print(linha)
        
import csv
with open('user.csv', 'w', encoding='utf-8') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['pietro', 'ribeiro', 'pietro@email.com.br', 'masculino'])
    escritor.writerow(['jonas', 'programades', 'jonas@email.com.br', 'masculino'])
    
get_ipython().run_line_magic('ls', '')
get_ipython().run_line_magic('rm', 'user.csv')
with open('user.csv', 'w', encoding='utf-8', newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['pietro', 'ribeiro', 'pietro@email.com.br', 'masculino'])
    escritor.writerow(['jonas', 'programades', 'jonas@email.com.br', 'masculino'])
    
get_ipython().run_line_magic('cat', 'user.csv')
