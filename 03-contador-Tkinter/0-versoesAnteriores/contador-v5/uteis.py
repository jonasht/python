def ehNumero(n):
    n = str(n)
    return n.isnumeric()
    
if __name__ == '__main__':
    print(ehNumero(1))

    print(ehNumero('asdf'))
    