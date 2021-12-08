import sqlite3 as sql

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
                   cpf = ?,
                    WHERE id = ?
                   """, (cpf, id))

    banco.commit()
    banco.close()
    
    