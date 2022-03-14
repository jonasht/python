import os
def read_dir() -> list:
    pasta = './txtTeste/'
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    txts = [arq for arq in arquivos if arq.lower().endswith('.txt')]

    return txts



var = 'algo algo algo algo'


def write(var):
    dirs = read_dir()
    contador = 0
    
    while True:
        if str(contador) is not dirs[contador]:
            txt_endereco = './txtTeste/' + 'txt' + str(contador) + '.txt'
            print('entrou', txt_endereco)
            with open(txt_endereco, 'w') as arq:
                arq.write(var)

            break
        print('fora')
        
        contador += 1

# write(var)
dirs = read_dir()

for i in range(10):
    for dir in dirs:
        if str(i) in dir:
            print(i, 'true')
            break
        else:
            print(False)

# read_dir()