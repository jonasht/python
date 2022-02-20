conta = '2x+y+5z'
conta1 = '2x+z+5y' 

order = ['x', 'y', 'z']

def get_vars(conta) -> list:
    vars = list()
    for c in conta:
        if c.isalpha():
            vars.append(c)
    # print(vars)
    return vars

def order_vars(conta):
    print(conta)

print(get_vars(conta))
order_vars(conta1)