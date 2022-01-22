import os
pasta = './placas de transito'

# for diretorio, subpastas, arquivos in os.walk(pasta):
#     for arquivo in arquivos:
        
#         print(os.path.join(os.path.realpath(diretorio), arquivo))
#     print()
    
caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
jpgs = [arq for arq in arquivos if arq.lower().endswith(".jpg")]


print('jpgs:', jpgs)