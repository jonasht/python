import sqlite3 
from validate_docbr import CPF
def show():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()         
    cursor.execute("""
                   SELECT * FROM clientes
                   """) 
    print(cursor.fetchall())
    banco.commit()
    banco.close()

def update_(id, cpf):
    '''update cliente: nome, cpf, cidade, rua, numero, telefone, email
    o id serve para poder identificar
    '''

    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   UPDATE clientes
                   SET
                   cpf = ? 
                   WHERE id = ?
                   """, (cpf, id,))

    banco.commit()
    banco.close()
    
    
if __name__ == '__main__':
    cpf = CPF()
    for i in range(1, 15):
        update_(i, cpf.generate())
    show()