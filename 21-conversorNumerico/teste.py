def dec_to_base(num,base):  #base maxima - 36
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

r = dec_to_base(20, 12)
print('duodecimal:', r)
print('decimal:', int(r, 12))
