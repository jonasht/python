# coding: utf-8
import csv
with open('brasil_covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)
        
with open('brasil_covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header = next(leitor)
    for linha in leitor:
        if linha[2] > 1:
            print(linha)
            
        
with open('brasil_covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header = next(leitor)
    
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)
            
        
