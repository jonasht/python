print('= '*30)
x = 5

def print_valor():
    global x # tem q colocar global aqui para x fora somar com o X def, pois ai os2 estarao juntos
    x += 5
    print(x)
    
print_valor()
print(x)
print('\n', '- '*30)