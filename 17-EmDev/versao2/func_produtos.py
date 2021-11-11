import sqlite3
from colorama.ansi import Fore



def show():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   SELECT * FROM produtos
                   """)
    print(cursor.fetchall())

    banco.commit()
    banco.close()
def add_(nome, marca, quantidade, preco, descricao):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()  
    
    cursor.execute("""
                   INSERT INTO produtos (nome, marca, quantidade, preco, descricao) VALUES (?, ?, ?, ?, ?)
                   """, (nome, marca, quantidade, preco, descricao))  
    banco.commit()
    banco.close()
    print(f'{Fore.GREEN} {nome} {marca} {quantidade} {preco} {descricao}\ncadastro feito com sucesso{Fore.RESET}')
    
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


if __name__ == '__main__':
    pesquisa = pesquisar('celular')
    print(pesquisa)
    
    print('quantidade de pesquisa:', len(pesquisa))
    
    