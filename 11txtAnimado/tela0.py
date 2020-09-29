

def tela(mensagem):
    for i in range(12):
        print('')
        for ii in range(50):
            print(' ', end='')
            if ii == 5 and i == 5:
                print(mensagem, end='')
    print()

tela(' esta daqui é uma frase ')