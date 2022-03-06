def dec_to_base(num, base):  #base maxima - 36
    base_num = ''
    while num>0:
        dig = int(num%base)
        if dig < 10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)
        num //= base
    base_num = base_num[::-1] 
     
    return base_num



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
    var = 10
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
    
    varduo = dec_to_base(var, 12)
    print('duodecimal:', varduo)
    print('convertido:', int(varduo, 12))
