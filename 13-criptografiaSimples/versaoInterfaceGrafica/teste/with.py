import os
def read_dir() -> list:
    pasta = './txtTeste/'
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    txts = [arq for arq in arquivos if arq.lower().endswith('.txt')]

    return txts
    



var = 'algo algo algo algo'


def write(nameArq, txt):
    if not os.path.exists('txtTeste'):
        os.makedirs('txtTeste')

    txt_endereco = './txtTeste/' + nameArq + '.txt'
    with open(txt_endereco, 'w') as arq:
        arq.write(txt) 

        


def dir_in(dir):
    if not os.path.exists('txtTeste'):
        os.makedirs('txtTeste')
    dir = './txtTeste/'+ dir +'.txt'
    # dir = 'txt'
    
    if dir in read_dir():
        return True
    else:
        return False

def choose_nameDir():
    i = 0
    while True:
        nome = 'txt'+str(i)
        if not dir_in(nome):    
            return nome
        i += 1
if __name__ == '__main__':
    import random 
    def random_num():
        nums = ''
        for _ in range(100):
            nums += str(random.randint(10, 1000000))
        return nums
    for i in range(100):
        
        nextname = choose_nameDir()
        write(nextname, random_num())

    
