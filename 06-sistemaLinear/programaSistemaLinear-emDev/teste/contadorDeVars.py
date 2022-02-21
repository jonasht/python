conta = '2x+y+5z=8'
conta1 = '2x+z+5y=52' 

order = ['x', 'y', 'z']

def get_vars(conta) -> list:
    vars = list()
    for c in conta:
        print(c)
        if c.isalpha() or c == '=':
            vars.append(c)
            print(c, vars)
    # print(vars)
    return vars

def order_vars(conta):
    print(conta)

print(get_vars(conta))
print(get_vars(conta1))
