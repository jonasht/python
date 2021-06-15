def ehNumero(n):
    try:
        int(n)
    except:
        return False
    else:
        return True
    
    
if __name__ == '__main__':
    print(ehNumero(1))

    print(ehNumero('asdf'))
    