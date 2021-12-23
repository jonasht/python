

var = 10
def to_dec(num):
    
    if '0b' in num:
        return int(num, 2)
    elif '0o' in num:
        return int(num, 8)
    elif '0x' in num:
        return int(num, 16)
    else:
        return num
        
if __name__ == '__main__':
    print(var)
    varbin = bin(var)
    print(to_dec(varbin))
    print()

    varoct = oct(var)
    print('oct:', varoct)
    print('convertido:', to_dec(varoct))
    print()

    varhex = hex(var)
    print('hex:', varhex)
    print('convertido:', to_dec(varhex))
    print()