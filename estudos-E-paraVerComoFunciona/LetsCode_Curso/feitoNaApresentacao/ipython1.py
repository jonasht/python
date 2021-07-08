# coding: utf-8
print('hello world')
'hello world'
type(True)
1, 2, 3, 4
range(10)
[range(10)]
list(range(10))
help(if)
help('if')
help('title()')
help('title')
a = 'hello'
a.zfill()
a.isnumeric()
a[0:5]
a[0:2]
cnpj = '90.400.888/0001-42'
cnpj
c_cnpj = cnpj
cnpj = cnpj.replace('.', '')
cnpj
cnpj = cnpj.replace('-', '')
cnpj = cnpj.replace('/', '')
cnpj
cnpj.zfill(14)
cnpj
import random 
lista = list(range(20))
random.shuffle(lista)
lista
dicionario = dict('cachorro': 'branco', 'gato': 'preto')
dicionario = {'cachorro': 'branco', 'gato': 'preto'}
dicionario.keys()
dicionario
dicionario.values()
tupla = tuple(range(20))
tupla
tartarugas = ['leonardo', 'raphael', 'donatello', 'michelangelo']
for t in tartarugas:
    print(t.title())
    
import colors
for t in tartarugas:
    print(t.title())
    print(colors.green)
    
import colors as c
listaCores = [c.green, c.red, c.white, c.red, c.pink, c.yellow]
for letra in 'abcdefgh':
    print(letra)
    
for cor, letra in zip(listaCores, 'abcdefgh'):
    
    print(cor, letra)
    
    
for cor, letra in zip(listaCores, 'abcdefgh'):
    
    print(cor, letra, c.fim)
    
    
    
for cor, letra in zip(listaCores, 'abcdefgh'):
    
    print(cor, letra, c.fim, end='')
    
    
    
    
listaCores
for cor, letra, tartaruga in zip(listaCores, 'abcdefgh', tartarugas):
    
    print(cor, letra, tartaruga, c.fim, end='')
    
    
    
    
'a' in 'abcd'
celsius = [0, 10, 20.1, 34.5]
fahrenheit = []
for temp in celsius:
    temp_fahrenheit = (9/5) * temp + 32
    fahrenheit.append(temp_fahrenheit)
    
fahrenheit
[print(f) for f in fahrenheit]

 
[print(f) for f in fahrenheit]

 
lista
lista + lista
for cor, n in zip(cor, lista):
    print(cor, n)
    
    
listaCores
for i, cor in enumerate(cor):
    print(cor, i)
    
import colorama
colorama.init()
algo = 1 ,2 ,33,6,6,5,4
algo
type(algo)
listaDealgo = algo.copy()
listaDealgo = algo
listaDealgo
listaDealgo.append('algo')
random.shuffle(listaDealgo)
random.shuffle(lista)
sorted(lista)
sorted(lista)
lista +=lista
lista
random.shuffle(lista)
for l in lista:
    print(l, end='')
    
for l in lista:
    print(l, '', end='')
    
for i range(500):
    for l in lista:
        print(l, '', end='')
    random.shuffle(lista)
for i in range(500):
    for l in lista:
        print(l, '', end='')
    random.shuffle(lista)
    
for i in range(50000):
    for l in lista:
        print(l, '', end='')
    random.shuffle(lista)
    
m = [' ', '0', '1']
def contar(n=100):
    for i in range(n):
        for mm in m:
            print(c.green, mm, end='')
        random.shuffle(m)
        
contar()
contar(10000000000000)
m = [' ', ' ', ' ', '0', '1']
contar()
contar(10000)
contar(100000000000000)
from time import sleep
def contar(n=100):
    for i in range(n):
        for mm in m:
            print(c.green, mm, end='')
        random.shuffle(m)
        sleep(0.01)
        
contar(100000000000000)
def contar(n=100):
    for i in range(n):
        for mm in m:
            print(c.green, mm, end='')
        random.shuffle(m)
        sleep(0.1)
        
contar(100000000000000)
def contar(n=100):
    for i in range(n):
        for mm in m:
            print(c.green, mm, end='')
        random.shuffle(m)
        sleep(0.001)
        
contar(1000000000)
def contar(n=100):
    for i in range(n):
        for mm in m:
            print(c.green, mm, end='')
        random.shuffle(m)
        sleep(0.00001)
        
contar(1000000000)
contar(1000000)
