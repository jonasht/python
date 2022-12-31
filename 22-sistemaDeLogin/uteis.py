import sqlite3 as sql


def init_db():
    try:
        dados = sql.connect('db.sqlite')

        cursor = dados.cursor()

        cursor.execute("""
                        CREATE TABLE Conta (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            sobrenome TEXT,
                            login TEXT,
                            senha TEXT, 
                            email TEXT,
                            frase TEXT
                        );
                    """)


        dados.commit()
        dados.close()
    except:
        print('ja existe')
    else:
        add_data(nome='admin', sobrenome='', login='admin', senha='123', email='')
        add_data('jonas', 'joson', 'jonas', '123', 'jonas@email.com' )
        
  



def add_data(nome, sobrenome, login, senha, email):
    banco = sql.connect('db.sqlite')

    cursor = banco.cursor()
    
    cursor.execute("""
                   INSERT INTO conta (nome, sobrenome, login, senha, email) 
                   VALUES(?, ?, ?, ?, ?)
                   """, (nome, sobrenome, login, senha, email))
    banco.commit()
    banco.close()

def get_senha(login):
    banco = sql.connect('db.sqlite')

    cursor = banco.cursor()

    cursor.execute('SELECT senha FROM Conta WHERE login = ?', (login,) )
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    print(retornar)
    


    return retornar[0][0] if retornar else retornar

def login_in_data(login):
    # retorna true se tem, false se nao tem
    banco = sql.connect('db.sqlite')

    cursor = banco.cursor()

    cursor.execute('SELECT login FROM Conta WHERE login = ?', (login,) )
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()

    print(retornar)
    
    return True if retornar else False


# get id 
def get_id(login) -> int:
    banco = sql.connect('db.sqlite')

    cursor = banco.cursor()

    cursor.execute("""
                   SELECT id FROM Conta where login = ?
                   """, (login, ))
    
    retornar  = cursor.fetchall()
    banco.commit()
    banco.close()
    

    retornar = retornar[0][0]
    return retornar
    
def get_dataById(id) -> dict:
    banco = sql.connect('db.sqlite')

    cursor = banco.cursor()

    cursor.execute("""
                   SELECT * FROM Conta where id = ?
                   """, (id, ))
    retornar  = cursor.fetchall()
    banco.commit()
    banco.close()
    
    retornar = retornar[0]
    retornar = dict(
        id=retornar[0],
        nome=retornar[1],
        sobrenome=retornar[2],
        login=retornar[3],
        senha=retornar[4],
        email=retornar[5],
        frase=retornar[6])

    
    return retornar


def update_msg(id, msg):
    banco = sql.connect('db.sqlite')
    cursor = banco.cursor()

    cursor.execute('''
                   UPDATE Conta
                   SET frase = ?
                   WHERE id = ?

                   ''', (msg, id))
    
    banco.commit()
    banco.close()
    
    
def get_msg(login):
    banco = sql.connect('db.sqlite')

    cursor = banco.cursor()

    cursor.execute('SELECT frase FROM Conta WHERE login = ?', (login, ))
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    print(retornar)
    return retornar [0][0] if retornar else retornar
    


def mostrar():
    banco = sql.connect('db.sqlite')

    cursor = banco.cursor()

    cursor.execute('SELECT * FROM conta')
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    print(retornar)


if __name__ == '__main__':
    # mostrar()
    # add_data(nome='rafael', sobrenome='rardes', login='rafael123', senha='123', email='jonas@email.com')
    # mostrar()


    frase='so um teste 4'
    update_msg(1, frase)
    
    data = get_dataById(1)    
    for k, v in data.items():
        print(f'{k}: {v}')
    print()
    print(get_id('jonas'))
