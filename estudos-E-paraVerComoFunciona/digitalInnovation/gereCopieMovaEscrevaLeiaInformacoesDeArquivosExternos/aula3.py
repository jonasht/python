def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')

    arquivo.write(texto)
    arquivo.close()
    
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo)
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()

    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)
    for a in aluno_nota:
        lista_nota = a.split(',')
        aluno = lista_nota[0]
        lista_nota.pop(0)
        print('aluno:', aluno)
        # print(lista_nota)
        
        lista = list(map(float, lista_nota))
        print('media:', sum(lista) / len(lista))

if __name__ == '__main__':
    # aluno = 'mateus, 6.5, 5.9'
    # escrever_arquivo(nome_arquivo='aluno.txt', texto=aluno+'\n')
    # atualizar_arquivo(nome_arquivo='aluno.txt', texto=aluno+'\n')
    # ler_arquivo(nome_arquivo='teste.txt')
    # ler_arquivo('aluno.txt')

    media_notas('aluno.txt')

    
    