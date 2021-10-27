
import sqlite3


def add_(nome, cpf, uf, cidade, rua, numero, telefone, email):
    nome = nome.title()
    uf = uf.upper()
    cidade = cidade.upper()
    rua = rua.title()
    
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   INSERT INTO clientes (nome, cpf, uf, cidade, rua, numero, telefone, email)
                   VALUES (?,?,?,?,?,?,?,?)
                   """, (nome, cpf, uf, cidade, rua, numero, telefone, email))

    banco.commit()
    banco.close()
def get_():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()       
    cursor.execute("""
                   SELECT * FROM clientes
                   """) 
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()    
    return retornar

def show():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()         
    cursor.execute("""
                   SELECT * FROM clientes
                   """) 
    print(cursor.fetchall())   
    banco.commit()
    banco.close()

def pesquisar(opcao):
    if opcao.isnumeric():
        opcao = int(opcao)
        dados = sqlite3.connect('bancoDeDados.db')
        cursor = dados.cursor()

        cursor.execute('SELECT * FROM clientes WHERE id = ?', (opcao,))
        retornar = cursor.fetchall()
        dados.commit()
        dados.close()

    else:
        opcao = opcao.title()
        dados = sqlite3.connect('bancoDeDados.db')
        cursor = dados.cursor()

        cursor.execute('SELECT * FROM clientes WHERE nome = ?', (opcao,))
        retornar = cursor.fetchall()
        dados.commit()
        dados.close()
    
    return retornar


if __name__ == "__main__":
    pass