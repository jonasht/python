print('= '*30)
x = 5

def print_valor():
    x = 15
    print(x)
    return x
    
x = print_valor()
print(x)
print('\n'*3, '- '*30)