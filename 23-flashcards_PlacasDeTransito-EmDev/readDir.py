import os




def read_dir() -> list:
    pasta = './placasDeTransito'
    caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg")]

    return jpgs

if __name__ == '__main__':
    print('tmn lista:', len(read_dir()))
    for c in read_dir():
        print(c)