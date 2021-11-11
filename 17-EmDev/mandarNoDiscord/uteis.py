import sqlite3
from colorama.ansi import Fore

def mostrar_produtos():
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()

    # lendo os dados
    cursor.execute("SELECT * FROM produtos;")

    for linha in cursor.fetchall():
        print(linha)

    dados.close()

def cadastrar_produto(nome, preco, quantidade=0, tamanho='', cor=''):
    
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()

    cursor.execute("""
                   INSERT INTO produtos(nome, preco, quantidade, tamanho, cores)
                   VALUES (?, ?, ?, ?, ?)
                   """, (nome, preco, quantidade, tamanho, cor))
    dados.commit()
    dados.close()
    
    
def get_dados(opcao='*'):
    opcao = str(opcao)
    # colocar id par returnar id
    if opcao=='*':
        dados = sqlite3.connect('bancoDeDados.db')
        cursor = dados.cursor()

        cursor.execute('SELECT * FROM clientes')
        return list(cursor.fetchall())
    elif opcao.isnumeric():
        opcao = int(opcao)
        dados = sqlite3.connect('bancoDeDados.db')
        cursor = dados.cursor()

        cursor.execute('SELECT * FROM produtos WHERE id = ?', (opcao,))
        return cursor.fetchall()

def pesquisar(opcao):
    if opcao.isnumeric():
        opcao = int(opcao)
        dados = sqlite3.connect('bancoDeDados.db')
        cursor = dados.cursor()

        cursor.execute('SELECT * FROM produtos WHERE codigo = ?', (opcao,))
        retornar = cursor.fetchall()
        dados.commit()
        dados.close()

    else:
        dados = sqlite3.connect('bancoDeDados.db')
        cursor = dados.cursor()

        cursor.execute('SELECT * FROM produtos WHERE nome = ?', (opcao,))
        retornar = cursor.fetchall()
        dados.commit()
        dados.close()
    
    return retornar
def cadastrar(nome, preco, quantidade, tamanho, cor):
    
    dados = sqlite3.connect('bancoDeDados.db')
    cursor = dados.cursor()

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO clientes (nome, preco, quantidade, tamanho, cor)
    VALUES (?,?,?)
    """, (nome, preco, quantidade, tamanho, cor))

    # gravando no bd
    dados.commit()

    print(f'{Fore.GREEN}Dados inseridos com sucesso.{Fore.RESET}')

    dados.close()
# cadastrar_produto(nome='bone', cor='vermelho', quantidade=2)
# mostrar_produtos()

if __name__ == '__main__':
    # print(pesquisar('bone'))
    cadastrar_produto(nome='asdf', preco=1.80, quantidade=5, tamanho='', cor='')
    mostrar_produtos()
