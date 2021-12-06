import sqlite3
from colorama.ansi import Fore

from coisasAntigas.uteis import mostrar_produtos



def show():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   SELECT * FROM produtos
                   """)

    banco.commit()
    banco.close()
def get_():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   SELECT * FROM produtos
                   """)
    # print(cursor.fetchall())
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar

def add_(nome, marca, quantidade, preco, descricao):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()  
    
    cursor.execute("""
                   INSERT INTO produtos (nome, marca, quantidade, preco, descricao) VALUES (?, ?, ?, ?, ?)
                   """, (nome, marca, quantidade, preco, descricao))  
    banco.commit()
    banco.close()
    print(f'{Fore.GREEN} {nome} {marca} {quantidade} {preco} {descricao}\ncadastro feito com sucesso{Fore.RESET}')
    
def update_(codigo, nome, marca, quantidade, preco, descricao):
    '''
    o codigo serve para poder identificar
    '''
    codigo = str(codigo)
    nome = nome.title()
    marca = marca.title()

    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   UPDATE produtos
                   SET
                   nome = ?,
                   marca = ?,
                   quantidade = ?,
                   preco = ?,
                   descricao =?
                   WHERE codigo = ?
                   """, (nome, marca, quantidade, preco, descricao, codigo))

    banco.commit()
    banco.close()

def pesquisar(opcao):
    opcao = str(opcao)
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
    mostrar_produtos()
    update_(codigo=8, nome='chinelo', marca='rabs', quantidade=5, preco=10, descricao='algo' )
    mostrar_produtos()