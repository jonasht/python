import sqlite3 as sql
from sqlite3.dbapi2 import Cursor

def add_data(nome, sobrenome, login, senha, email):
    banco = sql.connect('db.db')

    cursor = banco.cursor()
    
    cursor.execute("""
                   INSERT INTO conta (nome, sobrenome, login, senha, email) 
                   VALUES(?, ?, ?, ?, ?)
                   """, (nome, sobrenome, login, senha, email))
    banco.commit()
    banco.close()

def get_senha(login):
    banco = sql.connect('db.db')

    cursor = banco.cursor()

    cursor.execute('SELECT senha FROM conta WHERE login = ?', (login,) )
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    print(retornar[0][0])
    
    return retornar[0][0]

def login_in_data(login):
    # retorna true se tem, false se nao tem
    banco = sql.connect('db.db')

    cursor = banco.cursor()

    cursor.execute('SELECT login FROM conta WHERE login = ?', (login,) )
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()

    print(retornar)
    
    return True if retornar else False

def mostrar():
    banco = sql.connect('db.db')

    cursor = banco.cursor()

    cursor.execute('SELECT * FROM conta')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    print(retornar)


if __name__ == '__main__':
    mostrar()
    # add_data(nome='jonas3', sobrenome='teixeira', login='jonas3', senha='123', email='jonas@email.com')
    mostrar()
    print()
    # get_senha('jonas')
    print(login_in_data('jonas'))