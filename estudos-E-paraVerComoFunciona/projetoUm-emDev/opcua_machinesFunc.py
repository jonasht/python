import sqlite3
from sqlite3.dbapi2 import Cursor

def add_(name=None, ip=None, url=None):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()

    cursor.execute("""
                   INSERT INTO tbl_opcua_machines (name, ip, url) VALUES(?, ?, ?)
                   """, (name, ip, url))
    
    banco.commit()
    banco.close()

    
    
# def set_name(name):
    
#     banco = sqlite3.connect('bancoDeDados.db')
#     cursor = banco.cursor()

#     cursor.execute("""
#                    UPDATE tbl_opcua_machines 
#                    SET name = ?
#                    """, (name, ))
#     banco.commit()
#     banco.close()
    
    
def get_name(nomeMaquina):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()    
    cursor.execute("""
                   SELECT name FROM tbl_opcua_machines WHERE name = ?
                   """, (nomeMaquina, ))
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0] 

# def set_ip(ip):
#     banco = sqlite3.connect('bancoDeDados.db')
#     cursor = banco.cursor()        
#     cursor.execute("""
#                    UPDATE tbl_opcua_machines 
#                    SET ip = ?
#                    """, (ip, ))  
#     banco.commit()
#     banco.close()
      
def get_ip(maquina):
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()      
    cursor.execute("""
                   SELECT ip FROM tbl_opcua_machines WHERE name = ?
                   """, (maquina, ))
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0] 

# def set_url(url):
#     banco = sqlite3.connect('bancoDeDados.db')
#     cursor = banco.cursor()       
#     cursor.execute("""
#                    UPDATE tbl_opcua_machines 
#                    SET url = ?
#                    """, (url, ))  
#     banco.commit()
#     banco.close()
    
def get_url(maquina): 
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()     
    cursor.execute("""
                   SELECT url FROM tbl_opcua_machines WHERE name = ?
                   """, (maquina, ))
    retornar = cursor.fetchall()
    banco.commit()
    banco.close()
    return retornar[0][0]    
   
def mostrar():
    banco = sqlite3.connect('bancoDeDados.db')
    cursor = banco.cursor()    
    cursor.execute('SELECT * FROM tbl_opcua_machines')
    print(cursor.fetchall())
    banco.commit()
    banco.close()



if __name__ == '__main__':
    # mostrar()
    # set_name('umNome1')
    # add_('ip', '123.123.123.123')

    # cursor.execute('DELETE FROM tbl_opcua_machines',())

    # add_('ip', '123.123.123.123')

    mostrar()

