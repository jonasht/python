# coding: utf-8
def hello():
    print('oii mundo')
    
hello()
def calcular_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media
    
calcular_media(10, 10, 10)
resultado = calcular_media(10, 10, 10)
print('resultado:', resultado)
resultado2 = calcular_media(valor1=9, valor2=10, valor3=9)
print('resultado2:', resultado2)
