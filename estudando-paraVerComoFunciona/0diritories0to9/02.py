
def oi(nome, maisculo=False):
    
    if maisculo:
        msg = f'oi, {nome.upper()}'
    else:
        msg = f'oi, {nome}'
        
    return msg
    
print(oi('jonas'))
print(oi('jonas', 1))
print(oi('jonas', 'sim'))
