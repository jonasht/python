import sqlite3
from validate_docbr import CPF

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
    banco.commit()
    banco.close()

def pesquisar(opcao):
    opcao = str(opcao)
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

def update_(id, nome, cpf, uf, cidade, rua, numero, telefone, email):
    '''update cliente: nome, cpf, cidade, rua, numero, telefone, email
    o id serve para poder identificar
    '''
    nome = nome.title()
    uf = uf.upper()
    cidade = cidade.upper()
    rua = rua.title()
    
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   UPDATE clientes
                   SET
                   nome = ?,
                   cpf = ?,
                   uf = ?,
                   cidade = ?,
                   rua = ?,
                   numero = ?,
                   telefone = ?,
                   email = ?
                    WHERE id = ?
                   """, (nome, cpf, uf, cidade, rua, numero, telefone, email, id))

    banco.commit()
    banco.close()
    
    
def gerar_cpf(mask=False) -> str:
    cpf = CPF()
    return cpf.generate(mask)

if __name__ == '__main__':
    print(gerar_cpf())
    print(gerar_cpf(True))